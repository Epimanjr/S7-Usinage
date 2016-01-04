#! /usr/bin/env python
# -*- coding: utf8 -*-
import Piece
import Machine
#import Entrepot
import Message
import sys

# launch all of our queued processes
def main(argv):
    nb = -1
    if len(sys.argv) == 3:
        if argv[0] == "-n":
            tmp = int(argv[1])
            if tmp > 0:
                nb = tmp
    if nb == -1:
        print('argument non valide')
        exit(1)
    print("----- DEBUT SIMULATION ENTREPOT -----")

    # Pièces
    Piece.processusPieces(nb)

    # Machine mA
    Machine.processusMachine("mA",["pA", "pB"],["mB"],nb)

    # Machine mB
    Machine.processusMachine("mB",["pB", "pC"],["mA"],nb)

    # Entrepôt
    Entrepot.processusEntrepot()

    print("------ FIN SIMULATION ENTREPOT ------")

main(sys.argv[1:])