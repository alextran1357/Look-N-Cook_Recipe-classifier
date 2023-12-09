# Access verb text file for read
file_name = "data/Cooking words/cooking_verbs.txt"
with open(file_name, 'r') as file:
    cooking_verbs = [line.strip() for line in file]

# Acess noun text file for read
file_name = "data/Cooking words/cooking_nouns.txt"
with open(file_name, 'r') as file:
    cooking_nouns = [line.strip() for line in file]

# Sorting
cooking_verbs.sort()
cooking_nouns.sort()

# Access verb text file for write
file_name = "data/Cooking words/cooking_verbs.txt"
with open(file_name, 'w') as file:
    for item in cooking_verbs:
        file.write("%s\n" % item)
        
# Acess noun text file for write
file_name = "data/Cooking words/cooking_nouns.txt"
with open(file_name, 'w') as file:
    for item in cooking_nouns:
        file.write("%s\n" % item)