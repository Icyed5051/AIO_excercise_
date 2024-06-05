import math
import random

def regression_loss():
    n = input('Input number of samples ( integer number ) which are generated : ')
    if(n.isnumeric() == False): 
        print('number of samples must be an integer number') 
        return
    n = int(n)
    tmae = 0
    tmse = 0
    loss_name = input('Input loss name: ')
    for i in range(0,n,1):
        pred = random.uniform(0,10);
        target = random.uniform(0,10);
        if(loss_name == 'MAE'):
            mae = abs(target - pred)
            tmae = tmae + mae
            print(f'loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}, loss: {mae}')
        elif(loss_name == 'MSE'):
            mse = (target - pred)**2
            tmse = tmse + mse
            print(f'loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}, loss: {mse}')
    
    if(loss_name == 'MAE'): print('final MAE: ',(1/n) * tmae)
    elif(loss_name == 'MSE'): print('final MSE: ',(1/n) *tmse)
    

#regression_loss()