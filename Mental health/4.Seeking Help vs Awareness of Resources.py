import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Mental Health.csv')
cross = pd.crosstab(df['seeks_treatment'], df['mental_health_history'])
cross.plot(kind='bar', stacked=True, colormap='Set2')
plt.title("Wellness Program Awareness vs Treatment")
plt.xlabel("Treatment")
plt.ylabel("Number of Respondents")
plt.tight_layout()
plt.show()
