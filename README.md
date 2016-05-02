a3-HvanTol-MWeirath
===============

## Team Members

1. Michelle Weirathmueller (michw)
2. Helena van Tol (hmvantol)

## Interactive World Ocean Atlas

For this project, we developed an interactive visualization using data from the [World Ocean Atlas 2013](https://www.nodc.noaa.gov/OC5/woa13/woa13data.html) dataset. We show two main panels: one is a global map of surface temperature or salinity (the user can choose which one they'd like to view). Clicking on the map brings up the temperature and salinity profiles corresponding to that location in the other panel. 


## Running Instructions

Access our visualization at http://cse512-16s.github.io/a3-michellejw-hmvantol/ or download this repository and run `python -m SimpleHTTPServer 9000` and access this from http://localhost:9000/.

If you don't see the map at first, expand your browser window width until the two diagrams are side-by-side.

## Story Board

### Data domain
Since we are both Oceanography graduate students, we decided to go with an ocean-related dataset: the [World Ocean Atlas 2013 (WOA 2013)](http://www.nodc.noaa.gov/OC5/woa13/woa13data.html). There are a number of simple variables that are often used by oceanographers to study the movements of different water masses. Some of those variables include temperature, salinity, and dissolved oxygen. The datasets provided through the WOA website are available as gridded files for each type of measurement. At each gridded location, the files contain a measurement "profile", which is a series of values interpolated to pre-defined depth bins. Oceanographers often look at measurements as a function of depth to understand the vertical stratification throughout the water column at a particular location. We will begin our visualization using one-degree gridded annual temperature, averaged between 2005-2012.

Oceanographers regularly explore large multi-variable data sets in 4D space (longitude, latitude, depth, time). Common visualizations include [contour maps](http://www.ospo.noaa.gov/Products/ocean/sst/contour/), [depth profiles](https://en.wikipedia.org/wiki/Thermocline#/media/File:THERMOCLINE.png), and [T-S diagrams](https://oceanpython.files.wordpress.com/2013/02/ts_diagram.png). On research cruises, oceanographers will interact with data as it is being collected to make decisions about where to sample along the cruise track and at which depths. Data exploration could be supported by linking multiple commonly used visualizations, allowing the user to observe multiple dimensions at once.

Here is our sketch of the visualization:

<img src="https://github.com/michellejw/a3_HvT_MW/blob/Master/sketch1.jpg" width="614">

We envision a map of sea surface temperature that the viewer can click to bring up depth profiles from different locations.
This is a sketch of the type of map we are envisioning (though for now, note that coordinates are not labeled correctly and the default image color map could probably be better).

![tempmap](https://github.com/michellejw/a3_HvT_MW/blob/Master/woa_map.png)

We brainstormed several other versions of this visualization, but eventually decided to go with our first idea because it seems more intuitive.

In this version, the viewer can click on the map to bring up a depth profile or click on a depth in the profile to change the depth visualized on the map.

<img src="https://github.com/michellejw/a3_HvT_MW/blob/Master/sketch2.jpg" width="614">

This one is similar to the previous idea, but the depth profile shows an entire latitude or longitude range.

<img src="https://github.com/michellejw/a3_HvT_MW/blob/Master/sketch5.jpg" width="614">

In this sketch, the depth profile hovers next to the mouse icon and changes depending on the map location.

<img src="https://github.com/michellejw/a3_HvT_MW/blob/Master/sketch3.jpg" width="614">

In this visualization we linked a T-S diagram to a depth profile to show the interaction between temperature and salinity rather than a map. The user could use brushing to highlight different regions of the T-S diagram or the depth profile.

<img src="https://github.com/michellejw/a3_HvT_MW/blob/Master/sketch4.jpg" width="614">



### Changes between Storyboard and the Final Implementation

After going to office hours, we learned that D3 doesn't really interpolate colours on a map. We would have to use another javascript library to make this sort of map. Instead, Michael came up with an idea where we could generate the base map in python and then overlay interactive rectangles on top of the background.

Originally we were going to map either temperature or salinity. After creating the visualization for temperature we decided to add salinity to make things more interesting. The user can toggle between two different surface maps for temperature and salinity and can visualize both salinity and temperature lines on the depth profile.

We made longitude and latitude appear upon hovering over the map to help the user find and remember specific locations.

After the lecture on colour, we moved away from the rainbow palette and used an XXXXXXX palette instead. This palette is better because _________________________________.


## Development Process

Include:
- Breakdown of how the work was split among the group members.
- A commentary on the development process, including answers to the following questions:
  - Roughly how much time did you spend developing your application?
  - What aspects took the most time?
