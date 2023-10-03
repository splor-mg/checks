from babel.numbers import format_currency

def pp(x):
    return format_currency(x, "BRL", locale="pt_BR")
