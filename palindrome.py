class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Số âm không thể là palindrome, hoặc số tận cùng là 0 nhưng khác 0 (vd: 10)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x = x // 10

        # Với số chẵn: x == reversed_half
        # Với số lẻ: x == reversed_half // 10 (bỏ số giữa)
        return x == reversed_half or x == reversed_half // 10

print(Solution().isPalindrome(121))  # True