import random
import tkinter as tk


root = tk.Tk()
root.title("Washup")
root.geometry("400x400")
root.config(bg="lightblue")

#Changement du logo de la fenêtre
root.iconbitmap("favicon.ico")
#Fonction pour demander les noms d'utilisateur et choisit aléatoirement un utilisateur

root_entry1=tk.Entry(root)
root_entry1.pack(pady=20)

root_entry2=tk.Entry(root)
root_entry2.pack(pady=25)

root_entry3=tk.Entry(root)
root_entry3.pack(pady=30)



def washup():
   #Demander les noms d'utilisateur
    u1=root_entry1.get()
    u2=root_entry2.get()
    u3=root_entry3.get()

   #Création d'une liste avec les noms d'utilisateur 
    list_user=[u1,u2,u3]

    result=random.choice(list_user)
    root_label=tk.Label(root, text=f"Celui fera la vaisselle est {result}")
    root_label.pack(pady=10)



#Création d'un bouton pour lancer la fonction washup
button=tk.Button(root, text="Lancer Washup", command=washup)
button.pack(pady=40)

#Création d'une étiquette pour afficher un message
root_label=tk.Label(root, text="Cliquez sur le bouton pour lancer Washup !")
root_label.pack(pady=35)

#Lancer la boucle principale de l'application
root.mainloop()

