import pandas as pd

# Load the dataset
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Check for unique values in the 'Churn' column
churned_customers = df[df['Churn'] == 'Yes']

# Display the details of customers who have churned
print("Churned Customers:")
print(churned_customers)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pointbiserialr

# Load the dataset
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Check for unique values in the 'Churn' column
churned_customers = df[df['Churn'] == 'Yes']

# Display the details of customers who have churned
print("Churned Customers:")
print(churned_customers)

# Visualize the distribution of categorical features
categorical_features = ['PhoneService', 'InternetService', 'Contract']
for feature in categorical_features:
    plt.figure(figsize=(8, 5))
    sns.countplot(x=feature, hue='Churn', data=df)
    plt.title(f'{feature} Distribution by Churn')
    plt.show()

# Visualize the churn distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='Churn', data=df)
plt.title('Churn Distribution')
plt.xlabel('Churn')
plt.ylabel('Count')
plt.show()

# Explore how customer tenure relates to churn
plt.figure(figsize=(8, 5))
sns.boxplot(x='Churn', y='tenure', data=df)
plt.title('Customer Tenure vs. Churn')
plt.show()

# Visualize the distribution of monthly charges for both churned and non-churned customers
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='MonthlyCharges', hue='Churn', multiple='stack', bins=30, kde=True)
plt.title('Monthly Charges Distribution by Churn')
plt.show()

# Calculate point-biserial correlation coefficient for 'Churn' and numerical columns
correlation_churn = {}
for column in df.columns:
    if df[column].dtype != 'object':  # Check if the column is numerical
        correlation, _ = pointbiserialr(df['Churn'].map({'No': 0, 'Yes': 1}), df[column])
        correlation_churn[column] = correlation

# Display the point-biserial correlation coefficients
print("\nPoint-Biserial Correlation with Churn:")
print(pd.Series(correlation_churn).sort_values(ascending=False))

