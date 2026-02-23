
def reverse_string(num):
    ans = ""
    for ch in num:
        ans = ch + ans
    return ans

name = input("enter the number:")
result = reverse_string(name)
print(result)