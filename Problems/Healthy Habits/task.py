# the list "walks" is already defined
# your code here
len_dist = [info["distance"] for info in walks]
print(round(sum(len_dist) / len(len_dist)))