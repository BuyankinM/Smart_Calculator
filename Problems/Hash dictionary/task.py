# create your dictionary here
objects_dict = {}
for obj in objects:
    try:
        objects_dict[obj] = hash(obj)
    except TypeError:
        pass
