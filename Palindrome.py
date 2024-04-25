def is_palindrome(word):
    word = word.lower().replace(" "," ")
    return word == word[::-1]

def reverse_ans():
    word = input("Enter a word or pharse: ")
    if is_palindrome(word):
      print("It is a plaindrome")
    
    else:
       print("It's not palindrome.")

reverse_ans()
       