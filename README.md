# Adj_WashUp

Une petite application de bureau en Python qui répartit au hasard trois tâches ménagères entre trois enfants.

## Fonctionnalités

- Saisir trois tâches ménagères différentes.
- Saisir les noms de trois participants.
- Lancer un tirage au sort animé qui attribue une tâche différente à chaque enfant.
- Éviter qu'un enfant reçoive la même tâche deux jours de suite.
- Conserver le tirage du jour et l'historique dans `~/.adj_washup_history.json`.
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

Entrez les trois tâches et les trois noms, puis cliquez sur **Lancer le tirage**. Chaque tâche est attribuée à un seul enfant. Le tirage du jour est conservé ; le lendemain, les affectations qui répètent la tâche de la veille sont exclues. L'historique est stocké dans le dossier personnel de l'utilisateur.

## Technologies

- Python
- Tkinter via [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

## Licence

Ce projet est distribué selon les conditions indiquées dans le fichier [LICENSE](LICENSE).
