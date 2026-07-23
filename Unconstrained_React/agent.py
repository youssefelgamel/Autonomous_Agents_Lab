from google import genai
from dotenv import load_dotenv
import os
import time

from prompt import PROMPT
from tools import *

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Execute Tool
def execute_tool(action, shipment):

    action = action.strip().lower()

    if action == "check_traffic":
        return check_traffic(shipment)

    elif action == "check_driver":
        return check_driver(shipment)

    elif action == "check_weather":
        return check_weather(shipment)

    elif action == "change_route":
        return change_route(shipment)

    elif action == "notify_customer":
        return notify_customer(shipment)

    elif action == "find_backup_driver":
        return find_backup_driver(shipment)

    elif action == "escalate_manager":
        return escalate_manager(shipment)

    return f"The tool '{action}' is not implemented in this environment."


# Extract Action
def extract_action(text):

    lines = text.splitlines()

    for i, line in enumerate(lines):

        if line.strip().lower() == "action:":

            if i + 1 < len(lines):
                return lines[i + 1].strip()

    return None


# Run Agent
def run_agent(shipment):

    conversation = f"""
{PROMPT}

Shipment Information

Shipment ID: {shipment['shipment_id']}
Delay Reason: {shipment['delay_reason']}
Delay Hours: {shipment['delay_hours']}
Customer: {shipment['customer']}
Package: {shipment['package']}
Customer Available: {shipment['customer_available']}
"""

    step = 1

    while True:

        time.sleep(2)

        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=conversation
        )

        answer = response.text

        print("\n")
        print("=" * 70)
        print(f"STEP {step}")
        print("=" * 70)
        print(answer)

        if "Final Answer:" in answer:
            return answer

        action = extract_action(answer)

        if action is None:
            return answer

        print("\nExecuting Tool:", action)

        observation = execute_tool(action, shipment)

        print("Observation:", observation)

        conversation += f"""

Assistant:

{answer}

System:

Observation:
{observation}
"""

        step += 1