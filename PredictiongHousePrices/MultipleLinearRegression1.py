import pandas as pd
import numpy as np
import math


#print math.log(1180)
training_data_frame = pd.read_csv('kc_house_train_data.csv')
testing_data_frame = pd.read_csv('kc_house_test_data.csv')

log_func = lambda x: math.log(x)
training_data_frame['bedrooms_squared'] = training_data_frame['bedrooms'] ** 2
training_data_frame['bed_bath_rooms'] = training_data_frame['bedrooms'] * training_data_frame['bathrooms']
training_data_frame['log_sqft_living'] = training_data_frame['sqft_living'].apply(log_func)
training_data_frame['lat_plus_long'] = training_data_frame['lat'] + training_data_frame['long']

testing_data_frame['bedrooms_squared'] = testing_data_frame['bedrooms'] ** 2
testing_data_frame['bed_bath_rooms'] = testing_data_frame['bedrooms'] * testing_data_frame['bathrooms']
testing_data_frame['log_sqft_living'] = testing_data_frame['sqft_living'].apply(log_func)
testing_data_frame['lat_plus_long'] = testing_data_frame['lat'] + testing_data_frame['long']

#Q1
print testing_data_frame['bedrooms_squared'].mean(),testing_data_frame['bed_bath_rooms'].mean(),testing_data_frame['log_sqft_living'].mean(),testing_data_frame['lat_plus_long'].mean()

Model_1 = ['sqft_living', 'bedrooms', 'bathrooms', 'lat','long']
Model_2 = [ 'sqft_living', 'bedrooms', 'bathrooms', 'lat','long','bed_bath_rooms']
Model_3 = ['sqft_living', 'bedrooms', 'bathrooms', 'lat','long', 'bed_bath_rooms', 'bedrooms_squared', 'log_sqft_living', 'lat_plus_long']

Model_1_X = np.array(training_data_frame[Model_1])
Model_2_X = np.array(training_data_frame[Model_2])
Model_3_X = np.array(training_data_frame[Model_3])

a = np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6]])
#print a.shape
b = np.array([[1],[1],[1]])
#print b.shape

#print Model_1_X.shape
#print np.ones((len(a),1)).shape
#print np.hstack((a,b))
#print Model_1_A.shape
Model_1_A = np.hstack((Model_1_X, np.ones((len(Model_1_X),1))))
target = np.array(training_data_frame['price'])
output = np.linalg.lstsq(Model_1_A, target)
print output[0]
#print target.shape
#print Model_1_A[0]
Model_2_A = np.hstack((Model_2_X, np.ones((len(Model_2_X),1))))
target = np.array(training_data_frame['price'])
output = np.linalg.lstsq(Model_2_A, target)
print output[0]


