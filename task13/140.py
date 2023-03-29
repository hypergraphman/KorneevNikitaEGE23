g = {
    'A': 'BC',
    'I': 'AE',
    'H': 'IFG',
    'K': 'F',
    'B': 'CK',
    'C': 'E',
    'E': 'DH',
    'D': 'BCF',
    'F': 'E',
    'G': 'FI',
}


def f(v, p):
    if len(p) > 1 and p[0] == p[-1]:
        return 1
    if len(p) > len(set(p)):
        return 0
    return sum(f(x, p + x) for x in g[v])


print(f('E', 'E'))