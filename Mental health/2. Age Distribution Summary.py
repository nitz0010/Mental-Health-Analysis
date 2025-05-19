import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Mental Health.csv')

df.columns = df.columns.str.strip()

df['age'] = pd.to_numeric(df['age'], errors='coerce')

df = df[(df['age'] >= 10) & (df['age'] <= 100)]

plt.hist(df['age'], bins=15, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
