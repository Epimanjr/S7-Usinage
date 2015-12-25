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

    def send(self):
        Message.listeMessages.append(self)

    def afficher(self):
        print "File", self.file, "Type", self.type, "Message", self.message


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
    mess.send()

# Fonction receive WITH LOOP
def receive(file, type):
    # flag
    trouve = False
    while not trouve:
        # Parcours de la liste
        for mess in Message.listeMessages:
            if mess.file == file and mess.type == type:
                trouve = True
                return mess
        # Attendre 2 secondes
        time.sleep(2)