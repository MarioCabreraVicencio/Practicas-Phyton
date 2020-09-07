# Elimina los multiplos de un numero en la lista del abecedario
abcd = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# print(len(abcd))
for i in range(len(abcd), 1, -1):
    # print(f'es i {i}')
    if i % 3 == 0:
        abcd.pop(i-1)
        # print(f' es i-1 {i-1}')
print(f'{abcd}')
    