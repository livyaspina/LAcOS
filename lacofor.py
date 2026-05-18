for c in range(0,20):
    print("TE AMO AMORZÃO")
    
############################

for c in range(11, 0, -1): #conta ao contrário
    print(c)
    
############################   

s = 0
for c in range(0, 3): #digite 3x um valor 
    d = int(input("Informe um valor: ")) #soma dos valores 
    s += d
print("O somatório dos valores são: {}". format(s))

############################

n = int(input("Digite um número: ")) # contagem 
for c in range(1, n+1):
    print(c)
    
############################

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('passo: '))

for c in range(i, f+1 , p):
    print(c)
    
############################
    

for par in range(0, 51,):
    if par % 2 == 0:
        print(par, end=' ')
print('Acabou')

############################

soma = 0
total = 0
for n in range (1, 501, 2):
    if n % 3 == 0:
        total = total + 1 # contador 
        soma = soma + n #acumulador
print('A soma de todos os {} valores é de {}'.format(total ,soma))

############################

soma = 0 #acumulador
for n in range(1, 7):
    number = int(input('Informe o {}° número: '.format(n)))
    if number % 2 == 0:
        soma += number
print('O valor total dos seis números informados é de: {}'.format(soma))
