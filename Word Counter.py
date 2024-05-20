'''To create a word counter using pyhton programming language.
   Word Counter is a program that counts the number of words in a given text'''

#Funtion to count the number of words in given text
def counting(text):
    #To split the text into words using blank space as separator 
    words=text.split(' ')
    #Return the number of words using length counting keyword
    return len(words)
#End of counting function

#Main function to take user input and give the desired output
def main():
    #Taking input from user in the form of a sentence or a single paragraph
    n=input("Enter a paragraph or a sentence in which number of words are to be counted : ")
    #Checking for error and error handling: if in case no input is given
    if (n==""):
        print("Error: No input given. Please enter a valid paragraohph or sentence.")
    #If there is no error ie the user has given some input then calculating the number of words
    else:
        #Counting the words in user input
        count=counting(n)
        #Displaying the total number of words in the text ie sentence or paragraph
        print(count)
    #End of main function

#Ensuring that the code runs only if it is executed directly and not when imported as a module
if __name__=="__main__":
    #Calling the main function if rhe script is executed directly
    main()