# Crie uma variável chamada val1 e atribua o valor 12
# Crie uma variável chamada val2 e atribua o valor 3.75
# Crie uma variável chamada texto e atribua o valor O valor da soma é:
# Imprima o tipo da variável val1
# Imprima o tipo da variável val2
# Imprima o tipo da variável texto
# Crie uma variável chamada soma e atribua a soma de val1 e val2
# Imprima o tipo da variável soma
# Imprima a variável texto juntamente com a variável soma
val1 = 12
val2 = 3.75
texto = 'a soma é:'
print(val1)
print(val2)
print(texto)
soma = val1 + val2
print(type(soma))
print(texto, soma)



# Escreva um programa que inicialize uma variável com o valor 32 para representar a temperatura em Celsius.
# Em seguida, converta esse valor em Fahrenheit usando a fórmula F = 1.8C + 32.
# Imprima o valor Fahrenheit.
var1 = 32
f = (1.8 * var1) + 3
print(f)



# Escreveva um script que converta uma quantidade inteira de minutos em seu respectivo valor dado em horas e minutos.
# O resultado do seu script deve ser da seguinte forma:
# Horas: x
# Minutos: y
# Por exemplo, o resultado da conversão de 132 minutos deve ser:
# Horas: 2
# Minutos: 12
digitado = 132
h = int(digitado / 60)
m = int(digitado - h * 60)
s = int(round(digitado % 1 * 60))
print(h)
print(m)
print(s)



# Crie um programa que avalia se um número entre 1 e 5, fornecido pelo usuário, é um número primo
# (quando ele é divisivel por 1 e por ele mesmo)
num = int(input('VEJA SE O NUMERO É PRIMO:'))
if num >=1  and num <= 5:
  if num % 1 == 0 and num % num == 0:
    print(f'{num}, é primo')
else:
  print(f'{num}, não é primo')



# Crie um programa que receba dois números do usuário e imprima a relação entre eles (iguais, o primeiro maior que o segundo ou o primeiro menor que o segundo)
num1 = input('Digite o primeiro numero: ')
num2 = input('Digite o segundo numero: ')

if num1 == num2:
  print('Eles são iguais')
if num1 > num2:
  print(f'maior: {num1} menor: {num2}')
if num2 > num1:
  print(f'maior: {num2} menor: {num1}')



# Escreva um programa que pede para o usuário acertar o nome de uma fruta em 10 tentativas.
# A cada interação, o programa deve imprimir o número de tentativas e pedir para que o usuário escolha uma fruta. ]
# Caso o usuário acerte a fruta, o programa deve imprimir "Parabéns, você acertou!". Caso o usuário escreva "desisto", o programa deve imprimir "ok, obrigado pela participação". No caso de todas as tentativas se esgotarem, o programa deve imprimir "Suas tentativas acabaram e você não acertou".
import random

frutas = ['abacaxi','melancia']
cpu = random.choice(frutas)

tentativas = 10

while tentativas > 0:
  user = input('Tente advinhar a fruta que eu estou pensando: ')
  if user != cpu:
    print('Não é essa, tenta de novo!')
    tentativas -= 1
    pass

  if user == cpu:
    print('Parabéns, você acertou!')
    break

  if input == 'desisto':
    print('ok, obrigado pela participação')
    break

else:
  print('acabou suas tentativas!')
  print(f'essa foi a fruta escolhida {cpu}')



# Escreva um programa que retorne o fatorial de qualquer número.
# O programa deve receber um número do usuário e imprimir o valor do fatorial, caso o número fornecido seja menor que 0 a seguinte mensagem deve ser retornada:
# "O valor deve ser positivo"
num = int(input('Fala um numero ae: '))
fatorial = 1
if num < 0:
  print('O valor deve ser positivo')
else:
  for x in range(1, num+1):
    fatorial = fatorial * x

print(f'o valor fatorial é {fatorial}')



# Crie um programa que imprima as tabuadas no seguinte formato:
# 1 * 1 =  1
# 1 * 2 =  2
# 1 * 3 =  3
# 1 * 4 =  4
# 1 * 5 =  5
# 1 * 6 =  6
# 1 * 7 =  7
# 1 * 8 =  8
# 1 * 9 =  9
# 1 * 10 =  10
for x in range(9):
  for i in range(11):
    print(f'{x} * {i} = {x * i}')
  print('\n')



#Escreva um programa em criar a tabuada de um número entre 1 e 10 fornecido pelo usuário.
x = int(input('Digite o numero que voce quer a tabuada: '))
for count in range(10):
  resultado = x * (count + 1)
  print(f'{x} * {count + 1} = {resultado}') 
  
  
  
