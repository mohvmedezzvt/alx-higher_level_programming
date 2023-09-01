#!/usr/bin/python3
def safe_print_division(a, b):
    result = None

    try:
        result = int(a) / int(b)
    except Exception:
        pass
    finally:
        print("Inside result: {}".format(result))

    return result
