class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()  # 👈 Pop luôn và gán vào top
                if (c == ')' and top != '(') or \
                   (c == ']' and top != '[') or \
                   (c == '}' and top != '{'):
                    return False
        return not stack  # 👈 Trả về True nếu stack rỗng hoàn toàn
print(Solution().isValid("()"))         # ✅ True
print(Solution().isValid("({[]})"))     # ✅ True
print(Solution().isValid("([)]"))       # ❌ False
print(Solution().isValid("((("))        # ❌ False
print(Solution().isValid(""))           # ✅ True

