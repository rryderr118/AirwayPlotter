'''
Created on Nov 19, 2020

@author: Ryder
'''
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import pandas as pd
import numpy as np

class Plotter:
    def __init__(self):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.root.configure(bg = 'black')
        self.frame.configure(bg = 'black')
        tk.Grid.columnconfigure(self.root, 0, weight=1)
        tk.Grid.columnconfigure(self.root, 1, weight=1)
        tk.Grid.columnconfigure(self.root, 2, weight=1)
        tk.Grid.rowconfigure(self.root, 1, weight=1)
    
    def plotAirportData(self):
        df = pd.read_csv('airports.csv')
        x = df['longitude_deg']
        y = df['latitude_deg']
        figure, ax = plt.subplots(figsize=(8, 6))
        plt.xticks(range(-100,100))
        plt.yticks(range(-180,180))
        ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
        
        figure.set_facecolor('black')
        ax.set_facecolor('black')
        plt.ylabel('Longitude', color='white')
        plt.xlabel('Latitude', color='white')
        plt.grid(linestyle='--', color='grey')
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.xaxis.label.set_color('white')
        ax.tick_params(colors='white')
        
        ax.plot(x,y,color='white',linestyle=' ', marker='o')
        figure.autofmt_xdate()
        figure.suptitle('Airports', color='white')
        canvas = FigureCanvasTkAgg(figure, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=1, rowspan=7, sticky='ns')    
        
    def plotRunwayData(self):
        df = pd.read_csv('runways_errors_removed.csv')
        x1 = df['le_longitude_deg']
        x2 = df['he_longitude_deg']
        y1 = df['le_latitude_deg']
        y2 = df['he_latitude_deg']
        x = np.array(x1)
        y = np.array(y1)
        
        #plotting the midpoint of the runway using the start point and end point
        for index in range(0,len(x1)):
            x[index] = (x1[index]+(x1[index]-x2[index])/2)
            y[index] = (y1[index]+(y1[index]-y2[index])/2)
            if x[index] < -180 or x[index] > 180:
                print(df['id'][index])
                print(x1[index], x2[index], x1[index]+(x1[index]-x2[index]))
        figure, ax = plt.subplots(figsize=(8, 6))
        plt.xticks(range(-100,100))
        plt.yticks(range(-180,180))
        ax.xaxis.set_major_locator(ticker.MultipleLocator(20))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
        
        figure.set_facecolor('black')
        ax.set_facecolor('black')
        plt.ylabel('Longitude', color='white')
        plt.xlabel('Latitude', color='white')
        plt.grid(linestyle='--', color='grey')
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.xaxis.label.set_color('white')
        ax.tick_params(colors='white')
        
        ax.plot(x,y,color='white',linestyle=' ', marker='o')
        figure.autofmt_xdate()
        figure.suptitle('Runways', color='white')
        canvas = FigureCanvasTkAgg(figure, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=2, rowspan=7, sticky='ns')

plot = Plotter()
plot.plotAirportData()
plot.plotRunwayData()
plot.root.mainloop()

'''    
'''
