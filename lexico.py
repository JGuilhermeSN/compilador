#abertura de arquivo fonte
print("abre arquivo")
print("="*20)
file = open("arqvteste.txt","r")
openfile = file.read().lower()


i = 0 #posiçao inicial do cursor

def __q7(caracter):
    global i
    if caracter == ' ':
        print(f'i: {i}')
        print("palavra reconhecida: program")
        i+=1
        #__q8(openfile[i])
    else:
        print("erro no q7")

def __q6(caracter):
    global i
    if caracter == 'm':
        print(f'i: {i}')
        print(f'reconheceu: {caracter}')
        i+=1
        __q7(openfile[i])
    else:
        print("erro no q6")

def __q5(caracter):
    global i
    if caracter == 'a':
        print(f'i: {i}')
        print(f'reconheceu: {caracter}')
        i+=1
        __q6(openfile[i])
    else:
        print("erro no q5")

def __q4(caracter):
    global i
    if caracter == 'r':
        print(f'i: {i}')
        print(f'reconheceu: {caracter}')
        i+=1
        __q5(openfile[i])
    else:
        print("erro no q4")

def __q3(caracter):
    global i
    if caracter == 'g':
        print(f'i: {i}')
        print(f'reconheceu: {caracter}')
        i+=1
        __q4(openfile[i])
    else:
        print("erro no q3")

def __q2(caracter):
    global i
    if caracter == 'o':
        print(f'i: {i}')
        print(f'reconheceu: {caracter}')
        i+=1
        __q3(openfile[i])
    else:
        print("erro no q2")

def __q1(caracter):
    global i
    if caracter == 'r':
        print(f'i: {i}')
        print(f'reconheceu: {caracter}')
        i+=1
        __q2(openfile[i])
    else:
        print("erro no q1")

def __q0(caracter):
    global i
    if caracter == 'p':
        print(f'i: {i}')
        print(f'reconheceu: {caracter}')
        i+=1
        __q1(openfile[i])
    else:
        print("erro no q0")

# chama a funçao q0
__q0(openfile[i])
print("="*20)
print("fecha arquivo")
file.close()