import enchant

file_name = "Data/Final/vocab_list_py.txt"
file = open(file_name, "r")
data = file.readlines()

'''
This block of code takes an existing data file and converting
everything to a dictionary
'''
strip_data = []
data_alone = []
data_dic = {}
for i in data:
    strip_data.append(i.strip())
for i in range (len(strip_data)):
    temp = strip_data[i]
    temp = temp.split(" ")
    data_alone.append(temp[0])
    data_dic[temp[0]] = int(temp[1])
del strip_data
file.close()

'''
Finds all the words that do not mean anything
'''
cooking_verbs = []
not_words = []
d = enchant.Dict("en_US")
for words in data_alone:
    if (d.check(words) == False):
        not_words.append(words)

filler_words = ['a','an','the','i','you','he','she','it','they','me','you','him',
        'her','it','my','mine','your','yours','his','her','hers','its','who','whom','whose','what',
        'which','another','each','everything','nobody','either','someone','who','whom','whose',
        'that','which','myself','yourself','himself','herself','itself','this','that']

'''
Inputs all the words back into the list if it does not contain in not_words list
'''
file_name = "Data/Final/filtered_test.txt"
file = open(file_name, "w")
for data in data_dic:
    if (data not in not_words and data not in filler_words and int(data_dic[data]) > 2):
        temp = data + " " + str(data_dic[data]) + "\n"
        file.write(temp)
        
file.close()





