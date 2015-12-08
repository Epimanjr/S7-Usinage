#! /usr/bin/env python
# -*- coding: utf8 -*-
import os
import sys
import random

class Piece: #creation de l'objet pièce

        """Une pièce est définie uniquement par son type"""
        def __init__(self, type): #Construit une pièce
            self.type = type

        #Méthode qui envoit un pièce à une machine sélectionnée aléatoirement
        def envoyerPiece(self):
            numeroMachine = random.randint(0,1);
            if numeroMachine == 0:
                typeMachine = "mA"
            else:
                typeMachine = "mB"
            print("fileMachine ; "+typeMachine+" ; "+self.type)

        #Méthode qui affiche les informations sur la pièce
        def afficher(self):
            print("Je suis une pièce de type : "+self.type);


i=0
while i<11:
    #génération aléatoire d'une pièce
    rand = random.randint(0,2);
    if rand == 0:
        typePiece = "pA"
    else:
        if rand == 1:
            typePiece = "pB"
        else:
                typePiece = "pC"
    piece = Piece(typePiece);
    piece.afficher();
    #envoit de la pièce
    piece.envoyerPiece();
    i=i+1;