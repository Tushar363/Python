import plotly.express as px

df = px.data.iris()

fig = px.area(df, x="sepal_width", y="sepal_length",
			color="species",
			hover_data=['petal_width'],)

fig.show()
df.head()