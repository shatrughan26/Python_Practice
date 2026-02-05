word = input("Enter a word: ")
frequency = {}
for char in word:
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)