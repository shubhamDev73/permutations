def permute(w):
    permuts = []
    for i in range(len(w)):
        w2 = ""
        for j in range(len(w)):
            if j != i:
                w2 += w[j]
        if len(w2) > 0:
            l = permute(w2)
            for j in l:
                p = w[i]+j
                permuts.append(p)
    if len(permuts) == 0:
        permuts.append(w)
    return permuts
word = raw_input("Enter a word to get it's permutations: ")
while " " in word:
    print "'"+word+"' is not A WORD!!! Enter again"
    word = raw_input("Enter a word to get it's permutations : ")
p = permute(word)
permutations = []
for i in p:
    if i not in permutations:
        permutations.append(i)
permutations.sort()
print "All possible permutations of",word,"in alphabetical order are : "
for i in permutations:
    print i
print "Total permutations are :",len(permutations)
print "Position of",word,"in a dictionary of all it's permutations is",
for i in range(len(permutations)):
    if permutations[i] == word:
        print i+1
        break
