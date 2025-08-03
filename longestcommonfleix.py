def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]  # cắt dần đi từ cuối
            if not prefix:
                return ""
    
    return prefix
print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"