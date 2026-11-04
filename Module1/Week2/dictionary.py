def dictionarize(string):
    stored = {}
    for c in string:
        if c not in stored:
            stored.setdefault(c,0)
        stored[c] += 1
    return stored
string = "happiness" 
print(dictionarize(string))