def decide_action(shipment):

    # Critical delays
    if shipment["delay_hours"] >= 10:
        return "Escalate to Manager"

    # Vehicle problem
    elif shipment["delay_reason"] == "Vehicle Breakdown":
        return "Reassign Driver"

    # Traffic
    elif shipment["delay_reason"] == "Traffic":
        return "Change Route"

    # Customer unavailable
    elif shipment["customer_available"] == False:
        return "Notify Customer"

    # Weather
    elif shipment["delay_reason"] == "Weather":
        return "Continue Delivery"

    else:
        return "Continue Delivery"