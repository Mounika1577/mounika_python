import math

incr=0.1
cube=1225
guess=10
for i in range(20):
    
    
    if(math.floor(guess**3)==cube):
        print(math.floor(guess**3))
        break
    guess=guess+incr
