import sys
def main():
    print("Hello there", sys.argv[1])
if __name__ == "__main__":
    main()

# Defines a "repeat" function that takes 2 arguments

def repeat(s, exclaim):
    "Returns a string repeated 3 times, with an optional exclamation mark"
    "If exclaim is true, add exclamation marks"

    result = s * 3
    if exclaim:
        result = result + '!!!'
    return result

repeat("crackers")