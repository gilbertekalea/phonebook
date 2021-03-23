import csv, sys
import datetime

#create contact list
def AddContact():
    name = input("name: ").strip()
    number = int(input("phonenumber: ").strip())
    email = input("email: ").strip()
    address = input("address: ").strip()

    #store input in a dictionary format
    contactInfor = dict(name=name, number=number, email=email, address=address, date_created=datetime.date.today())
    
   #then store that same information in a csv file. 
    with open('phonedata.csv', 'a', newline='') as contact:
        fieldnames = ['name', 'number', 'email', 'address', 'date_created']
        writer = csv.DictWriter(contact, fieldnames=fieldnames)
        writer.writerow(contactInfor)

    #Avoid reruning the scripting, ask users to if they would like to add another contact:
    add_query = input("Do you want to search something else? Y/N: ")
    if add_query == 'Y':
        add= AddContact()
    elif add_query == 'N':
        print(("*")*20, end=None)
        print("You are logged out")
        print(("*")*20, end=None)
        print("Thank you for using our services")
        sys.exit()
    return add

#Searching for contact: by name, number, email, address or date
def ContactSearch():
    with open('phonedata.csv', newline='') as file:  #Open the csv file containing list of contacts:
        reader = list(csv.DictReader(file))  #convert the csv into readerable dict
        q = input("Enter name or Number: ")  # search query :
        for i in range(0, len(reader)):
            if q in reader[i].values(): # q can be name, number, email, address
                print(("#")*20, "Printing Results", ("#")*20,end=None)
                result = reader[i].items() #return items where the query matched.
                print(result)
                print(("#")*20, "done Printing", ("#")*20, end=None)
                break
            if q not in reader[i].values(): #Avoid printing not found anytime q is not found in reader[i].
                #Until the program loops through the whole dict, then print the not found
                continue
        else:
            print(("#")*20, end=None)
            print("Please the contact can't be found!!")
            print(("#")*20, end=None)

            #asking for more actions
            search_query = input("Do you want to search something else? Y/N: ")
            if search_query == 'Y':
                search = ContactSearch()
            elif search_query == 'N':

                print(("*")*20, end=None)

                search = "logging you out"
                print(search + "done")
                print(("*")*20, end=None)
                print("Thank you for using our services")
                sys.exit()
            return search
def contactdelete():
    with open('phonedata.csv', newline='') as delfile:
        file_del = list(csv.DictReader(delfile))
        for i in range(0, len(file_del)):
            delquery = input("What would you like to delete:")
            if delquery in file_del[i].values():
                delete = file_del[i].values()
                del delete
                sys.exit()
                
def welcome():
    question = input(
        "Reply C to Create contact or S for search: ")
    if question == "C":
        follow = AddContact()
    elif question == "S":
        follow = ContactSearch()
    elif question=="D":
        follow = contactdelete()
    return follow
welcome()
