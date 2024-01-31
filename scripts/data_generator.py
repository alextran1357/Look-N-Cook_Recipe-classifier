# Imports
import re
import json
import csv

# Access unclean text file FALSE
file_path = "../data/unclean_data-FALSE.txt"
f = open(file_path, "r", encoding="utf-8")
output = f.read()
false_data = re.split('[.!?]', output.lower())
if "" in false_data:
    false_data.remove("")
    
# Access unclean text file TRUE
file_path = "../data/unclean_data-TRUE.txt"
f = open(file_path, "r", encoding="utf-8")
output = f.read()
true_data = re.split('[.!?]', output.lower())
if "" in true_data:
    true_data.remove("")

# Data cleaning
def remove_unknown_chars(string):
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789()/- ")
    return ''.join(c for c in string if c in allowed_chars)
def remove_single_word_sentences(sentence):
    word_list = sentence.split()
    if len(word_list) <= 2:
        return ""
    return sentence

for i, sentence in enumerate(true_data):
    true_data[i] = sentence.replace('\n', '').strip()
    # true_data[i] = remove_unknown_chars(true_data[i])
    true_data[i] = remove_single_word_sentences(true_data[i])
    if true_data[i] == "":
        true_data.remove("")

for i, sentence in enumerate(false_data):
    false_data[i] = sentence.replace('\n', '').strip()
    # false_data[i] = remove_unknown_chars(false_data[i])
    false_data[i] = remove_single_word_sentences(false_data[i])
    if false_data[i] == "":
        false_data.remove("")
        
false_dict = {}
true_dict = {}
for sentence in true_data:
    true_dict[sentence] = True
for sentence in false_data:
    false_dict[sentence] = False

# Write results to csv
# I want to make sure to write to a staging file first to make sure that the information is correct
file_path = "../data/binary_class_sentences-stage.csv"
with open(file_path, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for key, value in false_dict.items():
        writer.writerow([key, value])
    for key, value in true_dict.items():
        writer.writerow([key, value])
        
        
# Empty out unclean data text files
file_path = "../data/unclean_data-FALSE.txt"
with open(file_path, 'w') as file:
    pass
file_path = "../data/unclean_data-TRUE.txt"
with open(file_path, 'w') as file:
    pass