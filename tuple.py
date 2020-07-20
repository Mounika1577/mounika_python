def get_data(aTuple):
    nums=()
    words=()
    for t in aTuple:
        nums=nums+(t[0],)
        
        if t[1] not in words:            
            words=words+(t[1],)
            
        else:
            print(words)
            print(nums)
            idx=words.index(t[1])
            sum=nums[idx]+t[0]
            nums = nums[0:idx] + (sum,) + nums[idx+1:len(nums)-1]
            # temp = nums[0:idx]
            # #print(temp)
            # temp=temp+(sum,)
            # #print(temp)
            # temp =temp+nums[idx+1:len(nums)-1]
            # nums=temp
    min_n=min(nums)
    max_n=max(nums)
    unique_words=len(words)
    return(min_n,max_n,unique_words)
t1=((2,'one'),(4,'new'),(12,'truck'),(6,'new'),(10,'truck'),(2,'one'))
v1,v2,v3=get_data(t1)
print('min:',v1)
print('max:',v2)
print('u_words:',v3)