import math

# Subtrahiert 2 Vektoren voneinander
# vec_a         Array[number, number, number]   Minuend  
# vec_b         Array[number, number, number]   Subtrahend
# return vec_c  Array[number, number, number]   Differenz
def vec_op_minus(vec_a, vec_b):                 #Vektorsubtraktion
    vec_c = [0,0,0]                        
    vec_c[0] = vec_a[0]-vec_b[0]
    vec_c[1] = vec_a[1]-vec_b[1]
    vec_c[2] = vec_a[2]-vec_b[2]
    return vec_c

# Berechnet das Skalarprodukt von 2 Vektoren
# vec_a         Array[number, number, number]   1.Vektor  
# vec_b         Array[number, number, number]   2.Vektor 
# return ret    Ergebnis[number]                Skalarprodukt der beiden Vektoren 
def vec_op_sp (vec_a, vec_b):                  #Skalarprodukt
    ret = vec_a[0]*vec_b[0]+vec_a[1]*vec_b[1]+vec_a[2]*vec_b[2]
    return ret

# Berechnet die Euklidische Norm, also die Laenge von 1 Vektor
# vec_a         Array[number, number, number]   Eingabevektor 
# return ret    Ergebnis(Länge)[number]        Euklidische Norm, also die Laenge des Vektors
def vec_op_euk (vec_a):                        #Euklidische Norm
    ret=(vec_a[0]*vec_a[0]+vec_a[1]*vec_a[1]+vec_a[2]*vec_a[2])**0.5  #**0.5 bedeutet Wurzel
    return ret

# Berechnet das Kreuzprodukt von 2 Vektoren
# vec_a     Array[number, number, number]   1.Vektor  
# vec_b     Array[number, number, number]   2.Vektor 
# vec_c     Array[number, number, number]   Kreuzprodukt der beiden Vektoren 
def vec_op_cross(vec_a, vec_b):             #Kreuzprodukt
    vec_c = [0,0,0]
    vec_c[0] = vec_a[1]*vec_b[2]-vec_a[2]*vec_b[1]
    vec_c[1] = vec_a[2]*vec_b[0]-vec_a[0]*vec_b[2]
    vec_c[2] = vec_a[0]*vec_b[1]-vec_a[1]*vec_b[0]
    return vec_c

print(vec_op_cross([1,2,3], [4,5,6]))
