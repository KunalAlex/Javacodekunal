
k = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = sum(1 for char in k if char in vowels)
consonant_count = sum(1 for char in k if char.isalpha() and char not in vowels)
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
print("Vowel and consonant count completed.")
# This code counts the number of vowels and consonants in a given string.

