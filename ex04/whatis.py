import sys
n = len(sys.argv)
if n != 2:
    print("AssertionError: more than one argument is provided")
else:
    try:
        int(sys.argv[1])
        if int(sys.argv[1]) % 2== 0:
            print("I 'm Even")
        else:
            print("I'm Odd")
    except ValueError:
        print("AssertionError: argument is not an integer")