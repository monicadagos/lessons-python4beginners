# -*- coding: utf-8 -*-

def do_hello(input_saluto): #Una funzione è un simbolo all'interno di un modulo (noi possiamo importare anche solo alcuni simboli di un modulo che sono la nostra libreria)
    print(u"Sono dentro la funzione e mi è arrivato questo input: " + input_saluto)
    tot = 1 + 1
    print("tot vale " + str(tot))

# La funzione finisce quando finsice l'indentazione
# Se vieni importato come libreria e non per essere eseguito non printare.
if __name__ == "__main__":
    do_hello("Ciaone")
