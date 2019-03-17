import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
from matplotlib import style

df = pd.read_csv("BARC.L.csv")
#print(df.head())

prices = df['Close'].tolist()
dates = df.index.tolist()


#Convert to 1d Vector
dates = np.reshape(dates, (len(dates), 1))
prices = np.reshape(prices, (len(prices), 1))



#Define Linear Regressor Object
regressor = LinearRegression()
regressor.fit(dates, prices)

'''
#Visualize Results
plt.scatter(dates, prices, color='yellow', label= 'Actual Price') #plotting the initial datapoints
plt.plot(dates, regressor.predict(dates), color='red', linewidth=3, label = 'Predicted Price') #plotting the line made by linear regression
plt.title('Linear Regression | Time vs. Price')
plt.legend()
plt.xlabel('Date Integer')
plt.show()
'''

#Predict Price on Given Date
date = np.array(10)
date = date.reshape(-1,1)
predicted_price =regressor.predict(date)
print(predicted_price[0][0])
#regressor.coef_[0][0] ,regressor.intercept_[0]