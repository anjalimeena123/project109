import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv("data4.csv")
data=df["reading score"].tolist()
mean=sum(data)/len(data)
std_deviation=statistics.stdev(data)
median=statistics.median(data)
mode=statistics.mode(data)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
fig=ff.create_distplot([data],["Reading scores"],show_hist=False)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines" , name="Mean"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()
listofdatasd1=[result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
listofdatasd2=[result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
listofdatasd3=[result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]
print("Mean of this value is=".mean)
print("Mode of this value is=".mode)
print("Median of this value is=".median)
print("std_Deviation of this value is=".std_Deviation)