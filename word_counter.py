with open("sample.txt", "r") as file:
    text = file.read()

words = text.split()
lines = text.splitlines()
characters = len(text)

print("Number of words:", len(words))
print("Number of lines:", len(lines))
print("Number of characters:", characters)