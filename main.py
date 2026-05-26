#linear search
list1= [1,2,3,4,5,6,7,8,9,10]
print(list1)
key=int(input("What number do you want to search?: "))
found=False

for i in range(0,len(list1)):
    if list1[i] == key:
        print("The key exists")
        found=True
        break
if found == False:
    print("The key does not exist") 
