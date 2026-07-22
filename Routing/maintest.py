import os
from google import genai

# Initialize Gemini Client (Uses free Gemini API from Google AI Studio)
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# 1. AI Categorization Call (Only ONE LLM call!)
def classify_swiftrail_issue(incident_report: str) -> str:
    prompt = f"""
    You are a logistics dispatcher for SwiftRail. 
    Analyze the following train incident report and classify it into EXACTLY ONE category:
    - MINOR_DELAY
    - COLD_CHAIN_ALERT
    - CRITICAL_FAILURE

    Incident Report: {incident_report}

    Respond ONLY with the single category string.
    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text.strip()

# 2. Plain Python Code Functions
def handle_minor_delay():
    print("[ACTION] Logged minor delay. Automated email update sent to customer.")

def handle_cold_chain_alert():
    print("[ACTION] Rerouting train container to nearest refrigeration hub!")

def handle_critical_failure():
    print("[ACTION] ESCALATION: Emergency maintenance crew dispatched.")

# 3. Execution
if __name__ == "__main__":
    test_incident = "Train #402 reports refrigerated wagon temp increased by 12 degrees. Perishable medicine onboard."
    
    category = classify_swiftrail_issue(test_incident)
    print(f"Classified Category: {category}")
    
    if category == "MINOR_DELAY":
        handle_minor_delay()
    elif category == "COLD_CHAIN_ALERT":
        handle_cold_chain_alert()
    elif category == "CRITICAL_FAILURE":
        handle_critical_failure()
    else:
        print("[FALLBACK] Manual inspection required.")