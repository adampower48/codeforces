word = input().lower()

for vowel in ['a', 'e', 'i', 'o', 'u', 'y']:
    if vowel in word:
        word = word.replace(vowel, '')

# print(word)

newWord = ""
for letter in word:
    newWord += "." + letter

print(newWord)
