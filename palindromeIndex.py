def palindromeIndex(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            if s[i + 1:len(s) - i] == s[i + 1:len(s) - i][::-1]:
                return i
            elif s[i:len(s) - i - 1] == s[i:len(s) - i - 1][::-1]:
                return len(s) - i - 1
    return -1


def palindromeIndex(s):
    # Helper function to check if a string is a palindrome
    def is_palindrome(substring):
        return substring == substring[::-1]
    
    # Use two pointers to check for palindrome property
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Check if removing the left character makes it a palindrome
            if is_palindrome(s[left + 1:right + 1]):
                return left
            # Check if removing the right character makes it a palindrome
            elif is_palindrome(s[left:right]):
                return right
            else:
                return -1
        left += 1
        right -= 1
    
    # If already a palindrome, return -1
    return -1


