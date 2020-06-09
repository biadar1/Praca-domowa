import math
def zadanie1():
    a="Kot"
    b="Ala"
    c=15
    d=20
    e=2.24
    f=6.9
    g=complex (4,1)
    h=complex (7,5)
    print(a)
    print(type(a))
    print(b)
    print(type(b))
    print(c)
    print(type(c))
    print(d)
    print(type(d))
    print(e)
    print(type(e))
    print(f)
    print(type(f))
    print(g)
    print(type(g))
    print(h)
    print(type(h))
def zadanie2():
    a=2
    b=6
    c=3
    dodawanie=a+b
    print(dodawanie)
    odejmowanie=b-a
    print(odejmowanie)
    mnozenie=a*b
    print(mnozenie)
    dzielenie=b/c
    print(dzielenie)
    dzielenie_calkowite=a//b
    print(dzielenie_calkowite)
    reszta=a%b
    print(reszta)
    potega=a**b
    print(potega)
    potega=pow(2,10)
    print(potega)
def zadanie3():
    a=2
    a+=1
    print(a)
    a-=1
    print(a)
    a*=4
    print(a)
    a/=4
    print(a)
    a**=3
    print(a)
    a%=3
    print(a)
def zadanie4():
    print(math.pow(math.e,10))
    print((math.log10(5+(math.sin(8))**2))**(1/6))
    print(math.fabs(3,55))
    print(math.fabs(4,80))
def zadanie5():
    imie="BARTOSZ"
    nazwisko="BIAŁCZAK"
    imie=str.lower(imie)
    imie=str.capitalize(imie)
    nazwisko=str.lower(nazwisko)
    nazwisko=str.capitalize(nazwisko)
    print(imie)
    print(nazwisko)
def zadanie6():
    a="Ania la la la la, piłkę ma la la la..."
    print(a.count("la"))
def zadanie7():
    a="Abrakadabrax"
    print(a[2])
    print(a[-1])
def zadanie8():
    print(str.split("Ania la la la la, piłkę ma la la la..."))
def zadanie9():
    a="Łolaboga czy coś..."
    b=3.4
    c=hex(12)
    print(str(a)+" "+str(b)+" "+str(c))
def zadanie10():
    lista=["Pianista","Avengers: Endgame","Hulk"]
    lista.sort()
def zadanie11():
    a=[0,math.radians(30),math.radians(45),math.radians(60),math.radians(90)]
    for i in a:
        print("Kąt "+str(math.degrees(i)))
        print("Sin")
        print(math.sin(i))
        print("Cos")
        print(math.cos(i))
        print("Tan")
        if i==math.radians(90):
            print("Nie istnieje")
        else:
            print(math.tan(i))
        print("Ctg")
        if math.tan(i)==0:
            print("Nie istnieje")
        else:
            print(1/math.tan(i))
def zadanie12():
    a="Siema siema byczuniu, jak tam życie?"
    b=[]
    b.extend(a.split())