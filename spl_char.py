txt1=input('enter the input:')
spl_cnt=0
mini_punc=',:;\.\'"'
for i in txt1:
    if not(i.isalpha() or i.isdigit() or i.isspace() or i in mini_punc):
        spl_cnt=spl_cnt+1
        print(i,spl_cnt)
print('total special char = ',spl_cnt)








