def palindrome():
    word = str(input("Pick a word: "))
    reverse = word[::-1]
    if word == reverse:
        print(f"{word} is a Palindrome!")
    else:
        print(f"{word} is Not a Palindrome!")


# palindrome()

#another way

# word = input("Please enter  word: ")
# reversed_word = ""
# for index in range(len(word) -1,-1,-1):
#     #reversed_word = reversed_word + word[index]
#     reversed_word += word[index]
# if word == reversed_word:
#     print("PALINDROME")
# else:
#     print("Not a palindrome")
