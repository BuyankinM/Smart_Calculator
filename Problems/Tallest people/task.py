def tallest_people(**kwargs):
    max_height = max(kwargs.values())
    tallest_list = [(name, height) for name, height in kwargs.items() if height == max_height]
    for name, height in sorted(tallest_list):
        print(f"{name} : {height}")