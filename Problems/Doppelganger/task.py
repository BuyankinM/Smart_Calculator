# the object_list has already been defined
# write your code here

from collections.abc import Hashable

hashes = {}
for obj in object_list:
    if isinstance(obj, Hashable):
        hashes[hash(obj)] = hashes.get(hash(obj), 0) + 1

print(sum(value for value in hashes.values() if value > 1))