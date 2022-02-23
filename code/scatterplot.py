import pandas as pd
import plotly.express as px

df = pd.read_csv("covid data.csv")
fig = px.scatter(df, x="date", y="number of cases",
	          size="Percentage",color="Country",
                   size_max=60)
fig.show()
