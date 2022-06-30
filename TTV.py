from bokeh.plotting import save, show, figure, output_file
import pandas
import numpy as np
from bokeh.models import ColumnDataSource, OpenURL, TapTool, HoverTool

output_file("main.html")

p = figure(width=600, height=400,
           tools="pan, tap, save, reset, wheel_zoom, help,",
           title="Click the Dots",
           x_axis_label = "Epoch", 
           y_axis_label = "O-C")

source = ColumnDataSource(data=dict(
    x=[1, 2, 3, 4], #instead of this we need to put epoch here.
    y=[2014, 2015, 2019, 2019], #instead of year we need O-C diagram here
    detail = ["25 September", "28 August", "08 August", "28 September"],
    link=["hatp23_20140925_T100", "hatp23_20150828_CAHA", "hatp23_20190808_T35", "hatp23_20190928_T35"]
    ))

# The following code enables clicking the dot

url = "@link.html"
taptool = p.select(type=TapTool)
taptool.callback = OpenURL(url=url)

# The following code is for hover effect

hover = HoverTool()
hover.tooltips = """
  <div>
    <h3>@link</h3>
    <h4>@detail</h3>
    <div><img src="@link.png" alt="" width="200" /></div> # This image hover will work only if you save the plot as a png file in the same folder with the same name as the datafile
  </div>
"""
p.add_tools(hover)

# The following code will plot the TTV and show it

p.circle('x', 'y', size=20, source=source)
show(p)