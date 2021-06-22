import plotly.express as px
import pandas as pd
import csv

reader = pd.read_csv('data.csv')
mean = reader.groupby(["student_id", "level"], as_index = False)['attempt'].mean()
figure = px.scatter(mean, x = 'student_id' , y = 'level' , color = 'attempt' , size = 'attempt')
figure.show()