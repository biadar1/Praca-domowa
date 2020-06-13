import sys
import math
def zadanie1():
    a=input("Podaj zdanie\n")
    print("Użyłeś/aś "+str(a.count(" "))+" Spacji")
def zadanie2():
    sys.stdout.writelines("Podaj pierwszą\n")
    a=float(sys.stdin.readline())
    sys.stdout.writelines("Podaj drugą\n")
    b=float(sys.stdin.readline())
    sys.stdout.write(str(a*b)+"\n")
#zadanie 3
    #odszukałem
def zadanie4():
    a=float(input("Podaj liczbę"))
    print(math.fabs(a))
    #a bez biblioteki math będzie
    #if a<0:
    #    print(a*-1)
    #else:
    #    print(a)
def zadanie5():
    a=float(input("Podaj pierwszą liczbę\n"))
    b=float(input("Podaj drugą liczbę\n"))
    c=float(input("Podaj trzecią liczbę\n"))
    if a>0 and a<=10:
        if a>b or b>c:
            print("Warunek spełniony")
    else:
        print("Warunek niespełniony")
def zadanie6():
    for i in range(1,11):
        print(i*5)
def zadanie7():
    i=int(input("Podaj ile liczb chcesz potęgować\n"))
    indeks=0
    while indeks<i:
        a=float(input("Podaj liczbę: "))
        print("Kwadrat tej liczby to: "+str(a**2))
        indeks+=1
def zadanie8():
    a=int(input("Ile chcesz podać liczb: "))
    b=[]
    i=0
    while i<a:
        c=float(input("Podaj liczbę: "))
        b.insert(i,c)
        i+=1
def zadanie9():
    a=int(input("Podaj liczbę całkowitą wielocyfrową dodatnią\n"))
    suma=0
    while a>0:
        suma+=a%10
        a=int(a/10)
    print(suma)
def zadanie10():
    a=-1
    b="A"
    while a<0 or a>10:
        a=int(input("Podaj liczbę od 0 do 10\n"))
    while a!=0:
        print(b)
        b=b+"A"
        a-=1
def zadanie11():
    a=0
    while a<=3 or a>=9:
        a=int(input("Podaj liczbę od 3 do 9\n"))
    for i in range(1,a):
        for j in range(1,a):
            if i==3 or j==3:
zadanie11()