# Nos primeiros dois anos, um ano canino é igual a 10.5 anos humanos. Depois disso, cada ano do cão equivale a 4 anos humanos.
# Crie um programa que pergunte ao usuário a idade do cachorro e retorne a idade do cachorro em anos caninos.
idade = float(input('Digite a idade do cachorro: '))
if idade <= 2:
  print(idade * 10.5)
elif idade > 2:
  print((idade-2) * 4) + 21)
  


# Crie um programa que, baseado na idade do usuário, indica se este pode votar na eleição de 2022 e se o voto é facultativo ou obrigatório.
idade = int(input('Digite sua idade: '))
if idade >= 18:
  print('Voto obrigatorio!')
elif idade == 16 or idade == 17:
  print('Voto facultativo')
else:
  print('Não precisa votar... ta suave')



# Crie um programa que retorne o útimo dígito de qualquer número inteiro (Dica: Use uma das 3 formas de divisão que existem em Python)
num = input('fala um numero inteiro ae: ')
print(num[-1])



# Escreva um programa para encontrar o maior número de três números do usuário.
num1 = int(input('Digite primeiro numero: '))
num2 = int(input('Digite segundo numero: '))
num3 = int(input('Digite terceiro numero: '))

if num1 > num2 and num1 > num3:
  print(f'Maior numero: {num1}')
if num2 > num1 and num2 > num3:
  print(f'Maior numero: {num2}')
if num3 > num1 and num3 > num2:
  print(f'Maior numero: {num3}')



# Escreva um programa que receba a temperatura em graus Celsius da água e verifica em qual estado de fase a água se encontra
# (considere a pressão ambiente ao nível do mar)

temp = int(input('Digite a temperatura da agua: '))
if temp <= 0:
  print('Está em estado SOLIDO')
if temp >= 100:
  print('Está em estado GASOSO')
else:
  print('Estado em estado LIQUIDO')



# Escreva um programa para verificar se um caractere é vogal ou não.
letra = str(input('Digite uma letra: '))
if letra == 'a' or  letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
  print('é vogal mano')
else:
  print('é consoante')



# Uma empresa decidiu conceder bônus ao funcionário de acordo com os seguintes critérios:

# Periodo de Tempo de Serviço	Bonus
# Mais de 10 anos	10%
# entre 6 e 10 anos (inclusos)	8%
# menos de 6 anos	5%

# Pergunte ao usuário seu salário e anos de serviço e imprima o valor líquido do bônus.
salario = int(input('Digite seu salario: '))
anos = int(input('Digite quantos anos de serviço voce tem: '))

if anos > 10:
  print(f'Seu bonus sera: {salario * 0.1}')
if anos < 6:
  print(f'Seu bonus sera: {salario * 0.05}')
else:
  print(f'Seu bonus sera: {salario * 0.08}')



# Escreva um programa que aceite dois números e operadores matemáticos e execute a operação de acordo.
# Exemplo:
# Digite o primeiro número: 7
# Digite o segundo número: 9
# Digite o operador: +
# Sua resposta é: 16
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
sinal = str(input('Digite a Operação desejada'))

if sinal == '+':
  print(num1 + num2)
if sinal == '-':
  print(num1 - num2)
if sinal == '**':
  print(num1 ** num2)
if sinal == '/':
  print(num1 / num2)
if sinal == '//':
  print(num1 // num2)
if sinal == '*':
  print(num1 * num2)
if sinal == '%':
  print(num1 % num2)


 
#Escreva um programa para verificar se um triângulo é equilátero, isósceles ou escaleno.
# Um triângulo equilátero é um triângulo em que os três lados são iguais.
# Um triângulo escaleno é um triângulo que tem três lados desiguais.
# Um triângulo isósceles é um triângulo com (pelo menos) dois lados iguais. 
plado = input('1°: ')
slado = input('2°: ')
tlado = input('3°: ')

if plado == slado == tlado:
  print('Triangulo equilátero ')

elif plado != slado != tlado:
  print('Triangulo escaleno')

elif plado == slado or slado == tlado or plado == tlado:
  print('triângulo isósceles')
  
  

# Escreva um programa para jogar jokenpô com o computador.
import random

opcoes = ['papel', 'pedra', 'tesoura']

escolha_computador = random.choice(opcoes)
user = input("Escolha entre: papel, pedra, tesoura \n")

if user == "papel" or user == 'pedra' or user == 'tesoura':
  if user == "papel" and escolha_computador == "tesoura":
    print( "Voce perdeu")
  elif user == 'pedra' and escolha_computador == "papel":
    print("Voce perdeu")
  elif user == "tesoura" and escolha_computador == "pedra":
    print("Voce perdeu")
  else:
    print("ganhou")
print("o cpu escolheu:", escolha_computador)


