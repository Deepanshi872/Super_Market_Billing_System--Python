import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

# 1. Sales Prediction:

# Load data
order_items = pd.read_csv("C:/Users/deepa/Downloads/order_items.csv")
orders = pd.read_csv("C:/Users/deepa/Downloads/orders.csv")
geolocation= pd.read_csv("C:/Users/deepa/Downloads/geolocation.csv")
payments= pd.read_csv("C:/Users/deepa/Downloads/payments.csv")
products= pd.read_csv("C:/Users/deepa/Downloads/products.csv")
sellers= pd.read_csv("C:/Users/deepa/Downloads/sellers.csv")
customers= pd.read_csv("C:/Users/deepa/Downloads/customers.csv")

# Merge and prepare data
data = pd.merge(order_items, orders, on='order_id')
data['order_purchase_month'] = pd.to_datetime(data['order_purchase_timestamp']).dt.to_period('M')
monthly_sales = data.groupby('order_purchase_month')['price'].sum().reset_index()

# Prepare for linear regression
monthly_sales['Month'] = monthly_sales['order_purchase_month'].astype(str)
monthly_sales['Month'] = pd.to_datetime(monthly_sales['Month'])
monthly_sales['Month_Num'] = np.arange(len(monthly_sales))
X = monthly_sales[['Month_Num']]
y = monthly_sales['price']

# Linear Regression
model = LinearRegression()
model.fit(X, y)
monthly_sales['Predicted'] = model.predict(X)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales['Month'], monthly_sales['price'], label='Actual Sales')
plt.plot(monthly_sales['Month'], monthly_sales['Predicted'], label='Predicted Sales', linestyle='--')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Monthly Sales Prediction')
plt.legend()
plt.show()


# 2. Customer Segmentation (Clustering):

# Load data
orders = pd.read_csv("C:/Users/deepa/Downloads/orders.csv")
order_items = pd.read_csv("C:/Users/deepa/Downloads/order_items.csv")

# Merge orders and order_items
data = pd.merge(orders, order_items, on='order_id')

# Calculate RFM
now = datetime.now()
data['order_purchase_timestamp'] = pd.to_datetime(data['order_purchase_timestamp'])

rfm_table = data.groupby('customer_id').agg({
    'order_purchase_timestamp': lambda x: (now - x.max()).days,
    'order_id': 'count',
    'price': 'sum'
}).reset_index()

rfm_table.columns = ['customer_id', 'Recency', 'Frequency', 'Monetary']

print(rfm_table.head())






