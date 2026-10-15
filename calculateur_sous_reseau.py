import ipaddress #sert a manipuler les adresses IP

saisie = input("Adresse IP avec masque (ex: 192.168.1.10/24) : ") #ici on va demander l'adresse

interface = ipaddress.ip_interface(saisie) #transforme le texte en objet que python comprend comme une IP et son masque 
reseau = interface.network #récupère le réseau auquel l'IP apparatient

adresse_ip = interface.ip
masque = reseau.netmask
cidr = reseau.prefixlen
adresse_reseau = reseau.network_address
broadcast = reseau.broadcast_address