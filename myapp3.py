#!/usr/bin/env python
# coding: utf-8

# load libraries
#get_ipython().run_line_magic('matplotlib', 'inline')
#import pandas as pd
#import numpy as np
#mport matplotlib.pyplot as plt
#mport geopandas as gpd
#import seaborn as sns
#import time
#import os
#from pysal.esda.mapclassify import Quantiles, Equal_Interval
# Import libraries
#import geopandas
#import json
#from datetime import datetime

from bokeh.io import output_notebook, show, output_file
from bokeh.plotting import figure
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, NumeralTickFormatter
from bokeh.palettes import brewer

from bokeh.io.doc import curdoc
from bokeh.models import Slider, HoverTool, Select
from bokeh.layouts import widgetbox, row, column

import numpy as np
import pandas as pd


from bokeh.io import show, output_notebook
from bokeh.plotting import figure
from bokeh.palettes import viridis
from bokeh.models import ColumnDataSource, FactorRange, Legend

from bokeh.io import output_file, show
from bokeh.plotting import figure

'''


df2 = pd.read_csv("us_states_covid19_daily.csv") #


df2 = pd.read_csv("us_states_covid19_daily.csv") #
df2["datetime"] = (pd.to_datetime(df2['date'], format="%Y%m%d"))

#Calculating the date as the days since the first outbreak was recorded .
df2["DateTime"] = pd.to_datetime(df2['date'], format='%Y%m%d', errors='ignore')
d0 = datetime(2020, 1, 22)
df2['DayNumber'] = df2.apply(lambda x : (x["DateTime"]-d0).days, axis=1)
df2 = df2.drop(columns=['DateTime'])
df = pd.DataFrame(df2[["datetime",'DayNumber',"state",'death']])


df = df.pivot(index='datetime', columns='state', values='death')
df["Date"] = df.index


df.fillna(0, inplace=True)



df



df = df.reset_index()
df.head()

df.save_csv()
'''

df = pd.read_csv("df_death.csv")   
df = df[df.columns[1:]]


from bokeh.io import show, output_notebook
from bokeh.plotting import figure
from bokeh.palettes import viridis
from bokeh.models import ColumnDataSource, FactorRange, Legend
#from bokeh.models.tools import HoverTool


states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VT': 'Vermont',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}






from bokeh.plotting import figure

p = figure(x_axis_type="datetime", plot_width=700,plot_height=400, title="Total number of deaths over time",
           toolbar_location=None, tools="",y_range=[0,21640])

state = "NY"
# Create a ColumnDataSource: source

source = ColumnDataSource(data={'deaths': df[state],
                                'Date': pd.to_datetime(df["Date"]).tolist(),
                               })    


p.vbar(x="Date", top="deaths", width=10,source=source)

menu = Select(options=list(states.values()),value= "New York",title = "Select State")

states_short = {}
for i in range(len(list(states.values()))):
    states_short[list(states.values())[i]] = list(states.keys())[i]



def callback(attr, old, new):
    state = states_short[menu.value]
    source.data = {'deaths': df[state].tolist(),
                                'Date': pd.to_datetime(df["Date"]).tolist(),
                               }
menu.on_change("value",callback)



from bokeh.io import curdoc
from bokeh.layouts import column
# Create layout and add to current document
layout = column(p,menu)
#show(p)
curdoc().add_root(layout)  
