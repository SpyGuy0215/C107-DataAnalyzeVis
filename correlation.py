import pandas as pd
import plotly.express as px

df = pd.read_csv('./data.csv')

student_means = df.groupby(['student_id', 'level'], as_index=False)['attempt'].mean()
print(student_means)

fig = px.scatter(student_means, x='student_id', y='level', color='attempt', size='attempt', size_max=50)

fig.show()

