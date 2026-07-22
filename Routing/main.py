import os
from dotenv import load_dotenv
from google import genai

# Load secret environment variables from .env file
load_dotenv()

# Initialize Gemini Client using your free API key
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


# STEP 1: The AI Call (Single Classification Prompt)
def classify_delay_severity(incident_report: str) -> str:
    """
    Sends the late package report to Gemini ONCE to categorize it.
    """
    prompt = f"""
    You are a logistics dispatch agent for SwiftRail.
    Analyze the following shipment delay report and classify it into EXACTLY ONE category:
    - MINOR_DELAY      (Delay under 2 hours, standard cargo)
    - MODERATE_DELAY   (Delay 2 to 6 hours, high-priority cargo or perishable goods)
    - CRITICAL_DELAY   (Delay over 6 hours, VIP client, or urgent medical delivery)

    Incident Report: {incident_report}

    Respond ONLY with the single category string (MINOR_DELAY, MODERATE_DELAY, or CRITICAL_DELAY). Do not add extra text.
    """
    
    # Active Gemini 3.5 model for newly created API keys
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )
    return response.text.strip()


# STEP 2: Plain, Testable Python Code Actions (No AI involved here!)
def handle_minor_delay(report: str):
    print("--------------------------------------------------")
    print("🟢 [CATEGORY]: MINOR_DELAY")
    print("   [ACTION 1]: Updated estimated arrival time in internal database.")
    print("   [ACTION 2]: Sent automated SMS update to recipient.")
    print("--------------------------------------------------")

def handle_moderate_delay(report: str):
    print("--------------------------------------------------")
    print("🟡 [CATEGORY]: MODERATE_DELAY")
    print("   [ACTION 1]: Triggered priority rerouting via nearest express rail hub.")
    print("   [ACTION 2]: Issued 15% shipping credit voucher to customer account.")
    print("--------------------------------------------------")

def handle_critical_delay(report: str):
    print("--------------------------------------------------")
    print("🔴 [CATEGORY]: CRITICAL_DELAY")
    print("   [ACTION 1]: ESCALATION! Alerted SwiftRail logistics manager on call.")
    print("   [ACTION 2]: Dispatched emergency courier transport for direct pickup.")
    print("--------------------------------------------------")


# STEP 3: Execution Flow
if __name__ == "__main__":
    sample_report = "Shipment #SR-809 carrying organ transport coolers is delayed by 4 hours due to track signaling failure near Station B."
    
    print(f"Processing Report: '{sample_report}'\n")
    
    category = classify_delay_severity(sample_report)
    print(f"AI Model Output: {category}\n")
    
    if "MINOR_DELAY" in category:
        handle_minor_delay(sample_report)
    elif "MODERATE_DELAY" in category:
        handle_moderate_delay(sample_report)
    elif "CRITICAL_DELAY" in category:
        handle_critical_delay(sample_report)
    else:
        print("⚠️ [FALLBACK]: Unrecognized category. Escalating to human operator.")