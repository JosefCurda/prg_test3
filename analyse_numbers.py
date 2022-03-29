def is_whol_number(number):
    if (number % 1 ==0) and (number > 0):
        return True

    return False


def is_even_number(number):
    if number % 2 == 1:
        return True
    else:
        return False

s=2

def main():
    my_numbers = [5.4, 5, 10]
    for my_number in my_numbers:
        get_is_whole_number = is_whol_number(my_number)
        print(get_is_whole_number)


if __name__ == '__main__':
    main()