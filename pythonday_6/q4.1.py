#with function(palindrome)
def isPalindrome(str):
    for i in range (0,int(len(str)/2)):
        if str[i]!=str[len(str)-i-1]:
            return False
        return True
pal="madam"
if(isPalindrome(pal)):
    print(F"Yes {pal} is a palindrome")
else:
    print(f"No {pal} is a palindrome")