class stack1:
    
    def __init__(self):
        self.s=[ ]

    def push(self,x):
        self.s.append(x)
      
    def isempty(self):
        if(self.get_size(self.s)==0):
            return True
        else:
            return False
    def pop(self):
        if(self.get_size(self.s)==0):
            return -1
        else:
            temp=self.s[self.get_size(self.s)-1]
            self.s.pop()
            return temp
    def get_size(self,stk):
        return len(stk)
abc=stack1()
mismatch=False
input="[(){}]"
for i  in range(len(input)):
    if(input[i]=="[" or input[i]=="(" or input[i]=="{"):
        abc.push(input[i])
        print(input[i])
    else:
        if(input[i]=="]" and abc.pop()=="["):
            continue
        print(input[i])
        if(input[i]==")" and abc.pop()=="("):
            continue
        print(input[i])
        if(input[i]=="}" and abc.pop()=="{"):
            continue
        print(input[i])
        mismatch=True
        break
if(mismatch==True):
    print("invalid brackets")
else:
    print("valid brackets")