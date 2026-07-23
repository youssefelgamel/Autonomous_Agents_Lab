# Check Traffic

def check_traffic(shipment):

    if shipment["delay_reason"] == "Traffic":

        if shipment["delay_hours"] >= 4:
            return "Heavy traffic. Route B is available."

        elif shipment["delay_hours"] >= 2:
            return "Moderate traffic. Route B is available."

        else:
            return "Light traffic."

    return "No traffic issues."


# Check Driver

def check_driver(shipment):

    if shipment["delay_reason"] == "Vehicle Breakdown":
        return "Driver cannot continue."

    return "Driver is available."


# Check Weather

def check_weather(shipment):

    if shipment["delay_reason"] == "Weather":

        if shipment["delay_hours"] >= 4:
            return "Heavy rain."

        else:
            return "Light rain."

    return "Weather is clear."


# Change Route

def change_route(shipment):

    if shipment["delay_reason"] == "Traffic":
        return "Route changed successfully."

    elif shipment["delay_reason"] == "Weather":
        return "Alternative route selected."

    return "No route change required."


# Notify Customer

def notify_customer(shipment):

    if shipment["customer_available"]:
        return "Customer notified successfully."

    return "Customer is not available."


# Find Backup Driver

def find_backup_driver(shipment):

    if shipment["delay_reason"] == "Vehicle Breakdown":
        return "Backup driver assigned."

    return "No backup driver needed."


# Escalate Manager

def escalate_manager(shipment):

    if shipment["customer"] == "VIP":
        return "Case escalated to the logistics manager."

    return "Escalation is not required."