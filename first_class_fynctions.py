
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find element {expected}")


friends = [
    {"name": "Bob Rock", "age": 24},
    {"name": "Jack Daniels", "age": 25},
    {"name": "Stew A", "age": 26}]


# def get_name(friend):
#     return friend["name"]


# print(search(friends, "Bob Rock", get_name))

print(search(friends, "Bob Rock", lambda friend: friend["name"]))
