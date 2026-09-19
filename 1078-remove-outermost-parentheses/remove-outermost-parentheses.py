class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        level = 0
        for ch in s:
            if ch == '(' and level>0:
                res.append(ch)
                level+=1
            elif ch==')' and level>1:
                res.append(ch)
                level-=1
            elif ch=='(':
                level+=1
            elif ch==')':
                level-=1
        return "".join(res)