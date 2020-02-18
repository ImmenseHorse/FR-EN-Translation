#This program was written by Duc Nguyen on Oct 14, 2019.
#This program Create a program that will test the user’s English-French
#translation abilities. This program will display twenty English words and the
#numbers from 1 to 20. The user will be prompted, “Enter the number of the word
#to be translated.” After entering an appropriate number, the program will then
#ask for the French translation. If the user enters the correct translation,
#they should be given a congratulatory message.
#Variable Dictionary:
#   engwords - the list of English words
#   frenchwords - the list of French words
#   wordnumber - the ordinal number of the English word
#   badinput - the flag for the user's input for wordnumber 
#   keepdisplaying - the flag for the user's wish to either keep displaying the
#                    list of English words or exit the program.
#   answer - the user's reply to the question
#   response - the user's wish to either exit or remain in the program

engwords=["Pepper","Parsnip","Map","Ice","Handsome","Price","Never","Liar",
          "Joke","House","Garlic","Cow","Asparagas","Mouse","Lamb","Knee","Hen",
          "Fox","Pig","January"]
frenchwords = ["Poivre","Panais","Carte","Glace","Beau","Prix","Jamais",
               "Menteur","Plaisanterie","Maison","Ail","Vache","Asperge",
               "Souris","Agneau","Genou","Poule","Renard","Cochon","Janvier"]
for x in range(len(engwords)):
    print(str(x+1)+".",engwords[x])    
keepdisplaying = True
while keepdisplaying:   
    wordnumber = input("Enter the number of the word to be translated. ")
    badinput = True
    while badinput:
        if wordnumber.isdigit():
            if int(wordnumber) < 1 or int(wordnumber) > len(engwords):
                print("The number must be from 1 to",len(engwords))
                wordnumber = input("Enter the number of the word to be translated. ")
            elif engwords[int(wordnumber)-1] == "***":
                print("That word has already been translated.")
                wordnumber = input("Enter the number of the word to be translated. ")
            else:
                badinput = False
                answer = input("What is the French translation of "+engwords[int(wordnumber)-1]+"? ")
        else:
            print("You must enter a number.")
            wordnumber = input("Enter the number of the word to be translated. ")       
    if answer.capitalize() == frenchwords[int(wordnumber)-1]:
        print("Congrats! You got the correct answer!")
        engwords[int(wordnumber)-1] = "***"
        if engwords.count("***") == len(engwords):
            print("Congratulations! You translated them all!")
            print("Thank you for using the program!")
            keepdisplaying = False
        else:
            response = input("Would you like to exit?(Y/N) ")
            while response.lower() != "y" and response.lower() != "n":
                print("That is not a valid response.")
                response = input("Would you like to exit?(Y/N) ")
            if response.lower() == "n":
                for x in range(len(engwords)):
                    print(str(x+1)+".",engwords[x])
            else:
                keepdisplaying = False
                print("Thank you for using the program!")
                print("Keep working on your French!")
    else:
        print("Sorry. That is not the correct answer.")
        response = input("Would you like to exit?(Y/N) ")
        while response.lower() != "y" and response.lower() != "n":
            print("That is not a valid response.")
            response = input("Would you like to exit?(Y/N) ")
        if response.lower() == "n":
            for x in range(len(engwords)):
                print(str(x+1)+".",engwords[x])  
        else:
            print("Thank you for using the program!")
            print("Keep working on your French!")
            keepdisplaying = False


        
        

        
    


