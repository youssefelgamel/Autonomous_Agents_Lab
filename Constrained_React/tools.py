#In real Agent the tools should fetch the data from current data sources, but it's just a demo
"""
WEATHER_DB = {
    "Alexandria": {
        "weather": "Sunny"
    },
    "Cairo": {
        "weather": "Heavy Rain"
    }
    .....
}

TRAIN_DB = {
    "SW123": {
        "status": "Delayed",
        "delay": 42,
        "location": "Alexandria"
    },

    "SW200": {
        "status": "On Time",
        "delay": 0,
        "location": "Cairo"
    }
    .......
}
"""

def get_train_status(train_id: str):

    return {
        "train_id": train_id,
        "status": "Delayed",
        "delay_minutes": 45,
        "location": "Boston"
    }


def get_weather(location: str):

    return {
        "location": location,
        "weather": "Heavy Rain",
        "impact": "Possible signal failures and slower train speeds."
    }

def reroute_shipment(shipment_id: str):

    return {
        "shipment_id": shipment_id,
        "status": "Rerouted",
        "new_route": "Boston -> Houston"
    }