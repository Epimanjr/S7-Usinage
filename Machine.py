#! /usr/bin/env python
# -*- coding: utf8 -*-
import os
import sys
import time
from Piece import *
import Message

class Machine: #Création de notre objet Machine

    pieceCourante = Piece("")
    resultatCourant = ""

    """ Une machine est défini par son nom, et une liste de pièces traitables par la machine.
    """
    def __init__(self, nom, listePiecesTraitables, listeAutresMachines): # Construit une machine
        self.nom = nom
        self.listePiecesTraitables = listePiecesTraitables
        self.listeAutresMachines = listeAutresMachines

    # Méthode qui démarre la machine
    def fonctionner(self):
        # Réceception de la pièce
        self.recevoirPiece()
        # Vérification de la pièce
        if self.verifierPiece():
            # Traitement
            self.traiterPiece()
            # Stockage dans l'entrepôt
            self.stockerPiece()
        else:
            # Renvoie à l'autre machine
            self.renvoyerPiece()


    # Méthode qui renvoie la pièce à l'autre machine
    def renvoyerPiece(self):
        print("[XXX] On veut renvoyer la pièce")
        if len(self.listeAutresMachines) != 0:
            print("[XXX] On la renvoie ")
            Message.send("fileMachine",self.listeAutresMachines[0],self.pieceCourante.type)

    # Méthode qui récupère une pièce.
    def recevoirPiece(self):
        # Récupèration d'un message dans la file, où le type est le nom de la machine
        filetypemessage = Message.receive("fileMachine",self.nom)
        # Mise à jour de la pièce courante (qui est la pièce à traiter)
        self.pieceCourante = Piece(filetypemessage.message)
        print("[NEW] La nouvelle pièce courante est de type "+self.pieceCourante.type)

    # Méthode qui traite une pièce.
    def traiterPiece(self):
        # Traitement
        #time.sleep(1)
        if self.pieceCourante.type == "pA":
            self.resultatCourant = "rA"
        if self.pieceCourante.type == "pB":
            self.resultatCourant = "rB"
        if self.pieceCourante.type == "pC":
            self.resultatCourant = "rC"
        # Fin Traitement
        self.traite = True

    # Méthode qui stocke une pièce dans l'entrepôt
    def stockerPiece(self):
        print("[-->] On veut stocker")
        # Vérification
        if self.traite == True:
            # Stockage dans l'entrepôt
            print("[-->] On stocke")
            Message.send("fileEntrepot",self.nom,self.resultatCourant)

    # Méthode qui vérifie qu'une pièce est traitable par cette machine.
    def verifierPiece(self):
        for nomPiece in self.listePiecesTraitables:
            print("[???] On compare "+nomPiece+" et "+self.pieceCourante.type)
            if nomPiece == self.pieceCourante.type:
                return True
        return False

    # Méthode qui affiche d'une machine.
    def afficher(self):
        print("Bonjour, je suis la machine " + self.nom + " et j'accepte les pièces " + str(self.liste))


# Construction des deux machines
#machineA = Machine("mA", ["pA", "pB"]);
#machineB = Machine("mB", ["pB", "pC"]);
# Affichage
#machineA.afficher();
#machineB.afficher();


def processusMachine(nom, listePiecesTraitables, listeAutresMachines, nb):
    print("LISTE DES MESSAGES INITIALE")
    Message.afficherListeMessages()
    machine = Machine(nom, listePiecesTraitables, listeAutresMachines)
    i = 0
    while i<nb:
        machine.fonctionner()
        i = i + 1
        print(" ");
    print("LISTE DES MESSAGES FINALE")
    Message.afficherListeMessages()


#processusMachine("mA",["pA", "pB"],["mB"])