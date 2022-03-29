def is_whol_number(number):
    if (number % 1 ==0) and (number > 0):
        return True

    return False


s=0

def main():
    my_number = 5.4
    get_is_whole_number = is_whol_number(my_number)
    print(get_is_whole_number)

if __name__ == '__main__':
    main()