import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

x1 = np.random.randn(100)
x2 = np.random.randn(100)+2
x3 = np.random.randn(100)+3
x4 = np.random.randn(100)+4

hist_data = [x1,x2,x3,x4]
group_labels = ['X1', 'X2', 'X3', 'X4']

fig = ff.create_distplot(hist_data, group_labels, bin_size=[.2,.1,.3,.4])

pyo.plot(fig)


