def to_base(n, base):
    # các ký tự cho cơ số tới 36
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"
    res = ""
    while n > 0:
        res = digits[n % base] + res
        n //= base
    return res

# ví dụ:
num = 12345
for b in range(2, 37):
    print(f"base {b}: {to_base(num, b)}")
