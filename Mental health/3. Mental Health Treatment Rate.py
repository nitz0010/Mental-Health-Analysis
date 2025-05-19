import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Mental Health.csv')
df['seeks_treatment'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title("Treatment for Mental Health")
plt.ylabel('')
plt.tight_layout()
plt.show()
