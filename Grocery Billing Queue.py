
print("=== Grocery Billing Queue ===\n")

customers = []
customers_served = 0
total_sales = 0

serving = True

while serving:
    name = input("Enter customer's name: ")
    items_count = int(input(f"Hello {name}! Enter number of items: "))

    bill = []
    item_idx = 1

    while item_idx <= items_count:
        item_name = input("Enter item name: ")
        price = float(input("Enter item price: "))

        if price <= 0:
            print("Invalid price. Please enter a positive price.\n")
            continue

        bill.append([item_name, price])
        item_idx += 1

    customer_total = 0

    for item in bill:
        customer_total += item[1]

    customers.append([name, bill, customer_total])
    customers_served += 1
    total_sales += customer_total

    print(f"\nTransaction complete, {name}!")
    print(f"Customer bill: Rs. {customer_total:.2f}\n")

    again = input("Next customer? (yes/no): ").strip().lower()

    if again != "yes":
        serving = False

print("\n===== DAILY GROCERY BILLING REPORT =====")

for customer in customers:
    print(f"\nCustomer: {customer[0]}")
    print("---------------------------------------")

    for item in customer[1]:
        print(f"{item[0]}: Rs. {item[1]:.2f}")

    print("---------------------------------------")
    print(f"Customer total: Rs. {customer[2]:.2f}")

print("\n===== DAILY SUMMARY =====")
print(f"Customers served: {customers_served}")
print(f"Total sales: Rs. {total_sales:.2f}")
print("Grocery billing session closed. Goodbye!")
