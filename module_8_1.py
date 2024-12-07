def add_everything_up(a: str|int|float, b: str|int|float ) -> str|int|float:
    try:
        a + b
    except TypeError:
        return f'{a}{b}'
    return round(a +b, 3)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))