## Simple Linear Regression Y = mX + c form

import numpy as np
import math
import pandas as pd

training_data_frame = pd.read_csv('kc_house_train_data.csv')
testing_data_frame = pd.read_csv('kc_house_test_data.csv')

#print type(training_data_frame['bedrooms'])
bedrooms = training_data_frame['bedrooms']
#data_frame['sq'] = data_frame['bedrooms'] * data_frame['view']
#print data_frame['sq']

def getIntercept(input_feature,output):
     """
     returns the intercept
     :param input_feature: the input feature selected
     :param output: target feature
     :return:
     """
     training_data_frame[output].mean() - getSlope(input_feature, output) * training_data_frame[input_feature].mean()

def getSlope(input_feature,output):
    """
    returns the slope of the line we are trying to fit
    :param input_feature: the input featuer selected
    :param output: target feature
    :return:
    """
    training_data_frame['XY'] = training_data_frame[input_feature] * training_data_frame[output]
    training_data_frame['X_2'] = training_data_frame[input_feature] ** 2

    Mean_X = training_data_frame[input_feature].mean()
    Mean_Y = training_data_frame[output].mean()
    Mean_XY = training_data_frame['XY'].mean()
    Mean_XSquare = training_data_frame['X_2'].mean()

    Numerator = Mean_XY - (Mean_X * Mean_Y)
    Denominator = Mean_XSquare - (Mean_X * Mean_X)

    return Numerator/Denominator

def simpleLinearRegression(input_feature,output):
    return (getIntercept(input_feature,output), getSlope(input_feature,output))

def get_regression_predictions(input_feature, intercept, slope):
    """
    adds a new column into training data frame which contains values of predictions for
    the given input feature
    """
    training_data_frame['predictions'] = training_data_frame[input_feature] * slope + intercept

def get_residual_sum_of_squares(input_feature, output, intercept,slope):
    """
    returns the residual sum of squares error
    """
    get_regression_predictions(input_feature,intercept,slope)
    training_data_frame['rss'] = (training_data_frame['predictions'] - training_data_frame[output]) ** 2
    return training_data_frame['rss'].sum()

def get_regression_predictions_test(input_feature, intercept, slope):
    testing_data_frame['predictions'] = testing_data_frame[input_feature] * slope + intercept

def get_residual_sum_of_squares_test(input_feature, output, intercept,slope):
    get_regression_predictions_test(input_feature,intercept,slope)
    testing_data_frame['rss'] = (testing_data_frame['predictions'] - testing_data_frame[output]) ** 2
    return testing_data_frame['rss'].sum()

def inverse_regression_predictions(output, intercept, slope):
    """
    adds a new column into training data frame which contains values of predictions of input_feature
    from the obtained slope and intercept
    """
    training_data_frame['predict_X'] = (training_data_frame[output] - intercept) / slope

##Model1
input_feature = 'sqft_living'
output = 'price'
sqft_intercept,sqft_slope = simpleLinearRegression('sqft_living','price')
get_regression_predictions(input_feature,sqft_intercept,sqft_slope)
req_values = training_data_frame[training_data_frame[input_feature] ==  2650]
#Q1 printing predictions for house with sqft_living = 2650
print req_values['predictions']

#Q2 - getting the value of rss
print get_residual_sum_of_squares(input_feature,output,sqft_intercept,sqft_slope)

#Q3 - calculating the prediction of input values from output values
inverse_regression_predictions(output,sqft_intercept,sqft_slope)
print training_data_frame[training_data_frame['price'] == 800000]

#Q4 - getting the difference of rss error on test data set between the two models

##Model 2
bedroom_intercept,bedroom_slope = simpleLinearRegression('bedrooms','price')
print get_residual_sum_of_squares_test(input_feature,output,sqft_intercept,sqft_slope)
print get_residual_sum_of_squares_test('bedrooms', 'price', bedroom_intercept, bedroom_slope)
#test_model = simpleLinearRegression('sqft_living','price')
