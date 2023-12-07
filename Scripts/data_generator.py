# Imports
import re
import json

# Access unclean data
file_path = "../data/unclean_data.txt"
f = open(file_path, "r")

output = f.read()

test = re.split('[.!?]', output.lower())
test.remove("")

# Acess vocab scoring json
file_name = "../data/Sentence Scorer Data/filtered_final.json"
with open(file_name, 'r') as fp:
    score_dict = json.load(fp)


# '''
# Scorer
# '''
# # Generate an average score for the paragraph
# total_words = len(paragraph_list)
# current_score = 0
# for word in paragraph_list:
#     word_score = 0
#     if (word in master_data_dic):
#         word_score = int(master_data_dic[word])
#     else:
#         word_score = 1
#     if (word in verb_list):
#         word_score = word_score * 2
#     if (word in noun_list):
#         word_score = word_score * 1.5
#     current_score += word_score
  
# score = current_score / total_words
# print(score)        

# if (score > 20):
#     print("YES")
# else:
#     print("NO")