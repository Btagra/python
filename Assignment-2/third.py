# Write a program to calculate the frequency of any special
# character if that exist in any string.
import re 
x="hello&*$$world"
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
y=regex.findall(x)
   
d=dict()
for i in y:
        d[i]=y.count(i)  

# d = {i:y.count(i) for i in y}
   
print d  

