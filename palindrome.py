class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False  # Số âm không thể là palindrome

        div = 1
        while x // div >= 10:
            div *= 10

        while x:
            left = x // div       # chữ số đầu tiên
            right = x % 10        # chữ số cuối cùng
            if left != right:
                return False

            x = (x % div) // 10   # loại bỏ chữ số đầu và cuối
            div = div // 100      # chia cho 100 vì bỏ 2 chữ số

        return True
print(Solution().isPalindrome(121))  # True