def ExtEuclides(a,b):
    if (b==0):
        return a,1,0
    d,xP,yP = ExtEuclides(b,a%b)
    x,y = (yP,xP -yP * int(a/b))
    return d,x,y

a,b=-1,-1
while(a<0 or b<0):
  a = int(input('\nIngrese un numero para la variable "a": '))
  b = int(input('\nIngrese un numero para la variable "b": '))
  if (a<0 or b<0):
    print("\nIngrese enteros no negativos")
  
mcd,x,y = ExtEuclides(a,b)
print(f'\n- Ec: {a}x + {b}y = {mcd}')

print(f'\nEl Maximo Comun Divisor de "a"={a} y "b"={b} es: {mcd} \n')
print(f'El valor de "x" es {x} y el valor de "y" es {y} \n')
print("mcd(a,b) = ax + by (x,y que pertenecen a los Z) \n")
print(f"{(a*x)+(b*y)} = {a}({x}) + {b}({y})")
