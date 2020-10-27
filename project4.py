import random


def main():

    cheese = input("What fortunes text do you want to open?")
    display_fortunes = file_reader(cheese)

    choice = random.choice(display_fortunes)
    print(choice)

    while(input("Would you like another fortune?").lower() == "yes"):
        choice = random.choice(display_fortunes)
        print(choice)



def file_reader(beef):


    infile1 = open(beef)
    readfile1 = infile1.readlines()

    fortunes = []
    temp_line = ""

    for item in readfile1:
        x = "%" in item
        if x == True:
            fortunes.append(temp_line)
            temp_line = ""
        else:
            temp_line += item


    return fortunes







main()
