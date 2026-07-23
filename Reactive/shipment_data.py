test_cases = [
# case 1
{
    "shipment_id":"SH001",
    "delay_reason":"Traffic",
    "delay_hours":2,
    "customer":"Standard",
    "package":"Electronics",
    "customer_available":True,
    "expected_action":"Change Route"
},
# case 2
{
    "shipment_id":"SH002",
    "delay_reason":"Vehicle Breakdown",
    "delay_hours":1,
    "customer":"Standard",
    "package":"Clothes",
    "customer_available":True,
    "expected_action":"Reassign Driver"
},
# case 3
{
    "shipment_id":"SH003",
    "delay_reason":"Customer Not Available",
    "delay_hours":1,
    "customer":"Standard",
    "package":"Books",
    "customer_available":False,
    "expected_action":"Notify Customer"
},
# case 4
{
    "shipment_id":"SH004",
    "delay_reason":"None",
    "delay_hours":0,
    "customer":"Standard",
    "package":"Food",
    "customer_available":True,
    "expected_action":"Continue Delivery"
},
# case 5
{
    "shipment_id":"SH008",
    "delay_reason":"Weather",
    "delay_hours":1,
    "customer":"Standard",
    "package":"Food",
    "customer_available":True,
    "expected_action":"Continue Delivery"
},
# case 6
{
    "shipment_id":"SH009",
    "delay_reason":"Traffic",
    "delay_hours":3,
    "customer":"Standard",
    "package":"Documents",
    "customer_available":True,
    "expected_action":"Change Route"
},
# case 7
{
    "shipment_id":"SH010",
    "delay_reason":"Traffic",
    "delay_hours":8,
    "customer":"VIP",
    "package":"Medicine",
    "customer_available":True,
    "expected_action":"Escalate to Manager"
},
# case 8
{
    "shipment_id":"SH011",
    "delay_reason":"Weather",
    "delay_hours":5,
    "customer":"VIP",
    "package":"Medicine",
    "customer_available":True,
    "expected_action":"Escalate to Manager"
},
# case 9
{
    "shipment_id":"SH012",
    "delay_reason":"Traffic",
    "delay_hours":4,
    "customer":"Standard",
    "package":"Electronics",
    "customer_available":False,
    "expected_action":"Notify Customer"
}
]