import numpy as np
import math
import pandas as pd

data_frame = pd.read_csv('kc_house_train_data.csv')

print type(data_frame['bedrooms'])
bedrooms = data_frame['bedrooms']
#data_frame['sq'] = data_frame['bedrooms'] * data_frame['view']
#print data_frame['sq']

def getIntercept(input_feature,output):

    return data_frame[output].mean() - getSlope(input_feature, output) * data_frame[input_feature].mean()

#gives the slope of the line we are fitting
def getSlope(input_feature,output):
    XY_datapoints = []
    data_frame['XY'] = data_frame[input_feature] * data_frame[output]
    data_frame['X_2'] = data_frame[input_feature] ** 2

    #for i in range(0,len(X_datapoints)):
    #    XY_datapoints.append(X_datapoints[i]*Y_datapoints[i])

    Mean_X = data_frame[input_feature].mean()
    Mean_Y = data_frame[output].mean()
    Mean_XY = data_frame['XY'].mean()
    Mean_XSquare = data_frame['X_2'].mean()


    Numerator = Mean_XY - (Mean_X * Mean_Y)
    Denominator = Mean_XSquare - (Mean_X * Mean_X)

    return Numerator/Denominator

def simpleLinearRegression(input_feature,output):
    pass

#print getSlope(X_datapoints,Y_datapoints)
#print getIntercept(X_datapoints,Y_datapoints)

#Give the required input x value here
#getEstimatedOutput(input_value)


#funtionality for reading data from the files to be added

