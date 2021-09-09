def is_palindrome(s):
    for i in range(len(s)//2):
        sym = len(s) - i - 1
        if s[i] != s[sym]:
            return False
    return True


while(True):
    s = input()
    if s == "0":
        break
    
    if is_palindrome(s):
        print("yes")
    else:
        print("no")

