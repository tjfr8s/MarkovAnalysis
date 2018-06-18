import random
import string

def markov_map(fileName):
    markovMap = {}
    textString = open(fileName).read()
    strippables = string.whitespace #+ string.punctuation
    textList = textString.split()
    processed = []

    for word in textList:
        word = word.strip(strippables)
        processed.append(word)
    #print(processed)

    count = 0
    prefixLength = 2

    # Make dictionary that maps prefix pairs of words to 
    # all possible postfixes
    for word in processed[:len(processed)-3]:
        prefixList = []
        # Make a prefix of desired length
        for number in range(prefixLength):
            prefixList.append(processed[count + number])

        prefix = tuple(prefixList)
        postfix = processed[count + prefixLength]

        # Map prefix to postfix in markovMap
        if prefix in markovMap:
            markovMap[prefix].append(postfix)
        else:
            markovMap[prefix] = [postfix]

        count += 1
        
    print(markovMap)
    #for key in markovMap:
        #print(key, markovMap[key])
    return markovMap


def random_text(markovMap, n = 10):
    #print(markovMap)
    keys = list(markovMap)
    # Choose initial random key and add it to the story.
    key = random.choice(keys)
    story = ' '.join(list(key))
    for number in range(n):
        
        # Find possible suffixes.
        suffixes = markovMap.get(key, None)
        if suffixes == None:
            random_text(markovMap,n-1)
            return

        # Choose random suffix.
        suffix = random.choice(suffixes)
        nextPart = list(key)

        # Add suffix to story.
        story = story + ' '+ suffix

        # Generate next key.
        nextPart.append(suffix)
        del nextPart[0]
        key = tuple(nextPart)
    
  # need to determine next key from current story 

markovMap = markov_map('bee.txt')
randomStory = random_text(markovMap)
print(randomStory)

