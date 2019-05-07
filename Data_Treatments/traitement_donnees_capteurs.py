import datetime
from datetime import date
from random import *
import json

def gen_data_ir(cap,starting_time,data,max_delta):
    nb_donnees = randint(0,3)
    for i in range (nb_donnees):
        now = starting_time + datetime.timedelta(days=0,seconds=randint(1,max_delta))
        data[cap][now] = -1
    i = 0
    transitions = sorted(data[cap].keys(), reverse=True)
    for time in transitions:
        data[cap][time] = i%2
        i = i+1

def gen_data_ul(cap,starting_time,ending_time,data):
    delta = ending_time-starting_time
    for cur in range(delta.seconds):
        data[cap][starting_time+datetime.timedelta(days=0,seconds=cur)] = random()*5

def init_data():
    now_init = datetime.datetime.now()
    data = {}
    data_IR1 = {}
    data_IR2 = {}
    data_IR3 = {}
    data_IR4 = {}
    data_UL1 = {}
    data_UL2 = {}
    data_UL3 = {}
    data_UL4 = {}
    data_UL5 = {}
    data["IR1"] = data_IR1
    data["IR2"] = data_IR2
    data["IR3"] = data_IR3
    data["IR4"] = data_IR4
    data["UL1"] = data_UL1
    data["UL2"] = data_UL2
    data["UL3"] = data_UL3
    data["UL4"] = data_UL4
    data["UL5"] = data_UL5
    data["begin"] = now_init
    data["end"] = data["begin"] + datetime.timedelta(days=0,seconds=20)
    for cap in data:
        if cap.startswith("IR"):
            gen_data_ir(cap,now_init,data,19)
                
        elif cap.startswith("UL"):
            gen_data_ul(cap,data["begin"],data["end"],data)
    print(data)
    return data

def lire_etat():
    fichier = open("etat_capteur", "r")
    etat = json.loads(fichier.read())
    fichier.close()
    return etat

def ecrire_etat(etat):
    fichier = open("etat_capteur", "w")
    fichier.write(json.dumps(etat))
    fichier.close()

def lire_transition():
    fichier = open("derniere_transition", "r")
    transition = json.loads(fichier.read())
    fichier.close()
    return transition

def ecrire_transition(transition):
    fichier = open("derniere_transition", "w")
    fichier.write(json.dumps(transition, default=str))
    fichier.close()

def ecrire_distance_max_ul():
    distances = {}
    distances["UL1"] = 5.0
    distances["UL2"] = 5.0
    distances["UL3"] = 5.0
    distances["UL4"] = 5.0
    distances["UL5"] = 5.0
    fichier = open("distance_max_ultrason", "w")
    fichier.write(json.dumps(distances))
    fichier.close()

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

ordre_capteurs = lire_ordre_capteur()
data = init_data()

etat = lire_etat()

last_transition = lire_transition()

distances_max = lire_distance_max_ul()

delta = datetime.timedelta(days=0,seconds=10)

now = datetime.datetime.now()

debut_inter = data["begin"] #a modifier pour le reel
fin_inter = data["end"] #a modifier pour le reel

time_format = "%Y-%m-%d %H:%M:%S.%f"

for cap in ordre_capteurs:
    if cap.startswith("IR"):
        transitions = sorted(data[cap].keys(), reverse=True)
        nb_transitions = len(transitions)
        if nb_transitions > 1:
            if fin_inter - transitions[0] >= delta:
                etat[cap] = data[cap][transitions[0]]
                last_transition[cap] = ""
            else:
                for i in range(nb_transitions-1):
                    diff = transitions[i] - transitions[i+1]
                    if diff >= delta:
                        etat[cap] = data[cap][transitions[i+1]]
                        break
                last_transition[cap] = transitions[0]
        elif nb_transitions == 1:
            diff = fin_inter - transitions[0]
            if diff >= delta:
                etat[cap] = data[cap][transitions[0]]
                last_transition[cap] = ""
            elif last_transition[cap] != "":
                diff = transitions[0] - datetime.datetime.strptime(last_transition[cap],time_format)
                if diff >= delta:
                    if etat[cap] == 0:
                        etat[cap] = 1
                    else:
                        etat[cap] = 0
                last_transition[cap] = transitions[0]
            else:
                last_transition[cap] = transitions[0]
        else:
            if last_transition[cap] != "":
                diff = fin_inter - datetime.datetime.strptime(last_transition[cap],time_format)
                if diff >= delta:
                    if etat[cap] == 0:
                        etat[cap] = 1
                    else:
                        etat[cap] = 0
                    last_transition[cap] = ""
    elif cap.startswith("UL"):
        somme = 0
        for time in data[cap].keys():
            somme = somme + data[cap][time]
        avg = somme/len(data[cap].keys())
        etat[cap] = (distances_max[cap] - avg)/distances_max[cap]

ecrire_etat(etat)
ecrire_transition(last_transition)

