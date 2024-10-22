#- Escribe un método recursivo para calcular la potencia de un número 'a' 
# elevado  a 'b': a^b.

def potencia(base,exponente):
    if exponente==1:
        return base
    elif exponente==0:
        return 1
    else:
        return base*potencia(base,exponente-1)
a=2
b=3
print(f"{a}^{b} = {potencia(a,b)}")
