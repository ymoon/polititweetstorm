# polititweetstorm
EECS 498 W16 Final Project
Welcome to the world of #polititweetstorm.
We are (Team Members):
	- Danielle Livneh
	- John Moon
	- Aren Vogel
	- Mathew Wiesman
Students of Professor Mihalacea's Information Retrieval Class. 
Our goal with #polititweetstorm was to create a real time web application to display the sentiment of trending political topics in a given location.
Learn more about the goal and process in detail from our paper.

Setting up:
1) Navigate to the main polititweetstorm directory
2) run: pip install -r requirements.txt
	This should install all APIs and Modules necessary to run the project

To run training:
1) Naivgate to the classifier directory
2) type: python training.py
	The output will be stored in training_information.json
3) You now have json formatted data storing a dictionary that represents a trained Naive Bayes Classifier

To run the website and sentiment analysis system:
1) Navigate to the main polititweetstorm directory
2) run: python app.py
3) Open your preffered browser and navigate to 0.0.0.0:3000/polititweetstorm/
4) Click get started to get started
5) Enjoy

