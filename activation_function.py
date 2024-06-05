import math

# Given
def is_number ( n ) :
    try :
        float ( n ) # Type - casting the string to ‘float ‘.
                    # If string is not a valid ‘float ‘ ,
                    # it ’ll raise ‘ValueError ‘ exception
    except ValueError :
        return False
    return True

def activation_function():
    x = input('Input x = ')
    if(is_number(x) == False): 
        print('x must be a number')
        return
    x = float(x)
    activation = input('Input activation Function (sigmoid|relu|elu): ')
    if(activation == 'sigmoid'):
        sigmoid = 1 / (1 + math.e**(-x))
        #print(type(sigmoid))
        print(f'sigmoid: f({x}) = {sigmoid}')
        
    elif(activation == 'relu'):
        if(x <= 0):
            print(f'relu: f({x}) = 0')
        else:
            print(f'relu: f({x}) = {x}')
            
    elif(activation == 'elu'):
        if(x <= 0):
            alpha = 1.0
            elu = alpha * (math.e ** x - 1)
            print(f'relu: f({x}) = {elu}')
        else:
            print(f'relu: f({x}) = {x}')
            
    else:
        print(f'{activation} is not supported')
activation_function()