# def status-valido(int status){
#    while (type(status) != "integer"):
#    print("Status inválido, digite um número valido.")
#    return status
#    }
forca = 0
while (type(forca) != 'int'):
    forca = int(input('STR: '))
    print("Status inválido, digite um número válido.")
destreza = int(input('DEX: '))
inteligencia = input('INT: ')
vitalidade = int(input('VIT: '))
carisma = input('CHR: ')
velocidade = int((vitalidade+destreza)/4)

print('\nPV: {}'.format(forca))
print('VNT: {}'.format(inteligencia))
print('PER: {}'.format(inteligencia))
print('STM: {}'.format(vitalidade))
print('VEL: {}'.format((vitalidade+destreza)/4))
print('ESQ: {}'.format((velocidade+3)))
