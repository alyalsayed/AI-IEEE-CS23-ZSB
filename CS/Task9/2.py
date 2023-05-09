#125. Valid Palindrome
#https://leetcode.com/problems/valid-palindrome/description/
# solving using regex 
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]