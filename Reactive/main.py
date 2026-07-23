from shipment_data import test_cases
from rules import decide_action

passed = 0
failed = 0

print("-" * 50)
print("Delayed Shipment Management - Reactive Agent")
print("-" * 50)

for shipment in test_cases:

    actual = decide_action(shipment)

    print(f"\nShipment ID : {shipment['shipment_id']}")
    print(f"Reason      : {shipment['delay_reason']}")
    print(f"Delay       : {shipment['delay_hours']} hours")
    print(f"Customer    : {shipment['customer']}")
    print(f"Package     : {shipment['package']}")
    print(f"\nExpected : {shipment['expected_action']}")
    print(f"Actual   : {actual}")

    if actual == shipment["expected_action"]:
        print("PASS")
        passed += 1
    else:
        print("FAIL")
        failed += 1

print("\n" + "-" * 50)
print(f"Total Test Cases : {len(test_cases)}")
print(f"Passed           : {passed}")
print(f"Failed           : {failed}")
print("-" * 50)