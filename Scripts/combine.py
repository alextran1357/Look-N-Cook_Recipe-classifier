import itertools
import collections

'''
Combines two dictionaries together, taking in consideration of common keys
'''
def combine_dictionaries(master_dic, temp_dic):
    Cdict = collections.defaultdict(int)

    for key, val in itertools.chain(master_dic.items(), temp_dic.items()):
        Cdict[key] += val
    return dict(Cdict)

'''
Getting all the data of the individual data files
'''
# Check for continuation
print("WARNING")
print("You are about to combine all data together.")
temp = input("Type 'combine' to continue: ")
temp.lower()
if (temp != "combine"):
    sys.exit()

files = ['alex.txt','dane.txt','henry.txt','john.txt','jose.txt']
master_dictionary = {}
for x in range(len(files)):
    file_name = "Data/" + files[x]
    file = open(file_name, 'r')
    data = file.readlines()
    file.close()
    open(file_name, 'w').close()
    
    #Get content of individual file
    strip_data = []
    data_dic = {}
    for i in data:
        strip_data.append(i.strip())
    for i in range (len(strip_data)):
        temp = strip_data[i]
        temp = temp.split(" ")
        data_dic[temp[0]] = int(temp[1])
    del strip_data
    
    master_dictionary = combine_dictionaries(master_dictionary, data_dic)

'''
Adding everything into the final data file
'''
file_name = "Data/Final/vocab_list_py.txt"
file = open(file_name, 'r')
data = file.readlines()
file.close()

# Extracting dictionary content
strip_data = []
data_dic = {}
for i in data:
    strip_data.append(i.strip())
for i in range (len(strip_data)):
    temp = strip_data[i]
    temp = temp.split(" ")
    data_dic[temp[0]] = int(temp[1])
del strip_data

master_dictionary = combine_dictionaries(master_dictionary,data_dic)
print(master_dictionary)
# Write to final data file
file = open(file_name, 'w')
for data in master_dictionary:
    temp = data + " " + str(master_dictionary[data]) + "\n"
    file.write(temp)
file.close()
print("complete")



