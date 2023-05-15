print("Comienza el Juego")
a= int(input("estas en una carcel y te acusan de un crimen que no cometiste, tienes que tomar una decisión, \n 1. esperar al juicio \n 2. intentar descapar \n"))

if a==2:
    b= int(input("Tienes derecho a una llamada, ¿A quien llamas? \n 1.Tu novia \n 2. Tu mejor amigo\n"))
    if b==2:
        c= int (input("tu amigo accede a ayudarte a escapar, te llevara un pastel \n ¿Que quieres que te lleve dentro del pastel? \n 1. un arma \n 2. una lima \n 3. un brebaje magico \n"))
        if c==1:
            d= int (input("logras ingresar el arma a tu celda. \n ¿Que haras? \n 1. dispararle al guardia \n 2. amenazar al guardia con el arma\n"))
            if d==2: 
                e=int(input("Consiges que el guardia te deje salir de la celda. Encuentras dos pasillos ¿Cual eliges? \n 1. Derecho \2.Izquierdo\n"))
                if e==1:
                    f=int(input("Te encuentras dos opciones \n 1. salir por una alcantarilla \n 2. Salir por una regilla de ventilacion\n"))
                    if f==2:
                        g=int(input("tienes dos caminos, ¿Cual de los dos eliges? \n 1. Derecha \n 2. Izquierda\n"))
                        if g==1:
                            h=int(input("Logras salir a la terraza de la prision, debes buscar una forma de bajar\n Tienes 3 opciones para salir de ahi, ¿Cual eliges? \n 1. Coger un paracaidas para saltar \n 2. Bajar por las escaleras \n 3. Bajar deslizandote por una soga\n"))
                            if h==3:
                                print("Lograste escapar, felicitaciones!!")
                                print ("Ganaste el juego")
                            elif h==1:
                                print ("El paracaidas estaba descompuesto, no abre, caes y mueres.")
                                print("Fin del juego, perdiste")
                            elif h==2:
                                print("Al bajar por las escaleras te ve uno de los guardias y te capturan ")
                                print("Fin del juego, perdiste")
                        elif g==2:
                            print("Hay un precipicio, caes y mueres")
                            print("Fin del juego, perdiste")
                    elif f==1:
                        print("Caes a un pozo, y te ahogas porque no sabes nadar")
                        print("Fin del juego, perdiste")

                elif e==2:
                    print("Hay mas guardias y te detienen de nuevo")
                    print("Fin del juego, perdiste")
            elif d==1:
                print("Llegan refuerzos y terminan asesinandote.")
                print("Fin del juego, perdiste")
        elif c==2:
            z=int(input("¿Que vas a limar\n 1. Los barrotes de la ventana \n 2. Los barrotes de la puerta\n"))
            if z==2:
                g=int(input("te encuentas con dos policias, logras entrar a un cuarto de limpieza, en la cual hay una regilla de ventilacion y te metes alli\n tienes dos caminos ¿Cual de los dos eliges \n 1. Derecha 2. Izquierda\n"))
            elif z==1:
                print("sales por la ventana pero estas en un decimo piso y mueres al caer")
                print("Fin del juego, perdiste")


        elif c==3:
            print("Te tomas el brebaje y tienes el poder de super fuerza. con, con la cual rompes el muro y puedes salir de la celda. sin embargo dura solo unos minutos y al finalizar te capturan de nuevo ")

    elif b==1:
        print("Tu novia no te contesta, y pierdes la unica llamada que tenias")
        print("Fin del juego, perdiste")


    
elif a==1:
    print("te declaran culpable, y te sentencian a cadena perpetua")
    print("Fin del juego, perdiste")
    