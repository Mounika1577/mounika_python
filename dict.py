# keys=["ten","twenty","thirty"]
# values=[10,20,30]
# sampledict=dict(zip(keys,values))
# print(sampledict)


# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# #dict3={**dict1,**dict2}
# #dict3=dict1.update(dict2)
# dict3=dict1.copy()
# dict3.update(dict2)
# print(dict3)

# sampleDict = {"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
# print(sampleDict["class"]["student"]["marks"]["history"])

# employees = ['Kelly', 'Emma', 'John']
# defaults = {"designation": 'Application Developer', "salary": 8000}
# res=dict.fromkeys(employees,defaults)
# print(res)

# sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
# keys=["name","salary"]
# for k in keys:
#     print({k:sampleDict[k]})

# sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
# keystoremove={"name","salary"}
# for k in keystoremove:
#     sampleDict.pop(k)
# print(sampleDict)

# sampledict={'a':100,'b':200,'c':300}
# print(sampledict.setdefault('d',400))
# print(sampledict)

# l=[('matt',20),('karim',30),('maya',40)]
# for idx,val in enumerate(l):
#     name=val[0]
#     age=val[1]
#     print(idx,name,age)

# str="python"
# for idx, ch, in enumerate(str,1):
#     print(idx,ch) 


# for idx,val in enumerate(['a', 'b']):
#     print([idx,val])

#print(list(enumerate(['a','b','c'])))

# d = {'a': 1, 'b': 2, 'c': 3}
# for k,v in d.items():
#     print(k,v)


# d_color={'cat:'white',dog':'brown','parrot':'green'}
# #d-color[peacock]=green
# anml=['hen','red and black']
# if anml[0] not in d_color:
#     d_color[anml[0]]=anml[1]
#     print(d_color)
# else:
#     print(anml[0] + 'is already added')

# sales_fruits={'Apple':{'monday':[7,250],'tuesday':[7,275]},'orange':{'monday':[7,200],'tuesday':[7,300]},'Apricot':{'monday':[8,450],'tuesday':[8,200]},'mangoes':{'monday':[25,200],'tuesday':[25,300]},'cherry':{'monday':[9,500],'tuesday':[9,100]}}

# for fruit in sales_fruits.keys():
#         total_stock=0
#         total_value=0
#     #if fruit=='Apple':
#         for day in sales_fruits[fruit].keys():
#             total_stock+=sales_fruits[fruit][day][0]
#             total_value+=sales_fruits[fruit][day][0]*sales_fruits[fruit][day][1]
#         print('weekly stock value for',fruit,'is',total_stock,total_value)

 
# marks={'stu1':55,'stu2':45,'stu3':78}
# m2=marks.copy()
# m2['stu4']=67
# print(id(marks),id(m2))
# print(marks,m2)

# d9={}
# d9['name']='meena'
# d9['phone']='898963'
# d9.get('location','india')
# #print(loc)
# l9=list(d9.items())
# print(d9.items())
# print(l9)

# a=[2,3,4,10,20]
# x=10
# for i in range(len(a)):
#     if a[i]==10:
#         print(i)

 
#teacher={name(saroj,meena),subject(english,hindi),classes(6-8,9-12),times('6A'-'monday'10:15,'6B'-'monday'1:45}

# people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}
# for p_id, p_info in people.items():
#     print("\nPerson ID:", p_id)
#     for key in p_info:
#         print(key + ':', p_info[key])


teacher={1:{'name':'saroj','subject':'english','classes':('6-8','9-12'),'times':{'6A':{'monday':'10:15'},'6B':{'monday':'1:45'}}},2:{'name':'meena','subject':'hindi','classes':('6-8','9-12'),'times':{'6A':{'monday':'11:00'},'6B':{'monday':'11:45'}}}}
for t_id,t_info in teacher.items():
    #print()
    for key in t_info:
        print(key+':',t_info[key])
        #if(type(t_info[key]) == type({})):
        if(key == "times"):
            for key2 in t_info[key]:
                print(key2, t_info[key][key2])
                print(t_info['classes'][0])

