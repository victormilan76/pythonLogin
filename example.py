'''
https://www.w3schools.com/python/python_strings_methods.asp

Esto es un ejemplo con las funciones 
mas usadas en phyton Wellcome 
'''

#mensaje por pantalla string
'''
message = "Desarrollo de Login"
print(message)
'''

#operaciones matematicas int
'''
number1 = 10
number2 = 2
result = (number1 + number2)+9
print(number1+number2)
print(number1-number2)
print(number1*number2)
print(number1/number2)
print(result)
'''

#operadores de comparacion
'''
print(3 > 7) # false
print(7 >= 3) # true
print(7 == 7) # true
print(7 != 6) # true
print('Milan' == 'Milan') #true
print('Milan' == 'MILAN') #false (sencible)
'''

#operadores de comparacion
'''
stok = input('Ingrese un numero')
stok = int(stok)
print(stok>=5 and stok<=10) 
role = input('Digita el rol =>')
print(role == 'admin' or role == 'seller')
'''

#operador logico not
'''
print(not True)
print(not False)
print ('=>', not (False and False))
print (not (True and True))
'''

#condicionales
'''
if True:
    print('verdad')

dog = input('Cual es tu mascota favorita?')
if dog == 'perro':
    print('tienes buen gusto')
if dog == 'gato':
    print('no es de mi gusto')

stock = int(input('Digita el stock'))
if stock >= 100 and stock <= 1000 :
   print('El stok es correcto')
else:
   print('el stok es incorrecto')
'''

#string recargado
'''
text = 'Ella sabe programar en Python'
text = 'JS'
if 'JS' in text:
    print('Este es un texto')
else:
    print('Caso contrario') 
size = len(text) #tamaño de una cadena
print(size)
print(text.upper()) #mayuscula para conversion
print(text.lower()) #minuscula para conversion
print(text.count('a')) #contar las letras en una cadena
print(text.startswith('Ella')) #busca el comodin de la palabra
print(text.replace('J','GO')) # remplaza palabras

print(text.isdigit())
print("45".isdigit()) #valida si es digito
'''

#indexing
'''
text = "El sabe Phyton" #detecta la letra segun la posicion
print(text[1])
size = len(text)
print(text[size-1])
print(text[3:7])
print(text[5:-1])
print(text[:])
print(text[1:6:2])
print(text[::2])
'''

#listas
'''
numbers = [1,2,3,4]
print(numbers)
print(type(numbers))
cadena = ['victor','milan']
print(cadena)
print(cadena[0])
t = [1,True,'hola']
print(t)
'''

#metodos CRUD 
'''
numbers = [1,2,3,4,5]
print(numbers)
numbers[-1] = 10
print(numbers)
numbers.insert(0,'hola')
print(numbers)
task = ['todo 1','todo 2','todo 3']
new_list = numbers + task
print(new_list)
new_list.remove('todo 1')
print(new_list)
new_list.pop #elimina el ultimo elemento
print(new_list)
new_list.reverse() # invierte la lista
print(new_list)
numbers2 = [1,2,5,4,3]
numbers2.sort()
print(numbers2)
'''

#




#piedra papel o tijera
'''
import random
options = ('piedra', 'papel', 'tijera')
computer_wins = 0
user_wins = 0

rounds = 1

while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    rounds += 1

    if not user_option in options:
      print('esa opcion no es valida')
      continue  

    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('user gano!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('user gano')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('user gano!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('computer gano!')
            computer_wins += 1

    if computer_wins == 2:
      print('El ganador es la computadora')
      break

    if user_wins == 2:
      print('El ganador es el usuario')
      break
'''

