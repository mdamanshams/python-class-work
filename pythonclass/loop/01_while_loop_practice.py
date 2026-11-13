# printing number in reverse from 100 to 1.
#i=100
#while i>=1:
#    print(i)
#  i=i-1

#printing a table of 3 & we can print any number's table
#i=3
#while i<=30:
#   print(i)
#   i=i+3
#i=1
#while i<=10:
#    print(3*i)
#    i=i+1

#printing the element of the following list using loop
# [1,4,9,16,25,36,49,64,81,100]
#i=1
#while i<=10:
#    print(i*i)
#    i=i+1


#nums=[1,4,9,16,25,36,49,64,81,100] second method of printing
#idx=0
#while idx<len(nums):
#    print(nums[idx])
#   idx=idx+1

#search for a number x in the tuple using loop
# [1,4,9,16,25,36,49,64,81,100]
#nums=(1,4,9,16,25,36,49,64,81,100)
#i=1
#while i<len(nums):
#   if(nums[i]==x):
#        print("found at ", i)
#        break #it is used to brake the loop
#  else:
#        print("not found")
#    i=i+1
nums=(1,4,9,16,25,36,49,64,81,100)
i=1
while i<=10:
    if(i==5):
        break
    i=i+1
print(i)
