def romanToInt(s: str) -> int:
    vals = [0] * 26
    vals[ord('I') - 65] = 1
    vals[ord('V') - 65] = 5
    vals[ord('X') - 65] = 10
    vals[ord('L') - 65] = 50
    vals[ord('C') - 65] = 100
    vals[ord('D') - 65] = 500
    vals[ord('M') - 65] = 1000

    total = prev = 0
    for c in reversed(s):
        val = vals[ord(c) - 65]
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total
print(romanToInt("MCMXCIV"))  # Output: 1994