ranks_dict = {str(d): d for d in range(2, 11)}
ranks_dict["Jack"] = 11
ranks_dict["Queen"] = 12
ranks_dict["King"] = 13
ranks_dict["Ace"] = 14

n = 6
s = 0
for _ in range(n):
    s += ranks_dict[input()]

print(s / n)