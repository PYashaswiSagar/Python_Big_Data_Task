import csv
import json
from faker import Faker

fake = Faker()

def generate_orders(start_id, end_id):
    orders = []
    for i in range(start_id, end_id + 1):
        orders.append({
            "id": i,
            "customer_id": f"CUST{i:04d}",
            "transaction_date": fake.date_between(start_date='-1y', end_date='today').strftime("%Y-%m-%d"),
            "order_status": fake.random_element(elements=('Processing', 'Shipped', 'Delivered', 'Cancelled')),
            "shipping_info": f"{fake.random_element(elements=['FedEx', 'UPS', 'USPS', 'DHL'])} Tracking #{fake.bothify(text='???#####')}"
        })
    return orders

# Generate datasets
orders_1_100 = generate_orders(1, 100)
orders_101_200 = generate_orders(101, 200)
orders_201_300 = generate_orders(201, 300)

# Save orders_1_100 as CSV
with open('orders_1_100.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=orders_1_100[0].keys())
    writer.writeheader()
    writer.writerows(orders_1_100)

# Save orders_201_300 as CSV
with open('orders_201_300.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=orders_201_300[0].keys())
    writer.writeheader()
    writer.writerows(orders_201_300)

# Save orders_101_200 as JSON
with open('orders_101_200.json', 'w') as f:
    json.dump(orders_101_200, f, indent=2)

print("Files generated:")
print(" - orders_1_100.csv")
print(" - orders_101_200.json")
print(" - orders_201_300.csv")

