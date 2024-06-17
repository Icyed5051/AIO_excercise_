def max_num_list(x, k):
    result = []   
    for i in range(len(x) - k + 1):
        dump = x[i:i+k]
        #print(max(dump))
        result.append(max(dump))
    return result  
        

num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
print(max_num_list(num_list,3))