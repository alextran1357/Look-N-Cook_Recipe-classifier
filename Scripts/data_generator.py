# Imports
import re
import json

# Acess vocab scoring json
file_name = "data/Sentence Scorer Data/filtered_final.json"
with open(file_name, 'r') as fp:
    score_dict = json.load(fp)
    
# Access verb text file
file_name = "data/Cooking words/cooking_verbs.txt"
f = open(file_name, "r")
cooking_verbs = f.read()
    
# Acess noun text file
file_name = "data/Cooking words/cooking_nouns.txt"
f = open(file_name, "r")
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

test_dict = {}

for sentence_list in data:
    total_words = len(sentence_list)
    current_score = 0
    completed_sentence = " ".join(sentence_list)

    for word in sentence_list:
        print(word)
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
    test_dict[completed_sentence] = score_avg        

# Acess noun text file for write
file_name = "data/test_file.txt"
with open(file_name, 'w') as file:
    for key in test_dict:
        file.write("%s : %s\n" % (key, test_dict[key]))

# if (score > 20):
#     print("YES")
# else:
#     print("NO")
    
# Want to make sure to delete everything from the unclean.txt file