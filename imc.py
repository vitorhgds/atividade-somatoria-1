print('imc(indice de massa corporal=será que seu peso)')
nome=input('nome de usuario:')
peso=float(input('qual o seu pesso:'))
altura=float(input('qual o seu peso:'))
imc=peso/(altura**2)
if imc <=18.5:
    print('abaixo do pesso')
elif imc <=24.9:
    print('pessso normal')
elif imc>=29.9:
    print('sobrepeso')
elif imc>=34.9:
    print('obesidade grau 1')
elif imc >=39.9:
    print('obesidade grau 2 ')
elif imc >=40.0:
    print('obesidade grau 3 (mórbida)')