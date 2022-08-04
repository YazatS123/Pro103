from google.colab import files
data_to_load = files.upload()
import pandas as pd
import plotly.express as px
data = pd.read_csv("Copy+of+data+-+data.csv")
fig = px.scatter(data, x = "date", y = "cases", color = "country", title = "COVID cases")
fig.show()
#You can import the file given as sample and run the code with that file imported in the import files command to check my work