"""
04.252.011/0001-10  40.688.134/0001-61  71.506.168/0001-11  12.544.992/0001-05

0  4  2  5  2  0  1  1  0  0  0  1  X  X
5  4  3  2  9  8  7  6  5  4  3  2
0  16 6  10 18 0  7  6  0  0  0  2 = 65##
Fórmula -> 11 - (65 % 11) = 1
Primeiro dígito = 1

0  4  2  5  2  0  1  1  0  0  0  1  1  X
6  5  4  3  2  9  8  7  6  5  4  3  2
0  20 8  15 4  0  8  7  0  0  0  3  2 = 67
(Fórmula -> 11 - (67 % 11) = 11 (como resultado > 9 então é 0)
Segundo dígito = 0

testado novo cnpj + digitos = 04.252.011/0001-10
cnpj original               = 04.252.011/0001-10
VÁLIDO

"""

import cnpj

cnpj1 = '40.688.134/0001-61'
if cnpj.valida(cnpj1):
    print(f'{cnpj1} é válido')
else:
    print(f'{cnpj1} NÃO é válido')
