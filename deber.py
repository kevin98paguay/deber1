class Deber:
    def __init__(self):
        pass

    def Operaritmeticos(self):
        num1=float(input("1° valor"))
        num2=float(input("2° valor"))
        suma=num1+num2
        resta=num1-num2
        multi=num1*num2
        div=num1/num2
        print("Suma es:{},Resta es:{}, Multiplicación es:{}, Division es:{}".format(suma,resta,multi,div,mod))

    def Operelacionales(self):
        a=float(input("1° valor"))
        b=float(input("2° valor"))
        c=float(input("3° valor"))
        if a<=b:
            print("El 1° valor es menor o igual al 2°")

    def Aritmeticos(self):
        n1=float(input("1° valor"))
        n2=float(input("2° valor"))
        res=(n1/n1+n2)/(n2/n2-n1)
        print("Resultado de la operacion es:",res)

    def Estrucsecuencial(self):
        val=float(input("Ingresar valor total de la compra"))
        des=val*0.15
        total=val-des
        print("El valor total a pagar ya con descuento es:{}".format(total))

    def Selectiva(self):
        not1=float(input("Ingresar nota del alumno"))
        if not1 >=7:
            print("El alumno esta aprobado")
        elif not1 >=5:
            print(("El alumno esta en remedial"))
        else:
            print("El alumno esta reprobado")

    def Sellmultiple(self):
        sue=int(input("Ingresar horas trabajadas"))
        ph=float(input("Ingresar pago por hora normal"))
        if sue>40:
            hex=sue-40
            if hex>8:
                tt=hex-8
                ptot=ph*2*8+ph*3*tt
            else:
                ptot = ph * 40 + ph
        else:
            ptot=sue*ph
        print("El pago total de horas trabajadas es:{}".format(ptot))

    def CiFor(self):
        n=int(input("Ingresar un numero"))
        sum=0
        for i in range(n):
            sum=sum+i*i
        print("La suma de los cuadros de:{} numero es de:{}".format(n,sum))

    def Ciwhile(self):
        numero = int(input("Escriba un número positivo: "))
        while numero < 0:
            print("¡Ha escrito un número negativo! Inténtelo de nuevo")
            numero = int(input("Escriba un número positivo: "))

    def Forani(self):
        n1=int(input("ingresar un numero"))
        for i in range(n1):
            print(f"i (externa) vale {i}")
            n2 = int(input("ingresar segundo numero"))
            for i in range(n2):
                print(f"i (interna) vale {i}")

    def Arrayci(self):
        datos = [0, 0, 0, 0, 0, 0]
        for i in range(1, 7):
            datos[i - 1] = int(input("Dime el dato numero {}: ".format(i)))
        print("Los datos al reves son: ")
        for i in range(6, 0, -1):
            print(datos[i - 1])

objdeber = Deber()
objdeber.Operaritmeticos()
objdeber.Operelacionales()
objdeber.Aritmeticos()
objdeber.Estrucsecuencial()
objdeber.Selectiva()
objdeber.Sellmultiple()
objdeber.CiFor()
objdeber.Ciwhile()
objdeber.Forani()
objdeber.Arrayci()
