def levenstein(source,target):
    rows = len(source) + 1
    cols = len(target) + 1
    table = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range (0,rows):
        table[i][0] = i
    for j in range (0,cols):
        table[0][j] = j    
    
    for i in range(1,rows):
        for j in range(1,cols):
            insert = table[i - 1][j]  + 1
            delete = table[i][j - 1] + 1
            if(target[j - 1] == source[i - 1]): temp = 0 
            else: temp = 1
            sub = table[i - 1][j - 1] + temp
            table[i][j] = min(insert,delete,sub)
        
    return table[i][j]


print(levenstein("yu","you"))
