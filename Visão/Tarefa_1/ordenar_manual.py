def main():

    lista = []
    lista.append(input("Digite um numero:"))
    lista.append(input("Digite um numero:"))
    lista.append(input("Digite um numero:"))
    lista.append(input("Digite um numero:"))



    for i in range(1,4) :
        for j in range(1,4):
            if lista[j] < lista[j-1]:
                aux = lista[j-1]
                lista[j-1] = lista[j]
                lista[j] = aux

    print(lista)
if __name__ == "__main__":
    main()