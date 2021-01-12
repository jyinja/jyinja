#Simple password generator created by Jason Yin
#jyinja on Github
import random
import string
s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYN!@#$%^&*()?"
minpasslength = 6
maxpasslength = 30
passW = ""
counter = 0
platform = ""
len = int(input("How long would you like your password? : "))
while len<minpasslength or len>maxpasslength:#setting up the min length of the password, nothing below 6 though and also nothing more than 30 characters
    print("Password length is too short. Please enter new password length")
    len = int(input("How long would you like your password? : "))
platform = str(input("What website/application/platform is this password for? : "))
while platform=="" or platform.isspace():#what site or app is the password for
    print("You didn't enter valid input. Try again. ")
    platform = input("What website/application/platform is this password for? : ")
saver = str(input("Would you like to save your password? (Y/N) : "))
while saver=="" or saver.isspace() or saver!="Y" and saver!="y" and saver!="n" and saver!="N": #checking whether or not to save the input in a txt file
    print("You didn't enter valid input. Try again. ")
    saver = input("Would you like to save your password? (Y/N) : ")

#generate pass
while counter!=len:
    passW=str("".join(random.sample(s,len)))
    counter+=1
   
#file input output
if saver == "Y" or saver == "y":
    outputfile = open("passBackUp.txt","a")#open in append mode, creates the file if it doesn't already exist
    outputfile.write(str(platform)+" | "+str(passW)+"\n")#the platform and the password are separate by a vertical line with space patting on the sides
    outputfile.close
    print("Successfully written to file")
elif saver == "N" or saver=="n":
    #just prints to the screen instead of opening a file for appending
    print(platform+" : "+passW+"\n") 
