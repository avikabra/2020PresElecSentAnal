import requests
from bs4 import BeautifulSoup
import string
from nrclex import NRCLex

tags = ["joy", "trust", "fear", "surprise", "sadness", "disgust", "anger", "anticipation", "positive", "negative"]

buzzwords = [
    "Implement", "Reform", "Prioritize", "Enhance", "Strengthen", "Revitalize",
    "Modernize", "Streamline", "Invest", "Boost", "Expand", "Develop", "Advance",
    "Promote", "Propel", "Facilitate", "Improve", "Upgrade", "Secure", "Revamp",
    "Innovate", "Foster", "Accelerate", "Tackle", "Address", "Champion", "Execute",
    "Policy", "Legislation", "Reform", "Act", "Initiative", "Strategy", "Framework",
    "Regulation", "Implementation", "Adjustment", "Compliance", "Guidelines",
    "Procedure", "Statute", "Mandate", "Provisions", "Amendment", "Revision", "Legal",
    "Jurisdiction", "Governance", "Code", "Standard", "Oversight", "Compliance",
    "Enforcement", "Resolution", "Accord", "Charter", "Constitutional",
    "Education", "Healthcare", "Jobs", "Economy", "Infrastructure", "Security",
    "Immigration", "Equality", "Justice", "Environment", "Innovation", "Reform",
    "Leadership", "Climate", "Opportunity", "Technology", "Prosperity", "Diversity",
    "Housing", "Sustainability", "Diplomacy", "Veterans", "Trade", "Regulation",
    "Safety", "Defense", "Energy", "Democracy", "Unity", "Resilience",
    "Education", "Economy", "Security", "Healthcare", "Education", "Reform", "Act",
    "Initiative", "Strategy", "Framework", "Regulation", "Implementation", "Adjustment",
    "Compliance", "Guidelines", "Procedure", "Statute", "Mandate", "Provisions",
    "Amendment", "Revision", "Legal", "Jurisdiction", "Governance", "Code", "Standard",
    "Oversight", "Compliance", "Enforcement", "Resolution", "Accord", "Charter", "Constitutional"
]

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

buzzword_data = {
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

    split_text = file_contents.split(".")

    temporal_emotion = []

    buzzword_count = []

    for section in split_text:
        emotion=NRCLex(section)
        emotion_scores = emotion.raw_emotion_scores

        #print(emotion_scores)

        if temporal_emotion == []:
            temporal_emotion.append(emotion_scores)
        else:
            data_to_add = temporal_emotion[-1]
            new_data = {}
            for key in tags:
                try:
                    try:
                        temp = emotion_scores[key]
                    except: 
                        emotion_scores[key] = 0
                    
                    new_data[key] = data_to_add[key] + emotion_scores[key]
                except:
                    new_data[key] = emotion_scores[key]

            temporal_emotion.append(new_data)

        words = section.split(" ")
        section_bwords = 0
        for word in words:
            if word in buzzwords:
                section_bwords += 1
        if len(buzzword_count) == 0:
            buzzword_count.append(section_bwords)
        else:
            buzzword_count.append(buzzword_count[-1] + section_bwords)
    
    if (files[i].__contains__("trump")):
        data["Trump"][i] = temporal_emotion
        buzzword_data["Trump"][i] = buzzword_count
    else:
        data["Biden"][i] = temporal_emotion
        buzzword_data["Biden"][i] = buzzword_count

#print(data)

print(buzzword_data)

# graph 1

"""print(data["Biden"].keys())
b_data = data["Biden"][6] 

y_axis_pos = []
y_axis_neg = []
for i in range(len(b_data)):
    try:
        y_axis_pos.append(b_data[i]["positive"])
    except:
        y_axis_pos.append(0)
    
    try:
        y_axis_neg.append(b_data[i]["negative"])
    except:
        y_axis_neg.append(0)

#print(y_axis_neg)
#print(y_axis_pos)

import matplotlib.pyplot as plt
import pandas as pd

data = {'A': [i+1 for i in range(len(y_axis_neg))], 'Positive': y_axis_pos, 'Negative': y_axis_neg}

# Create the DataFrame
df = pd.DataFrame(data)

# Create the plot
ax = df.plot.line(x='A', y=['Positive','Negative'], color=["green", "red"])

# Add labels and title
ax.set_xlabel('Biden')
ax.set_ylabel('Frequency')

# Show the plot
plt.show()"""

# Graph 2 

#b_data = buzzword_data["Biden"][2] 
b_data = buzzword_data["Trump"][1]

y_axis_bz = b_data

y_axis_emotion = []
b_emotion_data = data["Trump"][1]
for i in range(len(y_axis_bz)):
    total_emotion = 0
    for tag in b_emotion_data[i].keys():
        total_emotion += b_emotion_data[i][tag]
    y_axis_emotion.append(total_emotion)

print(y_axis_emotion)

#print(y_axis_neg)
#print(y_axis_pos)

import matplotlib.pyplot as plt
import pandas as pd

data = {'A': [i+1 for i in range(len(y_axis_bz))], 'Buzzword': y_axis_bz, 'Emotion': y_axis_emotion}

# Create the DataFrame
df = pd.DataFrame(data)

# Create the plot
ax = df.plot.line(x='A', y=['Buzzword','Emotion'], color=["blue", "black"])

# Add labels and title
ax.set_xlabel('Trump')
ax.set_ylabel('Frequency')
plt.yscale('log')

# Show the plot
plt.show()