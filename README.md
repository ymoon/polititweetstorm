----------------------
POLITITWEETSTORM
----------------------
EECS 498-1 (486) W16 Final Project
Welcome to the world of #polititweetstorm.
We are (Team Members):
```
	- Danielle Livneh
	- John Moon
	- Aren Vogel
	- Mathew Wiesman
```
Students of Professor Mihalacea's Information Retrieval Class at the University of Michigan. 
Our goal with #polititweetstorm was to create a real time web application to display the sentiment of trending political topics in a given location.
Learn more about the goal and process in detail from our paper.

----------------------
SETTING UP
----------------------
1. Navigate to the main polititweetstorm directory
2. run: pip install -r requirements.txt
	This should install all APIs and Modules necessary to run the project

----------------------
TRAINING YOUR SYSTEM
----------------------
To run training:
```
1. Naivgate to the classifier directory
2. Unzip sad.csv.zip which is your training dataset
3. run: python training.py
	The output will be stored in training_information.json
4. You now have json formatted data storing a dictionary that represents a trained Naive Bayes Classifier
```

----------------------
LAUNCH THE WEB APPLICATION
----------------------
To run the website and sentiment analysis system:
```
1. Navigate to the main polititweetstorm directory
2. run: python app.py
3. Open your preffered browser and navigate to 0.0.0.0:3000/polititweetstorm/
4. Click get started to get started
5. Enjoy
```

----------------------
TESTING YOUR SYSTEM
----------------------
To test the classifer:
```
1. Navigate to the classifier directory
2. Unzip sad.csv.zip which is your training dataset
3. Run: train_1000.py || train_10000.py depending on which training you wish to run
	•The output will be stored in training_information1000.json and training_information10000.py respectively
	•These programs also prints to console the number of tweets processed as it runs
4. You now have json formatted data storing a dictionary that represents a trained Naive Bayes Classifier for a portion of the oringal dataset
5. Run: run_1000.py || run_10000.py depending on which training program you ran
	•Output: (#of correctly classified tweets, total tweets classified)
```



