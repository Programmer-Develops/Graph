import pandas as pd

import plotly.express as px

df = pd.read_csv("line_chart.csv")

fig = px.line(df, x="Year", y="Per capita income", color="Country", title='Per Capita Income')

fig.show()

# https://colab.research.google.com/drive/1Xa9o3bIDGb6jKLVDj2E5NaDtNWyxjWSE  