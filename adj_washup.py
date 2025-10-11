import random
import customtkinter as ctk
import time 


#Création de la fenêtre principale

root = ctk.CTk()
root.title("Adj_Washup")
root.geometry("400x400")

#Apparence de la fenetre 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Création du champ de saisie pour le choix de l'activité

root_entry=ctk.CTkEntry(root, placeholder_text="Entrez ici l'activité")
root_entry.pack(pady=15)

#Création des champs de saisie pour les noms d'utilisateur

root_entry1=ctk.CTkEntry(root)
root_entry1.pack(pady=20)

root_entry2=ctk.CTkEntry(root)
root_entry2.pack(pady=25)

root_entry3=ctk.CTkEntry(root)
root_entry3.pack(pady=30)

# Fonction principale qui lance le tirage au sort
def washup():
    """
    Cette fonction est appelée quand on clique sur le bouton "Lancer Washup".
    Elle sert à choisir au hasard une personne parmi trois pour réaliser une activité.
    Voici comment elle fonctionne :
    1. Elle récupère le nom de l'activité et les trois noms entrés par l'utilisateur.
    2. Elle vérifie que les champs sont bien remplis.
    3. Elle utilise une fonction interne pour afficher des points pendant quelques secondes, pour faire patienter.
    4. Elle choisit un des trois noms au hasard.
    5. Elle affiche le résultat dans la fenêtre : qui doit faire l'activité.
    Si jamais il manque un nom, elle affiche un message d'erreur pour prévenir l'utilisateur.
    """

    # Fonction interne qui affiche un temps d'attente
    def temps_dattente_pour_laffichage(seconde, point="."):
        """
        Cette fonction sert à faire patienter l'utilisateur avant d'afficher le résultat.
        Elle affiche un point à l'écran chaque seconde, pendant le nombre de secondes indiqué.
        Par exemple, si on met 3 secondes, elle va afficher trois points, un par seconde.
        Cela permet de créer un petit suspense avant de révéler le nom choisi.
        """
        while seconde > 0:
            print(point, end="")
            time.sleep(1)
            seconde -= 1
                   
    try:

        #Récupération de l'activité
        activity=root_entry.get()


        #Demander les noms d'utilisateur
        u1=root_entry1.get()
        u2=root_entry2.get()
        u3=root_entry3.get()

        #Création d'une liste avec les noms d'utilisateur 
        list_user=[u1,u2,u3]

        [u for u in list_user if u != ""]

        #Choisir un utilisateur au hasard dans la liste
   
        result=random.choice(list_user)
        root_label=ctk.CTkLabel(root, text=f"Celui qui fera la {activity} est {temps_dattente_pour_laffichage(3)} {result} !!!")
        root_label.pack(pady=10, padx=10)
    except:
        root_label=ctk.CTkLabel(root, text="Erreur: Veuillez entrer trois noms d'utilisateur")
        root_label.pack(pady=10 , padx=10)

   
#Création d'un bouton pour lancer la fonction washup
button=ctk.CTkButton(root, text="Lancer Washup", command=washup)
button.pack(pady=10)

#Création d'une étiquette pour afficher un message
root_label=ctk.CTkLabel(root, text="Cliquez sur le bouton pour lancer Washup !")
root_label.pack(pady=15,padx=5)

#Lancer la boucle principale de l'application
root.mainloop()

