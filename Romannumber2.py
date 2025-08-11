def romanToInt(s: str) -> int:
    roman = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }

    total = 0
    prev = 0
    for c in reversed(s):
        val = roman[c]
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total
print(romanToInt("MCMXCIV"))  # Output: 1994