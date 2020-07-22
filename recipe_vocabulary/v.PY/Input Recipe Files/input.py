import os, re, string

file_name = "Data/alex.txt"
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
print("INPUT. Press 'Enter' -> 'Ctrl+D' to finish:")
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
for sentence in final_data:
    temp = sentence.split(" ")
    for word in temp:
        if (word != ""):
            if word in data_dic: # in dictionary
                data_dic[word] += 1
            else: # not in dictionary
                data_dic[word] = 1
del temp

'''
Convert dictionary into text file
'''
file = open(file_name, "w")
for data in data_dic:
    temp = data + " " + str(data_dic[data]) + "\n"
    file.write(temp)

file.close()
