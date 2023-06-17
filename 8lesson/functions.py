import os


def showContacts(fileName):
    os.system("CLS")
    with open(fileName, 'r') as file:
        data = file.readlines()

        for contact in data:
            print(contact, end='')

    input("\npress any key")


def addContacts(fileName):
    with open(fileName, 'a') as file:
        res = '\n'
        res += input("Input a surname of contact: ") + "\t\t"
        res += input("Input a name of contact: ") + "\t\t"
        res += input("Input a phone number of contact: ")

        file.write(res)

    input("press any key")


def searchContacts(fileName):
    target = input("Input the target: ")

    with open(fileName, 'r') as file:
        data = file.readlines()

        for contact in data:
            if target in contact:
                print(contact)
                break
        else:
            print("sorry, no")

    input("press any key")


def drawing():
    print('1 - show contacts')
    print('2 - add contact')
    print('3 - search contact')
    print('4 - exit')


def main(fileName):
    while True:
        os.system('CLS')
        drawing()
        userChoice = int(input("Input a number of operation: "))

        if userChoice == 1:
            showContacts(fileName)
        elif userChoice == 2:
            addContacts(fileName)
        elif userChoice == 3:
            searchContacts(fileName)
        elif userChoice == 4:
            print("OK")
            return


main("8lesson/text.txt")
