class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        forwards = []

        for char in string.strip():
            if char.isalnum() and char != "":
                forwards.append(char)

        backwards = list(reversed(forwards))


        return (forwards == backwards)
        