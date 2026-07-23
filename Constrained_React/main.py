import os # for file handling
from dotenv import load_dotenv # for fetching the API key from .env file
from openai import OpenAI
from pydantic import BaseModel # for structured JSON output
from typing import Literal
from tools import *
from prompt import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPEN_ROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


TOOLS = {
    "get_train_status": get_train_status,
    "get_weather": get_weather,
    "reroute_shipment": reroute_shipment
}

class AgentResponse(BaseModel):
    thought: str

    tool: Literal[
        "get_train_status",
        "get_weather",
        "reroute_shipment",
        "finish"
    ]

    arguments: dict

    answer: str | None = None


messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "user",
        "content": "Shipment S145 is delayed because train SW123 has not arrived."
    }
]

MAX_STEPS = 6

for step in range(MAX_STEPS):


    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        response_format={
            "type": "json_schema",
            "json_schema":{
                "name": "Info",
                "schema": AgentResponse.model_json_schema()
            }
        },
        temperature=0
    )

    output = AgentResponse.model_validate_json(
        response.choices[0].message.content
    )

    print(f"\nStep {step+1}")
    print(output)

    if output.tool == "finish":
        print("\nFinal Answer:")
        print(output.answer)
        break

    if output.tool not in TOOLS:
        raise ValueError(f"Unauthorized tool: {output.tool}")

    observation = TOOLS[output.tool](**output.arguments)
    print("Observation:", observation)

    print(f"Number of choices/completions: {len(response.choices)}")

    messages.append(
        {
            "role": "assistant",
            "content": response.choices[0].message.content# first answer, assistant's message, text of it
        }
    )

    messages.append(
        {
            "role": "user",
            "content": str(observation)
        }
    )