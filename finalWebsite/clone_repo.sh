#!/bin/bash

# Chemin vers le répertoire où le dépôt sera cloné
DEST_DIR="/opt/render/project/src"

# Supprimer le répertoire existant s'il existe
rm -rf $DEST_DIR

# Cloner le dépôt sans LFS
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/ChristianNissan/PA-4IABD $DEST_DIR

# Passer dans le répertoire cloné
cd $DEST_DIR

# Installer les dépendances
pip install -r requirements.txt

# Démarrer l'application
gunicorn finalWebsite.wsgi:application

