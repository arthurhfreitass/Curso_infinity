def maior_numero(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(maior_numero(10, 25, 17))  # Saída: 25
