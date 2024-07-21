# File Stream 📁🌍

File Sharing est un projet qui permet de partager des fichiers entre ordinateurs à travers un réseau. Ce projet est composé d'un serveur et d'un client, avec une interface graphique optionnelle pour le client (client_gui). Les utilisateurs peuvent envoyer et recevoir des fichiers rapidement et facilement sur un réseau local par défaut, avec la possibilité d'ajuster les configurations IP pour une utilisation sur différents réseaux.

## Fonctionnalités 🚀

- **Partage de fichiers facile :** Permet aux utilisateurs d'envoyer et de recevoir des fichiers en quelques clics.
- **Interface graphique pour le client :** Fournit une interface utilisateur simple pour naviguer et sélectionner les fichiers à partager.
- **Compatibilité réseau flexible :** Peut être configuré pour fonctionner sur des réseaux locaux ou étendus en modifiant les adresses IP dans les fichiers de configuration.

## Prérequis 📋

- Python 3.7+
- Bibliothèques Python spécifiées dans `requirements.txt`

## Configuration Environnementale 🛠️

### Clonage du Projet

Pour commencer, clonez le projet sur votre machine locale :

```bash
git clone https://github.com/KpihX/file_share.git
cd file_share
```

### Création d'un Environnement Virtuel

Utilisez un environnement virtuel pour exécuter le projet sans conflit de dépendances.

#### Sous Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### Sous Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### Installation des Dépendances

Installez les dépendances nécessaires via pip :

```bash
pip install -r requirements.txt
```

## Configuration du Projet 🔧

Avant de démarrer, configurez les adresses IP dans `server.py` et `client.py` (et éventuellement `client_gui.py`) pour correspondre à votre réseau. Les configurations par défaut sont établies pour une utilisation locale (`localhost` ou `127.0.0.1`).

## Lancement 🚀

### Serveur (Recepteur)

Pour lancer le serveur, exécutez :

```bash
python recv.py
```

### Client (envoyeur)

Pour démarrer l'interface graphique de l'envoyeur, utilisez :

```bash
python send.py
```

## Utilisation 🖱️

Une fois le serveur et le client GUI lancés, vous pouvez choisir des fichiers à partager et les envoyer à d'autres utilisateurs connectés au serveur. L'interface graphique facilite la navigation et la sélection des fichiers.

## Contribution 🤝

Les contributions au projet sont encouragées et appréciées. Pour proposer des améliorations ou corriger des bugs, soumettez des pull requests ou ouvrez des issues.

## Auteur ✍️

- KpihX

---

Explorez et expérimentez avec le code pour mieux comprendre le fonctionnement du projet File Sharing. Bonne programmation !"
