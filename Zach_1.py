import math
#import matplotlib.pyplot as plt #Plotter, um Bilder zu erstellen
import random
#Array ist vom Typ = [[[[],[]],[[],[]]]]

#********************************************************************************************#
#                  D  A  T  E  I  W  E  R  T  E     L  A  D  E  N                            #
#********************************************************************************************#

def is_number(str):                     #testet, ob ein gegebener String sich in eine Float verwandeln läßt oder nicht.
    try:
        float(str)
        return True
    except ValueError:
        return False

# Laedt eine gegebene Datei in ein Array
# filename      String 
# return        Array von gegebenem Typ.
def load_file(filename):                #Ziel ist es, dass die Messzahlen von Messung 1 und dann Messung 2 reingeladen werden
    fobj = open(filename, "r")          #...deshalb zuerst öffnen und einlesen; "r" =read, also einlesen

    hilfsarray=[]
    for line in fobj:
        str = line.strip();             #hier eine Analyse, um zu testen ob es sich bei dem String um eine Zahl handelt
                                        #wenn nicht, würde das Programm in der nächste Zeile aussteigen.
        if(len(str) > 0 and is_number(str)): 
            x = float(str)
            hilfsarray.append(x)
                                        #lese die 1.Zahl aus der Datei in das Hilfsarray
                                        #line ist ein String (da alles was aus der Datei im txt-Modus gelesen wird ein String ist)
                                        # float(...) konvertiert die Zeile in eine Zahl. Dazu müssen die nicht sichtbaren Hilfszeichen aber gelöscht werden
                                        #[Variable vom Typ String].strip löscht alle nicht sichtbaren Zeichen vor und hinter der Zeile
    fobj.close()                        # die gesamte Datei ist in einem Hilfsarray, jede Zeile wird von einem Block repräsentiert
                                        # nun sind 2 weitere Hilfsarrays zu konstruieren, die je einen Vektor aufnehmen koennen

    length = len(hilfsarray)            #wie viele Informationen sind in dem Hilfsarray?
    i = 0                               #eine Zählervariable um zu wissen in welcher Zeile man in der Datei ist
    file_array = []                     #Das Array in dem hinterher die gesamten Doppelvektoren dieser Datei gespeichert werden

    while(i<length):                    #hilfssarray = datei die geladen wird
        vec_hilfsarray_a = []           #initialisiert das Vektor Hilfsarray a 
        vec_hilfsarray_a.append(hilfsarray[i]) 
        i += 1
        vec_hilfsarray_a.append(hilfsarray[i])
        i += 1
        vec_hilfsarray_a.append(hilfsarray[i])
        i += 1
        
        vec_hilfsarray_b = []           #initialisiert das Vektor Hilfsarray b
        vec_hilfsarray_b.append(hilfsarray[i])
        i += 1
        vec_hilfsarray_b.append(hilfsarray[i])
        i += 1
        vec_hilfsarray_b.append(hilfsarray[i])
        i += 1
                                        # ... fülle die beiden Vektor - Hilfsarrays mit den Informationen aus dem Datei Hilfsarray
        element = []
        element.append(vec_hilfsarray_a)
        element.append(vec_hilfsarray_b)#... und so weiter (mit vec_hilfsarray_b)
                                        #damit hat man den Doppelvektor mit dem Namen Element
        file_array.append(element)
                                        
    return file_array;

# so soll das aussehen: Array = [[[[1.0,2.0,3.0],[1,2,1]] , [[7.0,7.0,7.0],[1,2,3]]] , [[[1.2,1.9,3.2],[1,8,9]] , [[6.7,7.1,6.5],[7,7,9]]]]

#********************************************************************************************#
#                       F  U  N  K  T  I  O  N  E  N                                         #
#********************************************************************************************#


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


#********************************************************************************************#
#                         H A U P T - P R O G R A M M                                        #
#********************************************************************************************#

def findfirstbigger(number,numlist):	#geht Liste durch und gibt Index der ersten Zahl aus numlist zurück die größer als number ist
    for i,q in enumerate(numlist):
        if q>=number:
            return i
    return len(numlist)


templimits = [-0.6,-0.2,0.2,0.6]
LIMITS = [[i*math.pi for i in templimits],templimits,templimits,[0.2,0.4,0.6,0.8]]  #Liste von Liste von Zahlen, bezieht sich auf alpha BIS delta

class Feature(object):		    #alle Feature Objekte haben diese Funktionen	
                                    #"Class Feature (object [object heißt es erbt von Keinem])" hat 4 Eigenschaften, nämlich alpha, beta, gamma, delta							
    
    def __init__(self,alpha,beta,gamma,delta):  #Konstruktor Eigenschaften:1.)erstellt EIN Objekt, in diesem Objekt sind alpha bis delta// Konstruktor, wegen Stichwort "__init__" 	
        self.alpha = alpha                      #Konstruktor Eigenschaften: 2.)bekommt Argumente uebergeben (alpha bis delta) 
        self.beta = beta                        #Konstruktor Eigenschaften: 3.)die 4 Eigenschaften werden im neuen Objekt gespeichert
        self.gamma = gamma                      #Alpha bis Delta sind die 4 Eigenschaften des Objekts
        self.delta = delta
        
    #bekommt EIN Feature Objekt von jedem, der diese Funktion aufruft
    #nimmt dieses Objekt und gibt die 4 Eigenschaften davon als Liste zurück  
    def aslist(self):
        return [self.alpha,self.beta,self.gamma,self.delta]

    #Erzeugt aus Features die Bin ID von einem Eintrag
    #Addiert alle Einträge von alpha bis delta zusammen und erstellt so die ID
    def genBinID(self):																		
        ret=[0]*IDLENGTH				#erstellt eine mit 0 vorinitialisierte Liste
        for feature,zahl in enumerate(self.aslist()):	#"self.aslist" gibt eine Liste zurueck mit den Eiträgen alpha bis delta....bis jetzt haben wir 2 verschiedene Listen
            ret[findfirstbigger(zahl,LIMITS[feature])]+=1 #erhöht die auf 0 vorinitialisierte Liste an der richtigen Stelle um 1
        return ret
    
    def __str__(self, *args, **kwargs):						#Funktion, die ein Feature (was ja ein Objekt ist), in einen String umwandelt
        return "Feature(Alpha: "+str(self.alpha)+"; Beta: "+str(self.beta)+"; Gamma: "+str(self.gamma)+"; Delta: "+str(self.delta)+")"	#das ist der String
    
    def __repr__(self, *args, **kwargs):					#gibt einen String zurueck
        return str(self)

Array = [load_file("Messung_1.txt"), load_file("Messung_2.txt")]
print(Array)
