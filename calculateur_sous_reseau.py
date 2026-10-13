import ipaddress #sert a manipuler les adresses IP

saisie = input("Adresse IP avec masque (ex: 192.168.1.10/24) : ") #ici on va demander l'adresse

interface = ipaddress.ip_interface(saisie) #transforme le texte en objet que python comprend comme une IP et son masque 
reseau = interface.network #récupère le réseau auquel l'IP apparatient