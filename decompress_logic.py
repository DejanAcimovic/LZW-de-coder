def CreateDictionary_reverse():
    dictionary = {0:'#'}
    for i in range(65,127):
        dictionary.update({len(dictionary):chr(i)})
    for i in range(32,65):
        if chr(i) != '#':
            dictionary.update({len(dictionary):chr(i)})

    return dictionary

def LZW_decoder(code_sentence):
    dictionary = CreateDictionary_reverse()
    new_str = ""
    code_sentence = code_sentence + '#'
    sentence = ""
    i = 0
    ch = code_sentence[i]
    while ch != '#':
        temp = ch
        while ch!=' ' and ch != '#':
            i = i+1
            ch = code_sentence[i]
            temp = temp + ch
        ch = int(temp)
        p = dictionary.get(ch)
        #ako se desava ekspanzija podataka, ne moze dekodirati, upravlja izuzetkom
        if ch not in dictionary.keys():
            p = new_str + new_str[0]
        ################################################   
        sentence = sentence + p 
        if new_str!="":
            dictionary.update({len(dictionary):new_str + p[0]})
        i = i + 1
        ch = code_sentence[i]
        new_str = p
    return sentence


dictionary = {'#':0}
for i in range(ord('A'),ord('Z')):
    dictionary.update({i-ord('A')+1:chr(i)})
