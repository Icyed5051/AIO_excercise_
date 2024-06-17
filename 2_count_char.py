def no_repeat(name):
    result = ''
    for i in range(len(name)):
        if(result.find(name[i]) == -1):
            result += name[i]
        else: continue
    return result

def count_char(name):
    dictionary = {}
    temp = no_repeat(name)
    for i in range(len(temp)):
        num = name.count(temp[i])
        dictionary[temp[i]] = num
    return dictionary


print(count_char("Happiness"))
