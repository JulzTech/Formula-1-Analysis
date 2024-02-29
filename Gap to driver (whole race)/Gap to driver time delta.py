# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:42:36 2023

@author: julsi
"""

import fastf1
import fastf1.plotting
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd

from matplotlib.ticker import MaxNLocator

fastf1.plotting.setup_mpl( misc_mpl_mods=False)

race = fastf1.get_session(2023, "Mexico", 'R')
race.load()




Drivers = ["VER", "NOR", "LEC", "TSU",  "HAM", "RIC", "PIA"]




session = []

for i in Drivers:
    
    
    
    
    
    i_laps = race.laps.pick_driver(i).reset_index()
    
    
    
    transformed_laps = i_laps.copy()
    transformed_laps.loc[:, "LapTime (s)"] = i_laps["LapTime"].dt.total_seconds() 
    
    session.append(transformed_laps)
    
driverss = len(Drivers)



Driver_list = []



for k in session:
    
    
    
    
    time_= k["Time"]
    time_list = time_.to_list()
    
    lap_number = k["LapNumber"]
    lap_number_list = lap_number.to_list()
    
    driver_ =k["Driver"]
    driver_list = driver_.to_list()
    
    
    
    data = pd.DataFrame(data=[time_list, driver_list, lap_number_list]).transpose()
    data.columns = ['Time', 'Driver', 'Lap Number']

    
    
    Driver_list.append(data)
    




Delta_file = []  

origin = Driver_list[0]


driver_range = list(range(1,driverss))

for Z in driver_range:


    new = Driver_list[Z]



    sub =  new['Time'] - origin['Time']
  
    sub1 = new['Driver']
    sub2 = new['Lap Number']
    
    data2 = pd.DataFrame(data=[sub.dt.total_seconds(), sub1, sub2]).transpose()
    data2.columns = ['Time Delta (s)', 'Driver', 'Lap Number']
    
    
    
    Delta_file.append(data2)    
   
  



dub =  origin['Time']

dub1 = origin['Driver']
dub2 = origin['Lap Number']

    
    
    

data3 = pd.DataFrame(data=[((dub)*0).dt.total_seconds(), dub1, dub2]).transpose()
data3.columns = ['Time Delta (s)', 'Driver', 'Lap Number']
  

Delta_file.append(data3)



fig, ax = plt.subplots(figsize=(18, 18))



for j in Delta_file:
    abb = j['Driver'].iloc[0]

    sns.lineplot(data=j,
                    x ="Lap Number",
                    y ="Time Delta (s)",
                    ax=ax,
                    
                    color=fastf1.plotting.driver_color(abb),
                    
                    legend='full')
start, end = ax.get_xlim()
start1, end1 = ax.get_ylim()

ax.xaxis.set_major_locator(MaxNLocator(integer=True))


plt.title((f"Gap To Leader \n"
             f"{race.event['EventName']} {race.event.year} Race"))

plt.grid()


xpos = [19,33,34] 
no = len(xpos)

text = "Verstappen Pits" 

for i in xpos:
    

    plt.vlines(x=i, ymin=start1, ymax=end1, color = 'white', linestyles="dashed")
    plt.text(x=i-1, y=60, s=text, ha='center', va='center',rotation='vertical')

plt.axis([start, end, start1, end1])

plt.gca().invert_yaxis()






plt.show() 