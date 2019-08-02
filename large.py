numa = float(input("Enter numbera: "))
numb = float(input("Enter numberb: "))
numc = float(input("Enter numberc: "))
 
if (numa > numb) and (numa > numc):
   largest = numa
elif (numb > numa) and (numb > numc):
   largest = numb
else:
   largest = numc
 
print("The largest number is",largest)
