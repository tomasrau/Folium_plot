###### Data Source: https://www.kaggle.com/worldbank/world-development-indicators
###### Folder: 'world-development-indicators'

# Using Folium Library for Geographic Overlays
## Further exploring CO2 Emissions per capita in the World Development Indicators Dataset

### Import libraries
import folium
import pandas as pd

## Country coordinates for plotting
###### source: https://github.com/python-visualization/folium/blob/master/examples/data/world-countries.json Download the raw form: https://raw.githubusercontent.com/python-visualization/folium/588670cf1e9518f159b0eee02f75185301327342/examples/data/world-countries.json

country_geo = 'world-countries.json'
###### Read in the World Development Indicators Database
data = pd.read_csv('world-development-indicators/Indicators.csv')
data.shape
data.head()

###### Pull out CO2 emisions for every country in 2011
# select CO2 emissions for all countries in 2011
hist_indicator = 'CO2 emissions \(metric'
hist_year = 2011

mask1 = data['IndicatorName'].str.contains(hist_indicator) 
mask2 = data['Year'].isin([hist_year])

# apply our mask
stage = data[mask1 & mask2]
stage.head()


## Setup our data for plotting.
### Create a data frame with just the country codes and the values we want plotted.
plot_data = stage[['CountryCode','Value']]
plot_data.head()

###### label for the legend
hist_indicator = stage.iloc[0]['IndicatorName']
hist_indicator


## Visualize CO2 emissions per capita using Folium
###### Folium provides interactive maps with the ability to create sophisticated overlays for data visualization
# Setup a folium map at a high-level zoom @Alok - what is the 100,0, doesn't seem like lat long
map = folium.Map(location=[30, 25], zoom_start=1.5)
###### choropleth maps bind Pandas Data Frames and json geometries.  This allows us to quickly visualize data combinations
map.choropleth(geo_data=country_geo, data=plot_data,
             columns=['CountryCode', 'Value'],
             key_on='feature.id',
             fill_color='YlGnBu', fill_opacity=0.7, line_opacity=0.2,
             legend_name=hist_indicator)

### Create Folium plot
map.save('plot_data.html')

###### Import the Folium interactive html file
from IPython.display import HTML
HTML('<iframe src=plot_data.html width=900 height=500></iframe>')

#### More Folium Examples can be found at:
###### http://python-visualization.github.io/folium/docs-v0.5.0/quickstart.html#Getting-Started

#### Documentation at:
###### http://python-visualization.github.io/folium/docs-v0.5.0/modules.html