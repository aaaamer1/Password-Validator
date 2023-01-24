# Password Validate
import random

def validate(password):
    """ Analyzes an input password to determine if it is "Secure", "Insecure", or "Invalid" based on the assignment description criteria.

    Arguments:
        password (string): a string of characters


    Returns:
        result (string): either "Secure", "Insecure", or "Invalid". 
    """

    special_characters = "!-$%&'()*+,./:;<=>?_[]^`{|}~"

    if len(password) < 8 or " " in password or "@" in password or "#" in password:
            password = "Invalid"
        
    else:
        r1=False
        r2=False
        r3=False
        r4=False
        for i in password:
            if i.isupper():
                r1=True
            if i.islower():
                r2=True
            if i.isnumeric():
                r3=True
            for special_char in special_characters:
                if special_char in password:
                    r4=True

        if r1 and r2 and r3 and r4:
            password = "Secure"

        else:
            password = "Insecure"

        
    return password


def generate(n): 
    #Choosing how many times a character type occurs
    charsLeft = n 
    smallCharNum = random.randint(1,charsLeft-3) 
    charsLeft -= smallCharNum 
    bigCharNum = random.randint(1,charsLeft-2) 
    charsLeft -= bigCharNum 
    digitCharNum = random.randint(1,charsLeft-1) 
    charsLeft -= digitCharNum 
    specialCharNum = charsLeft

    #Character dictionary
    charDict = {"smallChar":smallCharNum, "bigChar":bigCharNum, "digitChar":digitCharNum, "specialChar":specialCharNum}
    password = ""

    #Defining set of characters within each character type
    charSpace = {"smallChar":"abcdefghijklmnopqrstuvwxyz", "bigChar":"abcdefghijklmnopqrstuvwxyz".upper(), "digitChar":"1234567890", "specialChar":"!-$%&'()*+,./:;<=>?_[]^`{|}~"}
    lst = ["smallChar", "bigChar", "digitChar", "specialChar"]

    #Use while loop to create the password randomly
    while len(password) < n:
        entry = ""
        while entry == "":
            entryType = random.choice(lst)		    # Choose character type
            while charDict[entryType] == 0:		    # While (if) character type has no more space
                entryType = random.choice(lst)	    # Choose character type
            charDict[entryType] -= 1			    # Decrease the number of the chosen character type by one
            entry = random.choice(charSpace[entryType])
        password += entry

    
    return password

if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This can be useful for
    # testing your implementations.
    pass

