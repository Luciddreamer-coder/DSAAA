#Normal solution with o(logn) tc and o(1) sc

def Palindrome(x):
    if x<0:
        return False
    original = x    
    reversed = 0
    while x>0:
        reversed = reversed * 10 + x %10
        x= x// 10
    print(reversed)
    return original == reversed

# Using class
class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        original = x
        reversed = 0
        while x>0:
            reversed = reversed * 10 + x %10
            x= x// 10
        print(reversed)
        return original == reversed
test = Solution()
print(test.isPalindrome(121))    


#print(Palindrome(121))