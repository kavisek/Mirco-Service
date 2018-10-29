# Predictive Models as Restful APIs

This report contains templates Flask Restful APIs that accept data from an external source, and feedback the models predictions back. Theses "models as  micro services" are configured for the iris dataset. Please feel free to modify the code to your datasets. I have written comment within the code for each section. If you want this model to run in your local environment, pleas take a look the following instruction. All the code in this repo is PEP8 compliant.



### Instruction

These instruction are currently based on the Simple Flask Restful API found in the "Supervised Model API" Subdirectory. All other Subdirectories relate to additional micro services that I am currently working on.

<br>
<center>![img](https://cdn-images-1.medium.com/max/1600/1*9oK18ZPQX75ophT4s6Ee6A.png)</center>
<br>

1. Create a virtual environment

Type the following command in your terminal to create a virtual environment in conda.

`conda create -name micro_service`

Then activate and enter the environment

`source activate micro_service`

2. Install the packages we to run the flask app.

<br>`conda install -c anaconda flask ` <br>
<br>`conda install -c conda-forge flask-restful ` <br>
<br>`conda install -c conda-forge flask-httpauth ` <br>
<br>`conda install -c anaconda scikit-learn ` <br>

3. Download to clone this repo to your local machine
4. Run the `model_app.py` in terminal

`python model_app.py`

5. The model API should be running now.
6. Open up another terminal window and run the following commands to test the API


View all Prediction: `curl -u kavi:python -i http://localhost:5000/todo/api/v1.0/tasks`

View the Second Prediction in the API:  `curl -i http://localhost:5000/todo/api/v1.0/tasks/2`

Ask for a Predictin from the API:

`curl -u kavi:python -i -H "Content-Type: application/json" -X POST -d '{"sepal length (cm)":"7.1","sepal width (cm)": "3.0","petal length (cm)": "5.9","petal width (cm)": "2.1"}' http://localhost:5000/todo/api/v1.0/tasks`

Update a Prediction:

 `curl -u kavi:python -i -H "Content-Type: application/json" -X PUT -d '{"sepal length (cm)":"6.1","sepal width (cm)": "2.0","petal length (cm)": "4.8","petal width (cm)": "1.0"}' http://localhost:5000/todo/api/v1.0/tasks/2`
