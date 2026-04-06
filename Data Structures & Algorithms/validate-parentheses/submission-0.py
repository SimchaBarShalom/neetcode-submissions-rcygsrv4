class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                c = stack.pop()
                if c == '(' and s[i] != ')' or c == '[' and s[i] != ']' or c == '{' and s[i] != '}':
                    return False 
        return len(stack) == 0