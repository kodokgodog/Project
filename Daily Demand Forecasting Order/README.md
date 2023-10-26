# Order Forcasting

## Background
In today's dynamic business environment, accurate daily demand forecasting for order prediction is a pivotal factor in optimizing supply chain efficiency and customer satisfaction. This project seeks to develop a data science model for precise daily demand forecasting order prediction in the Industry.

The project aims to enhance order fulfillment, reduce inventory costs, and improve customer satisfaction by developing a robust model. We will collect and preprocess historical order data, employ advanced forecasting techniques, and integrate the model into the supply chain system. The ultimate goal is to provide accurate, real-time demand predictions, enabling better decision-making and positioning our organization as a leader in efficient supply chain management.

## Objective
Developing a prediction model that can be used effectively and got a high accuracy on the prediction to be used on the daily demand forecasting.

## Data Description
The data that are used are data consisted of number of all type of Order and the Target number of order per day.

## Model Evaluation
The model that are used on this modelling is Linear Regression model with the evaluation metrics MAPE. 

## Conclusion
* The dataset only consisting of 60 line and 13 feature
* There are 21 line of data that got missing value
* There are 4 variabel or feature that got really strong correlation to the data target ( Total orders), the feature are Non-urgent order (0.97), Order type C (0.86), Order type B (0.8), and Urgent order (0.74). 
* The dataset considered small so a syntetic data are needed on the modelling to avoid the risk of overfitting.
* Iterative Imputer is the final model that are used on the modelling based on the RMSE value, eventhough the value difference is not really significant.
* Looking at the score of the MAPE from the model, the model is fit because of the difference between the train and test of the data is not significant with the value of MAPE on the model is about 5.7%.
* The model got a good score both on MSE and R2 on the training and test data. An R-squared value approaching 1 (in this case, very close to 1) indicates that your model is capable of explaining nearly all of the variation in the target data. On the other hand, a low Mean Squared Error (MSE) indicates that the difference between the model's predictions and the actual data is very small.
