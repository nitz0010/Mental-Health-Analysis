import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Mental Health.csv')
remote_impact = pd.crosstab(df['stress_level'], df['sleep_hours'])
remote_impact.plot(kind='bar', stacked=True, color=['#8ecae6', '#219ebc'])
plt.title("stress level vs sleep hours")
plt.xlabel("st ress")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
