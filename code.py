import pandas as pd
import plotly.express as px
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].to_list()

#Calculating Mean, Median, Mode, and Standard Deviation
mean = sum(data)/len(data)
median = statistics.median(data)
mode = statistics.mode(data)
standard_deviation = statistics.stdev(data)

#finding start and end vaules of the first standard deviation
first_stdevi_start, first_stdevi_end = mean - standard_deviation, mean + standard_deviation

#finding start and end values of the second standard deviation
second_stdevi_start, second_stdevi_end = mean - (2*standard_deviation), mean + (2*standard_deviation)

#finding start and end values of the third standard deviation
third_stdevi_start, third_stdevi_end = mean - (3*standard_deviation), mean + (3*standard_deviation)

#you had to create a displot firt before adding other fog statement
fig = ff.create_distplot([data], ["reading scores"], show_hist=False)

#Plotting lines for mean
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "MEAN"))

#Plotting lines for first deviation
fig.add_trace(go.Scatter(x = [first_stdevi_start, first_stdevi_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x = [first_stdevi_end, first_stdevi_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1"))

#Plotting lines for second deviation
fig.add_trace(go.Scatter(x = [second_stdevi_start, second_stdevi_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x = [second_stdevi_end, second_stdevi_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2"))

#Plotting lines for third deviation
fig.add_trace(go.Scatter(x = [third_stdevi_start, third_stdevi_start], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x = [third_stdevi_end, third_stdevi_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3"))

fig.show()

#List of data within first, second, and third standard deviation lodw - list of data within, sd - standard deviation
lodw = [result for result in data if result > first_stdevi_start and result < first_stdevi_end]
lodw = [result for result in data if result > second_stdevi_start and result < second_stdevi_end]
lodw = [result for result in data if result > third_stdevi_start and result < third_stdevi_end]

print("This is the mean:{}".format(mean))
print("This is the median:{}".format(median))
print("This is the mode:{}".format(mode))
print("This is the standard deviation:{}".format(standard_deviation))

print("{}% of data lies within first standard deviation".format(len(lodw)))
print("{}% of data lies within second standard deviation".format(len(lodw)))
print("{}% of data lies within third standard deviation".format(len(lodw)))