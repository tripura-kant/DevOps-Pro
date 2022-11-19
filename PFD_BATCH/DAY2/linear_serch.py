list_of_env = ["qa","dev","test","prod"]

key = "tedst"

is_found = False
for env in list_of_env:
    if env == key:
        is_found = True


if is_found:
    print("Found")
else:
    print("na mila")

