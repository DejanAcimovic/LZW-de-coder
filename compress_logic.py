def CreateDictionary():
    dictionary = {'#':0}
    for i in range(65,127):
        dictionary.update({chr(i):len(dictionary)})
    for i in range(32,65):
        if chr(i) != '#':
            dictionary.update({chr(i):len(dictionary)})
    
    return dictionary

def LZW(sentence):
    #dictionary = CreateDictionary(sentence)
    dictionary = CreateDictionary()
    sentence = sentence + '#'
    code_sen = ""
    i=0
    new_str=sentence[i]
    ch = sentence[i]
    while ch != '#' :
        i = i + 1
        ch=sentence[i]
        if new_str+ch in dictionary.keys():
            new_str = new_str + ch
        else:
            code_sen = code_sen + str(dictionary.get(new_str)) + " "
            dictionary.update({new_str+ch:(len(dictionary))})
            new_str = ch
    return code_sen
