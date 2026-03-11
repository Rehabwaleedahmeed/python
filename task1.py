word = input("Enter word: ")
vowels = "aeiouAEIOU"
result = ""
for letter in word:
    if letter not in vowels:
        result += letter
print(result)