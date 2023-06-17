import os


def showContacts(fileName):
    os.system("CLS")
    with open(fileName, 'r') as file:
        data = file.readlines()

        for contact in data:
            print(contact, end='')

    input("\npress any key")


def addContact(fileName):
    os.system("CLS")
    with open(fileName, 'a') as file:
        res = '\n'
        res += input("Input a surname of contact: ") + "\t\t"
        res += input("Input a name of contact: ") + "\t\t"
        res += input("Input a phone number of contact: ")

        file.write(res)

    input("press any key")


def searchContact(fileName):
    os.system("CLS")
    target = input("Input the target: ")

    with open(fileName, 'r') as file:
        data = file.readlines()

        for contact in data:
            if target in contact:
                print(contact)
                break
        else:
            print("sorry, not found")

    input("press any key")


def changeContact(fileName):
    os.system("CLS")
    target = input("Input the target: ")

    with open(fileName, 'r') as file:
        data = file.readlines()

    for contact in data:
        if target in contact:
            print(contact)
            contactArr = contact.split()
            print("What do you want to change: ")
            print("1 - surname")
            print("2 - name")
            print("3 - phone number")

            userChoice = int(input())
            changedContact = input("Input new information: ")

            if userChoice == 1:
                contact = contact.replace(contactArr[0], changedContact)
            elif userChoice == 2:
                contact = contact.replace(contactArr[1], changedContact)
            elif userChoice == 3:
                contact = contact.replace(contactArr[2], changedContact)
            break
    else:
        print("sorry, not found")

    with open(fileName, 'r+') as file:
        file.writelines(contact)

    print("Changed contact: " + contact)
    input("press any key")


def deleteContact(fileName):
    os.system("CLS")
    target = input("Input the target: ")

    with open(fileName, 'r+') as file:
        data = file.readlines()

        for contact in range(len(data)):
            if target in data[contact]:
                print(data[contact])
                userChoice = input("Delete contact?(Y/N): ").lower()
                if userChoice == "y":
                    print(f"Contact {data[contact]}deleted.")
                    data[contact] = ""
                    
                break
        else:
            print("sorry, not found")

    data = list(filter(None, data))
    with open(fileName, 'w') as file:
        file.writelines(data)

    input("press any key")


def drawing():
    print('1 - show contacts')
    print('2 - add contact')
    print('3 - search contact')
    print('4 - change contact')
    print('5 - delete contact ')
    print('6 - exit')


def main(fileName):
    while True:
        os.system('CLS')
        drawing()
        userChoice = int(input("Input a number of operation: "))

        if userChoice == 1:
            showContacts(fileName)
        elif userChoice == 2:
            addContact(fileName)
        elif userChoice == 3:
            searchContact(fileName)
        elif userChoice == 4:
            changeContact(fileName)
        elif userChoice == 5:
            deleteContact(fileName)
        elif userChoice == 6:
            print("OK")
            return


main("8lesson/text.txt")
