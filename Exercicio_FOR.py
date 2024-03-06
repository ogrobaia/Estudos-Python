"""
iterável -> str, range, etc (_iter_)
iterador -> quem sabe entregar o valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador

"""

texto = iter('LUIZ') # _iter_()

print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())