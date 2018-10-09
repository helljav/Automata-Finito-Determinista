class Automata(object):
    #Estado Q0
    def q0(self,cadena,contador):
        #si es el ultimo digito a leer y se encuentra en este estado, no debe de aceptar la cadena
        if(len(cadena)==contador):
            return 1
        #Si no es el ultimo digito y es un uno se va a si mismo
        elif(cadena[contador]=="1"):
            print "voy a regresar"
            contador = contador+1
            return self.q0(cadena,contador)
        #Si no es el ultimo digito y es un cero se va al estado q1
        elif(cadena[contador]=="0"):
            print "voy pa q1"
            contador = contador+1
            return self.q1(cadena,contador)
    #Estado Q1
    def q1(self, cadena, contador):
        #Si no es el ultimo digito y se encuentra en ese estado no lodebe de reconocer la cadena
        if(len(cadena)==contador):
            return 1
        #Si no es el ultimo digito y es un cero se va a q2
        elif(cadena[contador]=="0"):
            contador = contador+1
            return self.q2(cadena,contador)
        #Si no es el ultimo digito y es un uno se va a q0
        elif(cadena[contador]=="1"):
            contador = contador+1
            return self.q0(cadena,contador)
    
    def q2(self, cadena, contador):

        if(len(cadena)==contador):
            return 0
        elif(cadena[contador]=="0"):
            contador = contador+1
            return self.q2(cadena,contador)
        elif(cadena[contador]=="1"):
            contador = contador+1
            return self.q0(cadena,contador)
