
def promedio(n1,n2,n3):
    prom=(n1+n2+n3)/3
    if prom>=6 and prom<=10:
        return "Aprobado"
    else:
        return "No Aprobado"
    

alumno1=promedio(8,7,4)
print (f"Alumno 1:  {alumno1}")

alumno2=promedio(6,4,5)
print (f"Alumno 2:  {alumno2}")