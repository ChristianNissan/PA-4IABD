# clone_repo.sh
#!/bin/bash

# Désactiver les filtres LFS
git lfs uninstall

# Cloner le dépôt sans LFS
git clone https://github.com/ChristianNissan/PA-4IABD.git .
