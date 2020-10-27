#owen lafont

#import the ability to randomly select
import random



#main function
def main():
#input what text file you want to open up
    cheese = input("What fortunes text do you want to open?")
#this variable is the whole file_reader function that is going to represented in this function
    display_fortunes = file_reader(cheese)
#this is how we are going to randomly select a fortune from the list of fortunes
    choice = random.choice(display_fortunes)
    print(choice)

#this while loop will ask you if you want another fortune and continue the process. if you say yes, it will give you another fortune and continue to ask you, if you say no the program will close.
    while(input("Would you like another fortune?").lower() == "yes"):
        choice = random.choice(display_fortunes)
        print(choice)



def file_reader(cheese):

#open the file that was asked from input
    infile1 = open(cheese)
#read the lines in the .txt file
    readfile1 = infile1.readlines()

#this is where the list that is going to be randomly selected from will be filled with the fortune cookie sayings. the loop handles the process of creating the fortunes list to pick from
    fortunes = []
#
    temp_line = ""
#this is the for loop that separates the fortune txt into a list of individual
    for item in readfile1:
# since the .txt file provided is separated by %, we are going to give the % a variable named x
        x = "%" in item
#if x is true, or in other words, if a % is detected, add to the fortunes line. This is how the list of fortunes to be randonly selected from is created
        if x == True:
            fortunes.append(temp_line)
            temp_line = ""
 #if there is no %, continue reading
        else:
            temp_line += item

#return the created list of fortunes to the main function
    return fortunes







main()
