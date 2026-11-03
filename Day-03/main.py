# print("===== TEXT ANALYZER =====")

# text = input("Enter a sentence: ")

# print("\n===== ANALYSIS =====")

# print("Original text:", text)

# print("Uppercase:", text.upper())

# print("Lowercase:", text.lower())

# print("Total characters:", len(text))

# print("Total words:", len(text.split()))

# print("Reversed text:", text[::-1])

# print("First character:", text[0] if text else "None")

# print("Last character:", text[-1] if text else "None")

# print("Title format:", text.title())

# print("Clean text:", text.strip())




text = input("enter text: ")

# reverse = text[::-1]

# if text == reverse :
#     print("palindrom")
# else:
#     print("not palindrom")

countvo = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')

print(countvo)

print(len(text.split()))


