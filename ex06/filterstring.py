import sys
from ft_filter import ft_filter
def main():
    f = lambda s,N:len(s) > N
    n = len(sys.argv)
    try:
        l = int(sys.argv[2])
        print(ft_filter(lambda s:f(s,l),sys.argv[1].split(' ')))
    except ValueError:
        print("AssertionError: the arguments are bad")
if __name__ == "__main__":
    main()

