def solution(n, b):
    
    # Helper function to convert string to decimal
    def to_dec(s):
        power = k-1
        result = 0
        for i in range(k):
            result += b ** power * int(s[i])
            power -= 1
        return result
    
    # Helper function to convert decimal to string
    def to_str(n):
        n = abs(n)
        result = ""
        while n > 0:
            result = str(n%b) + result
            n //= b
            
        prefix = k - len(result)
        return '0' * prefix + result
        
    k = len(n)
    appeared = {}
    i = 0
    while (n not in appeared):
        appeared[n] = i
        x = sorted(n, reverse=True)
        y = x[::-1]
        z = to_dec(x) - to_dec(y)
        n = to_str(z)
        i += 1
    
    return i - appeared[n]
    

print(solution("1211", 10))
