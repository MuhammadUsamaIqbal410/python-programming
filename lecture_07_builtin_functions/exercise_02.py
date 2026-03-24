a = input("Enter the phrase: ")

Sentence = ""
word = a.split()
corrected_sentence = " ".join(word)
vowels = 0
for char in a:
    if char.isalpha() or char == " ":
        corrected_sentence += char

    if char in "aeiouAEIOU":
        vowels +=1
        
print("The phrase is :", corrected_sentence)
print("The total number of vowels in the phrase is:", vowels)
