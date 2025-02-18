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

#Berechnet die Skalarmultiplikation zwischen einem Skalar und einem Vektor
#l      integer, oder numbering-Zahl    Skalar
#vec    Array[number, number, number]   Eingabektor, d.h. der zu skalierende Vektor 
#vec_c  Array[number, number, number]   Ergebnisvektor, d.h. der skalierte Vektor
def vec_op_skal_mul(l, vec):            #Skalarmultiplikation eines Vektors
    vec_c = [0.0,0.0,0.0]
    vec_c[0]=l*vec[0]
    vec_c[1]=l*vec[1]
    vec_c[2]=l*vec[2]
    return vec_c

#Berechnet den Arcustangens von 2 Zahlen
#x      number
#y      number
#alpha  Ergebnis, also der Arcustangens von x und y
def arctan(x, y):                       #Arcustangens
    if (x>0) and (y>0):                 #gemäß Vorgabe im Artikel
            alpha=math.atan(y/x)
    elif (x<0):
        alpha=math.atan(y/x) +   math.pi
    else:
            alpha=math.atan(y/x) + 2*math.pi
    return alpha 


