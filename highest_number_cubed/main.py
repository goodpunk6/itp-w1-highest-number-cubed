"""This is the entry point of the program."""


def highest_number_cubed(limit):
    x = 1
    while (x**3) <= limit:
        x+=1
    else:
        return x-1