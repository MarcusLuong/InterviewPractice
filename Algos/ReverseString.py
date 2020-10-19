def reverseString(self, s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    a = 0
    b = 0 
    for i in range(len(s)/2):
        
        a = s.pop(i)

        b = s.pop(len(s)-i-1)

        s.insert(i, b)
        s.insert(len(s)-i, a)

    return s