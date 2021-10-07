names = ["Sean", "Tommy", "Nikhil", "Brynn"]


def crowd_test(array):
    if len(array) > 3:
        print("This room is too crowded!")


crowd_test(names)
names.remove("Sean")
names.remove("Nikhil")
crowd_test(names)
