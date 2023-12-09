# Imports
import re
import json
import csv

# Acess vocab scoring json
file_path = "data/Sentence Scorer Data/filtered_final.json"
with open(file_path, 'r') as fp:
    score_dict = json.load(fp)
    
# Access verb text file
file_path = "data/Cooking words/cooking_verbs.txt"
f = open(file_path, "r")
cooking_verbs = f.read()
    
# Acess noun text file
file_path = "data/Cooking words/cooking_nouns.txt"
f = open(file_path, "r")
cooking_nouns = f.read()

# Access unclean text file
file_path = "data/unclean_data.txt"
f = open(file_path, "r")
output = f.read()
data = re.split('[.!?]', output.lower())
if "" in data:
    data.remove("")

# Data cleaning
def remove_unknown_chars(string):
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    return ''.join(c for c in string if c in allowed_chars)

for i, sentence in enumerate(data):
    new_sentence = sentence.replace('\n', '').replace(',', '').strip()
    data[i] = new_sentence.split(" ")
    for k in range(len(data[i])):
        data[i][k] = remove_unknown_chars(data[i][k])
    if "" in data[i]:
        data[i].remove("")
    
# Scorer
# We want to generate a score for each sentence for now
res_dict = {}
for sentence_list in data:
    total_words = len(sentence_list)
    current_score = 0
    completed_sentence = " ".join(sentence_list)

    for word in sentence_list:
        word_score = 0
        if score_dict.get(word) is not None:
            word_score = score_dict[word]
        else:
            word_score = 1
            
        if (word in cooking_verbs):
            word_score *= 2
        # if (word in cooking_nouns):
        #     word_score *= 1.5
        current_score += word_score
            
    # print(current_score)
    score_avg = current_score / total_words
    if (score_avg > 15):
        res = True
    else:
        res = False
    res_dict[completed_sentence] = res
    
# Write results to csv
# I want to make sure to write to a staging file first to make sure that the information is correct
file_path = "data/binary_class_sentences-stage.csv"
with open(file_path, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for key, value in res_dict.items():
        writer.writerow([key, value])
    
# Want to make sure to delete everything from the unclean.txt file
# Access unclean text file
file_path = "data/unclean_data.txt"
with open(file_path, 'w') as file:
    for item in cooking_nouns:
        file.write("")