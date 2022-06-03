# Dictionaries

filename = "dataset/mbox-short.txt"
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = {}
for line in handle:
    word = line.split()
    if len(word) < 3 or word[0] != "From" : continue
    email = word[1]
    if email in counts :
        counts[email] = 1 + counts[email]
    else :
        counts.update({email:1})
max = 0
value = ""
for i in counts:
    if (counts[i]) > max :
        max = counts[i]
        value = i
print(value, max)