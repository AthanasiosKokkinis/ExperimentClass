import matplotlib.pyplot as plt
import numpy as np
import json

class Experiment:
    
    def __init__(self, label):
        self.label = label
        self.data = {}
        self.i = 0
        
    def add_data(self, key, data_values):
        if(key in self.data):
            self.data[key].extend(data_values)
        else:
            self.data[key] = data_values
    def plot(self,xlabel,ylabel,handle = ""):
        x = self.data[xlabel]
        y = self.data[ylabel]
        plt.plot(x,y,label=handle)
        plt.scatter(x,y)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(self.label)
        plt.grid()
        plt.legend()
        plt.show()

    def mean(self,key):
        return np.mean(self.data[key])

    def deviation(self,key):
        return np.sigma(self.data[key])

    def find_value(self,key,value):
        for self.i in range(self.i, len(self.data[key])):
            self.i = self.i + 1
            if(self.data[key][self.i - 1]==value):
                #print(self.i - 1)
                return self.i - 1 
            
        self.i = 0
        return -1

    def one_dimensional_data_from_file(self,key,filename,delimiters):
        file = open(filename,"r")
        data = file.read().replace('\0','')
        data_lines = data.split(delimiters)
        for data in data_lines:
            self.data[key].append(data)

    def save_experiment_to_file(self,filename):
        file = open(filename,"w")
        file.write(self.label)
        keys = self.data.keys()
        for key in keys:
            file.write("#")
            file.write(key)
            file.write(json.dumps(self.data[key]))
        file.close()

        
    def load_experiment_from_file(self,filename):
        file = open(filename,"r")
        data = file.read().split("#")
        print(data)
        self.label = data[0]
        print(self.label)
        for item in data[1:len(data)]:
            item = item.replace("["," ").replace("]"," ")
            #print(item)
            key = item.split(" ")[0]
            print(key)
            data = item[1:-1].replace(" ","").split(",")
            if (key in self.data):
                self.data[key].extend(data)
                print(self.data[key])
            else:
                self.data[key] = data

        


