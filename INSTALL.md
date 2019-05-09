# Installation du projet

## Serveur Mysql

### Configuration

- Il faut lancer les scripts contenus dans `Server/database` : `SQL_script_create_database.sql` et `SQL_script_init_database.sql`.

## Serveur principal

### Prérequis

- Python 3
- python-mysql-connector

### Configuration

- Il faut modifier les paramètres de connexion à la base de données MySQL dans `Server/servlets/action_servlet.py`.
- Il faut modifier les paramètres de connexion au serveur principal dans `Data_Treatments/http_methods.py` si nécessaire.

### Exécution

- Il faut lancer `python3 web_server.py` depuis le dossier `Server`.
- Il faut aussi lancer `python3 compute_waiting_time.py` depuis le dossier `Data_Treatments`.

## Raspberry Pi

### Prérequis

- Python 3
- python-gpiozero
- python-pigpio

### Configuration

- Il faut modifier les paramètres de connexion au serveur principal dans `Sensors/sensors.py`.
- Il faut modifier la liste des ports et des identifiants des capteurs dans `Sensors/sensors.py`.

### Exécution

- Il faut lancer `python3 sensors.py` depuis le dossier `Sensors`.
