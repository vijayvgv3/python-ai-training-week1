import pandas as pd
csv_data = """order_id,customer_id,amount
1,101,500
2,102,
3,101,700
3,101,700
4,103,300
5,104,900"""

with open("orders.csv", "w") as f:
    f.write(csv_data)

df = pd.read_csv("orders.csv")

missing_amount = df['amount'].isna().sum()
duplicates_count = df.duplicated().sum()
print(f"Missing: amount{missing_amount} | Duplicates: {duplicates_count}")


df = df.drop_duplicates()

df['amount'] = pd.to_numeric(df['amount'])
df['order_id'] = df['order_id'].astype(str)

median_val = df['amount'].median()
df['amount'] = df['amount'].fillna(median_val)
print(f"median used: {median_val}")

result = df.groupby('customer_id').agg(
    total=('amount', 'sum'),
    orders=('order_id', 'count')
)

result['total'] = result['total'].astype(int)
print(result)