def isPalindrome(a):
    """
        Checks if string 'a' is a palindrome or not
        Returns True if yes
        Returns False if no
    """
    if a == a[::-1]:
        return True
    else:
        return False

a = "rabarbar"

print(isPalindrome(a))
