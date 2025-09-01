import random
import customtkinter as ctk


#Création de la fenêtre principale

root = ctk.CTk()
root.title("Adj_Washup")
root.geometry("400x400")

#Apparence de la fenetre 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Changement du logo de la fenêtre

root.iconbitmap("favicon.ico")

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


def washup():
    """
    Fonction qui choisit un utilisateur au hasard pour effectuer une activité donnée.
    Récupère l'activité et les noms d'utilisateur à partir des champs de saisie.
    Cree une liste avec les noms d'utilisateur non vides.
    Choisit un utilisateur au hasard dans la liste et affiche le résultat dans une étiquette.
    """
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
        root_label=ctk.CTkLabel(root, text=f"Celui qui fera :{activity} est : {result}")
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

