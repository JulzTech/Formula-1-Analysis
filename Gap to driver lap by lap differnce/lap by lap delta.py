# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:12:52 2023

@author: julsi
"""

import fastf1
import fastf1.plotting
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

from matplotlib.ticker import MaxNLocator




fastf1.plotting.setup_mpl( misc_mpl_mods=False)

race = fastf1.get_session(2023, "Mexico Grand Prix", 'R')
race.load()
race_laps = race.laps.pick_quicklaps()




Drivers = ["NOR", "RIC"]




session = []

for i in Drivers:
    
    
    
    
    
    i_laps = race_laps.pick_driver(i).reset_index()
    
    
    
    transformed_laps = i_laps.copy()
    transformed_laps.loc[:, "LapTime (s)"] = i_laps["LapTime"].dt.total_seconds() 
    
    session.append(transformed_laps)
    
driverss = len(Drivers)
    

Driver_list = []


for k in session:
    
    
    
    
    time_= k["LapTime"]
    time_list = time_.to_list()
    
    lap_number = k["LapNumber"]
    lap_number_list = lap_number.to_list()
    
    driver_ =k["Driver"]
    driver_list = driver_.to_list()
    
    compound_ =k["Compound"]
    compound_list = compound_.to_list()
    
    
    data = pd.DataFrame(data=[time_list, driver_list, lap_number_list, compound_list]).transpose()
    data.columns = ['Lap Time', 'Driver', 'Lap Number', 'Compound']

    
    
    Driver_list.append(data)
    
list(range(1,driverss))



Delta_file = []  

origin = Driver_list[0]


wer = list(range(1,driverss))

for Z in wer:


    new = Driver_list[Z]



    sub =  new['Lap Time'] - origin['Lap Time']
  
    sub1 = new['Driver']
    sub2 = new['Lap Number']
    sub3 = new['Compound']
    
    data2 = pd.DataFrame(data=[sub.dt.total_seconds(), sub1, sub2, sub3]).transpose()
    data2.columns = ['Time Delta (s)', 'Driver', 'Lap Number', 'Compound']
    
    
    
    Delta_file.append(data2)    
   
  
origin = Driver_list[0]


dub =  origin['Lap Time']

dub1 = origin['Driver']
dub2 = origin['Lap Number']
dub3 = new['Compound']

    
    
    

data3 = pd.DataFrame(data=[((dub)*0).dt.total_seconds(), dub1, dub2, dub3]).transpose()
data3.columns = ['Time Delta (s)', 'Driver', 'Lap Number', 'Compound']
  

Delta_file.append(data3)



fig, ax = plt.subplots(figsize=(18, 18))





for j in Delta_file:
    abb = j['Driver'].iloc[0]

    sns.lineplot(data=j,
                    x ="Lap Number",
                    y ="Time Delta (s)",
                    ax=ax,
                    hue = "Compound",
                    palette=fastf1.plotting.COMPOUND_COLORS,
                    #color=fastf1.plotting.driver_color(),
                    
                    
                    legend='auto'
                    )

start, end = ax.get_xlim()
start1, end1 = ax.get_ylim()

ax.xaxis.set_major_locator(MaxNLocator(integer=True))

plt.title((f"Riccardio Gap To Norris (Lap-By-Lap) \n"
             f"{race.event['EventName']} {race.event.year} Race"))

plt.grid()


ypos = [0] #x-value of the vertical line


text = "Norris Lap Time (Y = 0)" #text you wanna add to the verical line

for i in ypos:
    

    
    plt.text(y=i-0.05, x=59,  s=text, ha='center', va='center',rotation='horizontal', color = 'orange')



plt.gca().invert_yaxis()





plt.show() 