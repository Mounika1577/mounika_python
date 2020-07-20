txt1=input('enter the input:')
spl_cnt=0
mini_punc=',:;\.\'"'
spl_char=' '
for i in txt1:
        if not(i.isalpha() or i.isdigit() or i.isspace() or i in mini_punc):               
                
                if i not in spl_char:
                    spl_cnt=spl_cnt+1
                    spl_char=spl_char+i
                
                    print(spl_cnt,i)

print('total special char = ',spl_cnt)





#' I am @ home, && feel ^^good^^ there is no cat #food# '
