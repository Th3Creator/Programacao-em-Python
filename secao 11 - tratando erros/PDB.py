"""

PDB -> Python Debugger

Bug -> Inseto 

Debugger -> Remover o inseto
"""


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f"Ocorreu um problema do tipo: {err}"

print(dividir(4,2))