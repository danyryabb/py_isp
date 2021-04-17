def is_number(num):
    try:
        float(num)
    except ValueError:
        return False
    return True


def my_range(_from_, _to_, step = 1):
    if is_number(_from_) and is_number(_to_) and is_number(step):
        while (_from_ < _to_):
            yield _from_
            _from_ += step
    else:
        pass
    return

print(list(my_range(2,10,2)))
