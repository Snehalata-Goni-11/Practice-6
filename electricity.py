units = int(input("Enter the number of units consumed: "))
rate_per_unit = 5
total_bill = units * rate_per_unit

print(f"Units Consumed: {units}")
print(f"Total Bill:₹{total_bill}")

if total_bill > 1000:
    discount = total_bill * 0.10
    final_bill = total_bill - discount
    print(f"Discount Applied: ₹{discount}")
    print(f"Final Bill: ₹{final_bill}")
else:
    print("No discount applied.")
    print(f"Final Bill:₹{total_bill}")