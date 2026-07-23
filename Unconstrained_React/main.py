from shipment_data import test_cases
from agent import run_agent

print("\n")
print("=" * 40)
print("UNCONSTRAINED LLM-POWERED REACT AGENT")
print("=" * 40)

for shipment in test_cases:

    print("\n")
    print("=" * 40)
    print(f"Shipment ID : {shipment['shipment_id']}")
    print("=" * 40)

    print(f"Delay Reason       : {shipment['delay_reason']}")
    print(f"Delay Hours        : {shipment['delay_hours']}")
    print(f"Customer           : {shipment['customer']}")
    print(f"Package            : {shipment['package']}")
    print(f"Customer Available : {shipment['customer_available']}")

    print("\n")
    print("-" * 40)
    print("Running Agent...")
    print("-" * 40)

    result = run_agent(shipment)

    print("\n")
    print("=" * 40)
    print("FINAL OUTPUT")
    print("=" * 40)

    print(result)

print("\n")
print("=" * 40)
print("All shipment cases have been processed.")
print("=" * 40)