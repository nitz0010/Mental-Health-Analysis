import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Mental Health.csv')

df.columns = df.columns.str.strip()

df['gender'] = df['gender'].fillna('Unknown')

df['gender'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
