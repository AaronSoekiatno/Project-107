import pandas as pd
import plotly.express as pe

df = pd.read_csv(r"scores.csv")
list = df.groupby(['student_id','level'],as_index = False)["attempt"].mean()
print(list)
graph = pe.scatter(list,x="student_id",y="level",color="attempt",size="attempt")
graph.show()

