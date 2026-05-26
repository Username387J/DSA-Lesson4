contactList=["Alice","Bob","Charlie","Dave","Eve"]
person=input("Who are you looking for?: ")
found=False

for i in range(0,len(contactList)):
    if contactList[i] == person:
        found=True
        print("Found {} at index {}".format(person,i))
        break
if found==False:
        print("Contact not found")