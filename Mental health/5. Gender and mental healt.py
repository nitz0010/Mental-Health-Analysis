import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Mental Health.csv')
remote_impact = pd.crosstab(df['gender'], df['mental_health_risk'])
remote_impact.plot(kind='bar', stacked=True, color=['#8ecae6', '#219ebc'])
plt.title("gender vs mental healt risk")
plt.xlabel("gender")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
