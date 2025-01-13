import sys
from string import punctuation

def CountString(s:str):
    print("The text contains ",len(s)," characters:")
    upper = 0
    lower = 0
    digit = 0
    space = 0
    punct = 0
    for i in range(len(s)):
        if s[i].isupper():
            upper += 1
        elif s[i].islower():
            lower +=1
        elif s[i].isdigit():
            digit+= 1
        elif s[i].isspace():
            space +=1
        elif s[i] in punctuation:
            punct+=1
    print(upper," upper letters")
    print(lower," lower letters")
    print(punct," punctuation marks")
    print(space," spaces")
    print(digit, " digits")


def main():
    n = len(sys.argv)
    if n > 2:
        print("AssertionError: argument is not an integer")
    elif n == 2:
        CountString(sys.argv[1])
    else:
        print("What is the text to count?")
        try:
            text = input()
            CountString(text)
        except EOFError:
            print("Have a Good Day!")
            
if __name__ == "__main__":
    main()
