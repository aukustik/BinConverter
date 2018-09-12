from converter import *

print('Input number:')
kek = input()
print('DtB or BtD?:')
case = {
    'dtb': ToBin(kek),
    'btd': ToDec(kek)
}
input_data = input()
kekCon = case[input_data]
kekCon.convert()