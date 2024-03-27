Persons = []

while True:
    Choice = int(input("Press\n1. For Add\n2. For Display\n3. For Update\n4. For Delete\n5 For Exit:- "))
    if Choice == 1:
        Id = int(input("Enter a Id: "))
        flag = True
        for i in Persons:
            if i["Id"] == Id:
                flag = False
                break

        if flag == True:
            Name = input("Enter a Name: ")
            Age = int(input("Enter a Age: "))
            d = {"Id":Id,"Name":Name,"Age":Age}
            Persons.append(d)
        else:
            print("\n----------------\n")
            print("Id Already Exists\n")
            print("----------------\n")



    elif Choice == 2:
        if len(Persons)>0:
            print("\n----------------\n")
            for i in Persons:
                for j,k in i.items():
                    print(j,"-",k)
                print("----------------")

        else:
            print("\n----------------\n")
            print("No Data Found\n")
            print("----------------\n")

    elif Choice == 3:
        Id = int(input("Enter a Id: "))

        index = -1
        for i in range(len(Persons)):
            if Persons[i]["Id"] == Id:
                index = i
                break
        if index != -1:
            Name = input("Enter a Name: ")
            Age = int(input("Enter a Age: "))
            d = {"Id":Id,"Name":Name,"Age":Age}
            Persons[index].update(d)
        else:
            print("\n----------------\n")
            print("Id Dosent Exists\n")
            print("----------------\n")
        
        print("----------------\n")

    elif Choice == 4:
        Id = int(input("Enter a Id: "))

        index = -1
        for i in range(len(Persons)):
            if Persons[i]["Id"] == Id:
                index = i
                break
        if index != -1:
            Persons.pop(index)
        else:
            print("\n----------------\n")
            print("Id Dosent Exists\n")
            print("----------------\n")
        


    elif Choice == 5:
        print("\n---------------------------------")
        print("Thanks for Using...")
        print("\n---------------------------------")
        break

    else:
        print("\nInvalid Choice\n")