import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error 
import warnings 

warnings.filterwarnings('ignore')

training_data = pd.read_csv("final.csv")
training_data_x = training_data[['Day','Hour','Activity']]
training_data_y = training_data[['Duration']]

testing_data = pd.read_csv("final_test.csv")
testing_data_x = testing_data[['Day','Hour','Activity']]
testing_data_y = testing_data[['Duration']]

model = DecisionTreeRegressor(random_state = 0)  

model.fit(training_data_x,training_data_y)

predicted_duration = model.predict(testing_data_x)

MAE = mean_absolute_error(testing_data_y , predicted_duration)

print('Decision Tree validation Mean Absolute Error = ')
print(MAE)
