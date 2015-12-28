#! /usr/bin/env python
# -*- coding: utf8 -*-
import os
import sys
import time

class Message:

    # Liste de tous les messages
    listeMessages = []

    def __init__(self, file, type, message): # Construit un message
        self.file = file
        self.type = type
        self.message = message

    def ajouter(self):
        Message.listeMessages.append(self)

    def afficher(self):
        print("- File:", self.file, " - Type:", self.type, " - Message:", self.message)


# TEST
#print "Envoie d'un message"
#mess = Message("file1", "type1", "message1")
#mess.send()
#Message.listeMessages[0].afficher()
# FIN TEST

# Fonction send
def send(file, type, message):
    # Création d'une instance
    mess = Message(file, type, message)
    # Envoie
    mess.ajouter()

# Fonction receive WITH LOOP
def receive(file, type):
    # flag
    trouve = False
    while not trouve:
        # Parcours de la liste
        for i in range(0,len(Message.listeMessages)-1):
            mess = Message.listeMessages[i]
            if mess.file == file and mess.type == type:
                trouve = True
                print("[SUP] Un message de la file "+mess.file+" a été reçu donc supprimé de la liste.")
                Message.listeMessages.pop(i)
                return mess
        # Attendre 2 secondes
        # time.sleep(2)

def afficherListeMessages() :
    print("LISTE DES MESSAGES:")
    for message in Message.listeMessages:
        message.afficher();
    print("FIN LISTE DES MESSAGES.")
    print(" ")