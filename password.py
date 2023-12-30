import random     #we have to import random for random selection 
lower_case="abcdefghijklmnopqrstuvwxyz"
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="0123456789"
symbol="{}[]#()*;._-"
Rans=lower_case+upper_case+num+symbol
length=9
password="".join(random.sample(ans,length))# i am using join (dot)operator 
print("Generated password is",password) 
