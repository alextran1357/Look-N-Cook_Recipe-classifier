import os, re, string

file_name = "Data/vocab_list_py.txt"
file = open(file_name, "r")
data = file.readlines()

'''
This block of code takes an existing data file and converting
everything to a dictionary
'''
strip_data = []
data_dic = {}
for i in data:
    strip_data.append(i.strip())
for i in range (len(strip_data)):
    temp = strip_data[i]
    temp = temp.split(" ")
    data_dic[temp[0]] = int(temp[1])
del strip_data
file.close()

'''
This takes in user inputs. It takes into account of
multiple paragrapgs which is unable to be done with input()
'''
print("COMPARE. Press 'Enter' -> 'Ctrl+D' to finish:")
contents = []
final_data = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)
printable = set(string.printable)
for cstring in contents:
    cstring = ''.join(filter(lambda x: x in string.printable, cstring))
    final_data.append(cstring.translate(str.maketrans('', '', string.punctuation)).lower().strip())
del contents

'''
Input the user input into the current dictionary
'''
temp = []
compare_dic = {}
for sentence in final_data:
    temp = sentence.split(" ")
    for word in temp:
        if (word != ""):
            if word in compare_dic: # in dictionary
                compare_dic[word] += 1
            else: # not in dictionary
                compare_dic[word] = 0
del temp

'''
Compare the two dictionaries
'''
score = 0
word = 0
for data in compare_dic:
    word += 1
    if data in data_dic:
        score += int(data_dic[data])

print("Score: ", score)
print("Words: ", word)
print("AVG:   ", "%.2f" % (score/word))
