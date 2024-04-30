
import inflect 
# Imports library for number conversion

import time
# Imports time for countdown 

import winsound
# Imports sound at the end of the countdown

def start():
    print("Many Menus")
    print(f"\t1. Palindrome Checker\n\t2. Convert Number to Words\n\t3. Alarm\n\tx. Exit")

    while True:
        choice1 = input("* Select an option: ")
        print("")


        match choice1:
            case '1':
                palindrome_checker()
                goHome()
                break
            case '2':
                convert_to_words()
                goHome()
                break
            case '3':
                countdown()
                goHome()
                break
            case 'x':
                print("Exiting the program...")
                break
            case _:
                print("Enter a number from '1-3' or 'x': ")


def palindrome_checker():
    print("")
    string = str(input("Enter anything and find out if it's a palindrome: "))
    flipped_string = string[::-1]
    if flipped_string == string:
        print(f"Congratulations!, '{string}' is a palindrome.")
    else:
        print(f"Sorry, '{string}' is not a palindrome.")


def convert_to_words():
    while True:
        print("")
        try:
           num = int(input("Enter any number and get it in words:"))
           break
        except ValueError:
           print("Try Again. Enter a number")

    def convert(num):
        p = inflect.engine()
        return p.number_to_words(num) # Using the number_to_words function from the inflect library
    
    words = convert(num)
    print("")
    print(words.title())



def countdown():
    def alarm(minutes):
        seconds = minutes * 60 # Changes time to seconds
        time.sleep(seconds) # starts countdown
        winsound.PlaySound("alarm.wav", winsound.SND_FILENAME) # Next  line  after countdown plays the sound with  winsound
        print("Time's Up!")
    
    

    while True:
        try:
            print("Enter the time for the alarm in minutes:")
            time_input = int(input())
            print(f"Alarm set for {time_input} minutes.")
            alarm(time_input)
        except ValueError:
            print("Please enter a valid number of minutes.")

    

def goHome():
    print("")
    
    while True:
        decision = input("Home-'0' | Exit-'x' : ")
        print("")

        match decision:
            case '0':
                start()
                break
            case 'x':
                print("Exiting the program...")
                break
            case _:
                print("Enter either '0 - Home' or 'x - Exit'")


start()
