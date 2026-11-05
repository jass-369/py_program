#a={"name":"ritish","age":21,"city":"jaipur"}
#my_dict= dict(name="ram",
#              age=22,
#              city="jaiput"
 #             )
#print(my_dict)

#print(type(a))
##change value
#a["name"]="ram"
#print(a)
#dict={"name":"jass",
#      "age":21,
#      "city":"jaipur",
#      "data":{"name":"lara",33.3:"hight","voice":[33,45,11]},
#      "data2":{"N":"anju","A":13.4,"h":5.7}}
#print(dict)
##value nikalna
#print(dict["data"]["name"][-1])
##get
#print(dict.get('skill'))
#print(dict.get('skill','add nhi kiya'))
##mixed key
#mixed_key={"name":"mob",
#           1:"string",
#           4.44:"flot",
 #          (4,5):"tupple"}
#print(mixed_key)
##data add n updating
#grades={"math":90,"scince":95}
#grades["eng"]=80
#print(grades)
#grades["math"]=95
#grades.setdefault("art",88)
#print(grades)
###data del krna
#grades={"math":56,"science":78,"english":66}
#del (grades)
#print(grades)
#del grades["english"]
#grades.pop("science")
#a=grades.pop("science")
#print(grades,a)
#a=grades.pop("test","key nhi h")
#print(a)
#grades.popitem()
#print(grades)
#a={"math":99,"sci":88,"eng":66,'art':77}
#a['spritualy']=99
#a.popitem()
#print(a.popitem())
##a.clear()
#print(a)
###lenth method
#a={"math":99,
#   "sci":88,"eng":66,'art':77}
#print(len(a))
###membership,only for key 
#a={"math":99,
#   "sci":88,"eng":66,'art':77}
#print('math'in a)
###dict m new dic add
#d1={'a':1,'b':2,}
#d2={'b':5,'c':3,'d':4}
#d1.update(d2)
#print(f"after update=,{d1}")

##mulitiple value
#a=("rohit","manav","harshi")
#b=dict.fromkeys(a,"math")
#print(b)
#a=dict.fromkeys("msea",88)
#print(a)
###
#company={
#    "ceo":{"name":"john due",
#           "role":"Excutive"},
#    "employess":{
 #       101:{"name":"siru",
 #            "role":"Engineer",
#        },
#        102:{
#            "name":"sahu",
#            "role":"Designer"}
 #        },
 #    "Departments": ["HR","Engineer","Design"]   
#         }
#print(company["ceo"]["name"][1])
#print(company.get("ceo").get("employess"))
#print(company.get("employess"))
#print(company.get("employess").get("skill","mathmetics").upper())
###methods
#a={"name":"ishu","age":21,"skill":"manupulation"}
#print(a.keys())
#print(a.values())
#print(a.items())
###
#for loop in dict
#a={"name":"ishu","age":21,"skill":"manupulation"}
#for x in a:
#for x in a.values():
#for x in a.keys():
    #print(a)
    #print(x,a[x])
    #print(x)
#for x in a.items():
  #  print(x[1])
    #print(x[0])
#multiple data asgin
#data=[('name','ishi'),('age',21),("skill","manupulate")]
#for x, y in data:
#    print(x,y)

###loop in dict
#printing only key,values
# key print 
# dict={
#     "name":'rama',
#     "age":21,
#     "physics":"super",
#     'skill':"manupulation"}
#for x in dict:
#    print(x)
#value print
#1for x in dict.values():
#    print(x)
#for x in dict:
#    print(dict[x])
#for x in dict:
#    print(x,dict[x])
#for x in dict.items():
#    print(x[0],x[1])
#for x,y in dict.items():
#    print(x,y)


###que with loop 

##values sum with loop
# groceries = {
#     "bananas": 1.56,
#     "apples": 2.50,
#     "oranges": 0.99,
#     "bread": 4.59,
#     "coffee": 6.99,
#     "milk": 3.39,
#     "eggs": 2.98,
#     "cheese": 5.44
# }
# sos=0
# data=groceries.values()
# for i in data:
#     sos +=i
# for i in groceries:
#     sos +=groceries[i]
# print(sos)

##numeric with loop
#temp=0
#for i in a:
    #if i.isnumeric():
    #    print(i)
#    if i in '0123456789':
 #       temp=temp+1
 #       print(i,temp)

##create dict ,only even num
# dict={}
# for i in range(1,6):
#     dict[i]=i*i
# print(dict)

##filter dict
data = {'x': 10, 'y': 15, 'z': 20, 'w': 25, 'v': 30, 'u': 35}
# for x in data.values():
#      if x % 2 == 0:
#        print(x)
# for x in data:
#         if data[x]%2==0:
#                 print(data[x])
for x , y in data.items():
    if data[x]%2==0:
        print(x,data[x])
         
    
        



    



