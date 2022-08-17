# Ike Ven Louie Anicete
# John Andrei Lapid
#CS - 201


def naive(str, substr):  # str stands for the text and substr stands for the word
    if substr in str:  # if the word is in the text
        # using the find function in python, find the position of the word within the text
        j = str.find(substr)
        while(j != -1):  # search till the end of the text
            # print at which positions was the word found
            print("Word found at position", j)
            # increment j whenever we find the word inside the text
            j = str.find(substr, j+1)

    else:
        print("Error: Word not in Text.")

# initialize main function to run the program


def main():
    # ask for the user input on the word and text
    text = input('Enter the text you wish to use: ').lower()
    # convert both to lowercase in order to match the string even if some are in uppercase
    word = input('Enter the word you wish to find: ').lower()
    naive(text, word)  # use the naive algorithm on the inputs


main()  # run the main program
