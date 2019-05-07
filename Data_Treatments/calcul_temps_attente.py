import json

def lire_etat():
    fichier = open("etat_capteur", "r")
    etat = json.loads(fichier.read())
    fichier.close()
    return etat

def lire_distance_max_ul():
    fichier = open("distance_max_ultrason", "r")
    distances = json.loads(fichier.read())
    fichier.close()
    return distances
    
def lire_ordre_capteur():
    fichier = open("ordre_capteurs_file", "r")
    ordre_capteurs = []
    ordre_capteurs = json.loads(fichier.read())
    fichier.close()
    return ordre_capteurs
    
def lire_nb_personnes_capteur():
    fichier = open("nb_personnes_capteurs", "r")
    nb_personnes_capteurs = []
    nb_personnes_capteurs = json.loads(fichier.read())
    fichier.close()
    return nb_personnes_capteurs

etat = lire_etat()
distances_max = lire_distance_max_ul()
ordre_capteurs = lire_ordre_capteur()
nb_personnes_capteurs = lire_nb_personnes_capteur()
estim_nb_personnes = {}
i = 0
for cap in ordre_capteurs:
    estim_nb_personnes[cap] = nb_personnes_capteurs[i]
    i = i+1
i = 0
debit = 8 #personnes par minute
detection_file = {}
for cap in ordre_capteurs:
    if cap.startswith("IR"):
        detection_file[cap] = etat[cap]
    elif cap.startswith("UL"):
        if etat[cap] <= 0.1:
            detection_file[cap] = 1
        else:
            detection_file[cap] = 0
for i in range(len(detection_file)-2):
    if (detection_file[ordre_capteurs[i]] == 0 and 
    detection_file[ordre_capteurs[i+1]] == 1 and
    detection_file[ordre_capteurs[i+2]] == 1):
        detection_file[ordre_capteurs[i]] = 1
i = 0
nbPersonnes = 0
while (i < len(ordre_capteurs) and detection_file[ordre_capteurs[i]] == 1):
    nbPersonnes = estim_nb_personnes[ordre_capteurs[i]]
    i = i+1
if i > 0:
    if ordre_capteurs[i-1].startswith("UL"):
        estim_prec = estim_nb_personnes[ordre_capteurs[i-1]]
        estim_approx = estim_nb_personnes[ordre_capteurs[i]]
        estim_reelle = estim_prec + (estim_approx - estim_prec)*etat[ordre_capteurs[i]]
        nbPersonnes = int(estim_reelle)
print("Estimation temps attente : {} minutes".format(nbPersonnes/debit))
        
