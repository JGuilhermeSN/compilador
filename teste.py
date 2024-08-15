def contador(inicio, fim, passo=1): # O '=1' faz com que o parametro passo seja opcional, caso nao seja informado, ele ira ser igual a 1
    print("-"*20)
    for i in range(inicio,fim,passo):
        print(i)


inicio = int(input("inicio: "))
fim = int(input("fim: "))
iterador = int(input("iterador: "))

contador(1, 11)
contador(10, -1, -2)
contador(inicio, fim, iterador)
