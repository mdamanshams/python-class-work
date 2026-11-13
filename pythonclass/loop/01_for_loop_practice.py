#printing the element of the following list using loop
# [1,4,9,16,25,36,49,64,81,100]

#num= [1,4,9,16,25,36,49,64,81,100]
#for el in num:
#    print(el)

#search for a number x in the tuple using loop
# [1,4,9,16,25,36,49,64,81,100]

num= (1,4,9,16,25,36,49,64,81,100)
x=36
i=0
for el in num:
    if(el==x):
        print("value found", i)
        break
    i=i+1