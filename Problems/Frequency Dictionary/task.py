inp_words = [w.lower() for w in input().split()]
res = {}
for w in inp_words:
    res[w] = res.get(w, 0) + 1

print("\n".join(f"{key} {value}" for key, value in res.items()))
