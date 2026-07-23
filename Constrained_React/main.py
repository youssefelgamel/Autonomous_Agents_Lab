import os # for file handling
from dotenv import load_dotenv # for fetching the API key from .env file
from openai import OpenAI
from pydantic import BaseModel # for structured JSON output
from typing import Literal
from tools import *

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


SYSTEM_PROMPT = """
You are SwiftRail, a railway logistics assistant.

Your objective is to determine the cause of shipment delays and recommend
appropriate corrective actions.

You are ONLY allowed to use these tools:

1. get_train_status(train_id)
   Returns the current train status.

2. get_weather(location)
   Returns weather conditions affecting railway operations.

3. reroute_shipment(shipment_id)
   Creates an alternative shipment route.

Rules:

- NEVER invent tools.
- NEVER call a tool not listed above.
- Use ONLY one tool per response.
- If you already have enough information, return tool="finish".
- Return ONLY valid JSON.
- Do NOT wrap JSON inside markdown.
- Do NOT explain your reasoning outside the JSON.

The JSON schema is:

{
    "thought": "...",
    "tool": "...",
    "arguments": {},
    "answer": null
}
"""


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

    messages.append(
        {
            "role": "assistant",
            "content": response.choices[0].message.content
        }
    )

    messages.append(
        {
            "role": "tool",
            "content": str(observation)
        }
    )