import pandas as pd

customers = pd.DataFrame({
    "customer_id":[101, 102, 103,105],
    "name": ["Arun", "Priya", "Rahul", "Divya"],
    "city": ["Chennai", "Mumbai", "Chennai", "Bangalore"]
})
customers.to_csv("customers.csv",index=False)
print(customers)


orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4],
    "customer_id":[101, 102, 103, 104]
})
orders.to_csv("cleaned_orders.csv", index=False)
print(orders)


inner_join = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="inner"
)

print("Inner join rows:",len(inner_join))
print(inner_join)

left_join = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="left"
)

print(left_join)
no_orders = left_join[left_join["order_id"].isna()]
print("No orders:", no_orders["name"].tolist())



outer_join = pd.merge(
    customers,
    orders,
    on="customer_id",
    how="outer",
    indicator=True
)
print(outer_join)
no_customer = outer_join[outer_join["_merge"] =="right_only"]
print("order without customer:")
print(no_customer[["customer_id"]])


print("\njoin types explanation:")
print("1. inner join: returns only matching records from both datasets.")
print("2. left join: returns all records from the left dataset and matching records from the right dataset.")
print("3. outer join: returns all records from both datasets, including unmatched records.")


