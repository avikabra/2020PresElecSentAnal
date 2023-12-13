import requests
from bs4 import BeautifulSoup
import string
from nrclex import NRCLex

tags = ["joy", "trust", "fear", "surprise", "sadness", "disgust", "anger", "anticipation"]

import os
# Get the list of all files in the specified folder
files = os.listdir("final_data")

# Print the list of files
print("List of files in the folder:")
for file in files:
    print(file)

data = {
    "Trump": {},
    "Biden": {}
}

for i in range(len(files)):

    file_path = "final_data/" + files[i]

    file_contents = ""

    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    emotion = NRCLex(file_contents)
    emotion_scores = emotion.raw_emotion_scores
    #print (emotion_scores)
    
    if (files[i].__contains__("trump")):
        data["Trump"][i] = emotion_scores
    else:
        data["Biden"][i] = emotion_scores

#print(data)

""" First Analysis Parameter: Frequency and Normalisation """

# find the maximum three emotions
trump_data = data["Trump"]

trump_totals = {

}

for i in range(len(tags)):
    trump_totals[tags[i]] = 0

for key in trump_data.keys():
    for i in range(len(tags)):
        try:
            trump_totals[tags[i]] += trump_data[key][tags[i]]
        except:
            trump_totals[tags[i]] += 0

print("Trump: " + str(trump_totals))


biden_data = data["Biden"]

biden_totals = {

}

for i in range(len(tags)):
    biden_totals[tags[i]] = 0

for key in biden_data.keys():
    for i in range(len(tags)):
        try:
            biden_totals[tags[i]] += biden_data[key][tags[i]]
        except:
            biden_totals[tags[i]] += 0

print("Biden: " + str(biden_totals))

import matplotlib.pyplot as plt
# from pyplutchik import plutchik
# plutchik(emotions)

import pandas as pd

# Create the data
b_d = []
t_d = []
for key in trump_totals.keys():
    b_d.append(biden_totals[key])
    t_d.append(trump_totals[key])

t_max = max(t_d) 
b_max = max(b_d)

for i in range(len(t_d)):
    t_d[i] /= t_max
    b_d[i] /= b_max

data = {'A': tags, 'Trump': t_d, 'Biden': b_d}

# Create the DataFrame
df = pd.DataFrame(data)

# Create the plot
ax = df.plot.bar(x='A', y=['Trump','Biden'], color=["red", "blue"])

# Add labels and title
ax.set_xlabel('Candidate')
ax.set_ylabel('Standardised Value')
ax.set_xticklabels(tags, rotation=45)

# Show the plot
plt.show()
            
