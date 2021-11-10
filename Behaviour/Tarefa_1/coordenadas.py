def main():

    print("Tamanho do plano cartesiano em x vai de -500 a 500")
    print("Tamanho do plano cartesiano em y vai de -500 a 500")
    print("Defina as coordenadas")
    x = int(input("Coordenada x: "))
    y = int(input("Coordenada y: "))

    print("coordenada (",x,",",y,")")

    if x > 500 or y > 500 or x < -500 or y < -500:
        print("As coordenadas está fora do plano cartesiano")
        exit()
    else:
        if x <= 500 and x > 0:
            x_sit = "direita"
        elif x < 0 and x >= -500:
            x_sit = "esquerda"
        elif x == 0:
            x_sit = 0
        
        if y <= 500 and y > 0:
            y_sit = "emcima"
        elif y < 0 and y >= -500:
            y_sit = "embaixo"
        elif y == 0:
            y_sit = 0
    
    if y_sit == 0 and x_sit == 0:
        print("O ponto está no centro do plano cartesiano")
    elif y_sit == 0:
        print("O ponto está a", x_sit, "no plano cartesiano")
    elif x_sit == 0:
        print("O ponto está", y_sit, "no plano cartesiano")
    else:
        print("O ponto está a",x_sit, "e", y_sit, "no plano cartesiano")



if __name__ == "__main__":
    main()