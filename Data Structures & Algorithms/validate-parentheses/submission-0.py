class Solution:
    def isValid(self, s: str) -> bool:
        par={')':'(', ']':'[', '}':'{'}
        stack=[]
        for p in s:
            if p in par:
                if stack and par[p]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        if not stack:
            return True
        return False