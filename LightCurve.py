from bokeh.plotting import save, show, figure, output_file
import pandas
import numpy as np
from bokeh.models import ColumnDataSource, OpenURL, TapTool, HoverTool

# For each data file in the lc folder, change the name accordingly in the output_file and in the read_fwf function

output_file("hatp23_20190808_T35.html")

df = pandas.read_fwf("lc/hatp23_20190808_T35.txt", skiprows=15, header=None, sep="\s+")

# Initializing a figure 

p = figure(title = "A Light Curve",
           x_axis_label = "Barycentric Dynamical Time (JD)", 
           y_axis_label = "Normalized Flux")

# Error Bar calculation and plotting

df['error_low'] = df[1] - 1.96*df[2]
df['error_high'] = df[1] + 1.96*df[2]

p.segment(
    x0=df[0],
    y0=df['error_low'],
    x1=df[0],
    y1=df['error_high']
)

# Normalized flux plotting

p.scatter(x = df[0], y = df[1])
save(p)
show(p)

# The above code should output an html file. 