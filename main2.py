#Binary search
list1=[1,2,3,4,5,6,7,8,9,10]
key=int(input("Enter a number to search: "))
start=0
end=len(list1)-1
found=False

while start <= end:
    mid=(start + end) // 2
    if list1[mid]==key:
        print("The key exists")
        found=True
        break
    elif list1[mid]>key:
        end=mid-1
    else:
        start=mid+1

if found == False:
    print("The key does not exist")
    
