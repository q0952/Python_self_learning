def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

# print(first(x))
# print(last(x))
# print(middle(x))

def is_palindrome(word):
    if word==word[::-1]:
        print("Yes,", x, "is a palindrome.")
    else:
        print("No,", x, "is not a palindrome.")

x=str(input('Enter a word: '))
is_palindrome(x)