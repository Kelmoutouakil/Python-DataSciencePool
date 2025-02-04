import sys

def main():
    NESTED_MORSE= {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',      
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',   
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',    
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',   'T': '-',      
    'U': '..-',    'V': '...-',  'W': '.--',    'X': '-..-',   'Y': '-.--',   
    'Z': '--..',   
    '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-', '5': '.....', 
    '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.', '0': '-----',  
    ' ': '/'
}

    n = len(sys.argv)
    if n == 2:
        if sys.argv[1]!= '' and all(c.isalnum() or c.isspace() for c in sys.argv[1]):
            for c in sys.argv[1]:
               print(NESTED_MORSE[c.upper()],end=' ')
        else:
            print("AssertionError: the arguments are bad")
    else:
        print("AssertionError: the arguments are bad")   
if __name__ == "__main__":
    main()