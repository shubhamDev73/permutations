# Printing permutations of a word using recursion


def permute(word):

    '''The recursive permuting function
    Takes a word and returns its permutations'''

    allPermutes = []
    for i in range(len(word)):
        # subWord is the word without one character
        subWord = ""

        for j in range(len(word)):
            if j != i:
                subWord += word[j]

        if len(subWord) > 0:
            subPermutes = permute(subWord)
            for j in subPermutes:
                allPermutes.append(word[i] + j)

    if len(allPermutes) == 0:
        allPermutes.append(word)
    return allPermutes


if __name__ == "__main__":
    # Running the program

    word = input("Enter a word to get it's permutations: ")
    # Checking input
    while " " in word:
        print("'", word, "' is not A 'WORD'!!! Enter again")
        word = input("Enter a word to get it's permutations : ")

    # Permutations returned contains repititions!!
    fakePermutations = permute(word)
    permutations = []
    for i in fakePermutations:
        if i not in permutations:
            permutations.append(i)

    # Who doesn't like sorted lists?
    permutations.sort()

    # Displaying the permutations
    print("All possible permutations of", word, "in alphabetical order are : ")
    print('\n'.join(permutations))

    # Displaying additional information
    print("Total permutations are :", len(permutations))
    for i in range(len(permutations)):
        if permutations[i] == word:
            print("Position of", word,
                  "in a dictionary of all it's permutations is", (i + 1))
            break
