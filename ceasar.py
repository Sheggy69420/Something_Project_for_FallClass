word = "ABC"
encoded = ""
decoded = ""

for letter in word:
    encoded += chr(ord(letter) + 1)

for letter in encoded:
    decoded += chr(ord(letter) - 1)

print("Encoded:", encoded)
print("Decoded:", decoded)
