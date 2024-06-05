import math
import random
#excercise 1
def classification_model(tp,fp,fn):
    if(type(tp) != int):
        print("tp must be int")
        return
    elif(type(fp) != int):
        print("fp must be int")
        return
    elif(type(fn) != int):
        print("fn must be int")
        return
    if(tp <= 0 or fp <= 0 or fn <= 0):
        print("tp and fp and fn must begreater than zero")
        return
    
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * ((precision * recall) / (precision + recall))
    
    print('precision is ', precision)
    print('recall is ', recall)
    print('f1-score is ', f1_score)
    
#activation(tp = 2.1, fp = 3 , fn = 1)
