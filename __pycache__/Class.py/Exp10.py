# Required libraries
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px  # Import Plotly library

# Load the iris dataset into a Pandas dataframe
iris_data = sns.load_dataset('iris')

# Creating the correlation matrix of the iris dataset
iris_corr_matrix = iris_data.corr()
print(iris_corr_matrix)

# Create the heatmap using the `heatmap` function of Seaborn
sns.heatmap(iris_corr_matrix, cmap='coolwarm', annot=True)

# Display the heatmap using the `show` method of the `pyplot` module from matplotlib.
plt.show()

# Visualize the correlation matrix using Plotly heatmap
fig = px.imshow(iris_corr_matrix, color_continuous_scale='coolwarm', labels=dict(x='Columns', y='Columns'))
fig.show()
