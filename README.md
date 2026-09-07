# Adj_WashUp

Une petite application de bureau en Python qui choisit au hasard la personne chargée d'une tâche ménagère.

## Fonctionnalités

- Saisir une tâche à réaliser.
- Saisir les noms de trois participants.
- Lancer un tirage au sort animé.
- Effacer le formulaire pour recommencer.

## Prérequis

- Python 3.9 ou une version plus récente.
- `customtkinter`.

## Installation

1. Clonez le dépôt et ouvrez son dossier :

	```bash
	git clone <URL_DU_DEPOT>
	cd Adjs_WashUp
	```

2. Installez la dépendance :

	```bash
	python -m pip install customtkinter
	```

## Utilisation

Lancez l'application avec :

```bash
python adj_washup.py
```

Entrez une tâche, les trois noms, puis cliquez sur **Lancer le tirage**. Chaque participant a la même probabilité d'être choisi.

## Technologies

- Python
- Tkinter via [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

## Licence

Ce projet est distribué selon les conditions indiquées dans le fichier [LICENSE](LICENSE).
