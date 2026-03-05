text = input("Enter text: ")

i= j =k=0

for ch in text:
    if ch.isalpha():
        i += 1
    elif ch.isalnum():
        j += 1
    else:
        k += 1

print("Alphabets:", i)
print("Numbers:", j)
print("Special characters:", k)