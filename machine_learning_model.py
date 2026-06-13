#we are making simple and easy machine learning model using linear regression
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#we are creating a dataset for our machine learning model
np.random.seed(0)
heights=np.random.normal(170, 10, 100) #we are creating a dataset of heights of 100 people with mean 170 and standard deviation 10
weights=heights*0.5 + np.random.normal(0, 5, 100) #we are creating a dataset of weights of 100 people with mean 0 and standard deviation 5

#we are splitting our dataset into training and testing sets
X= heights.reshape(-1, 1) #we are reshaping our dataset to make it suitable for our machine learning model
y= weights
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) #we are splitting our dataset into training and testing sets with 80% training and 20% testing
#we are creating our machine learning model using linear regression
model= LinearRegression() #we are creating an instance of our machine learning model
model.fit(X_train, y_train) #we are fitting our machine learning model to our training data
#we are making predictions using our machine learning model
y_pred= model.predict(X_test) #we are making predictions using our machine learning model on our testing data
#evaluating our machine learning model
from sklearn.metrics import mean_squared_error, r2_score
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
#we are visualizing our machine learning model
sorted_index = X_test.flatten().argsort()
plt.scatter(X_test, y_test, color='blue', label='Data Points')
plt.plot(X_test[sorted_index], y_pred[sorted_index], color='red', label='Regression Line')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Height vs Weight')
plt.legend()
plt.show()