#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    length = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except (ValueError, TypeError):
            print("wrong type")
            div = 0
        except (ZeroDivisionError, FloatingPointError):
            print("division by 0")
            div = 0
        except (IndexError):
            print("out of range")
            div = 0
        finally:
            length.append(div)
    return (length)
