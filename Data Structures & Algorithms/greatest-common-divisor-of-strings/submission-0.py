class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Get GCD of the lengths
        gcd_length = math.gcd(len(str1), len(str2))
        
        # Extract candidate string
        candidate = str1[:gcd_length]
        
        # Verify if candidate divides both strings
        # A string divides another if repeating it produces the original
        if (candidate * (len(str1) // gcd_length) == str1 and 
            candidate * (len(str2) // gcd_length) == str2):
            return candidate
        
        return ""