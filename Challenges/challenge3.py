def missingCharacters(s):
    
    MaxChar = 26
    
    x = [False for i in range(MaxChar)]
    y = []
    

    for i in range(len(s)):
        if (s[i] >= 'a' and s[i] <= 'z'):
            x[ord(s[i]) - ord('a')] = True
        if (s[i].isdigit()):
            y.append(int(s[i]))
        
    
    result = "".join(str(x) for x in range(10) if x not in y)

    for i in range(MaxChar):
        if (x[i] == False):
          result += chr(i + ord('a'))
        
    return result
    
    