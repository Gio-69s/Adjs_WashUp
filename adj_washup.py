import random

import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Adj_WashUp")
root.geometry("460x520")
root.resizable(False, False)

title_label = ctk.CTkLabel(
    root,
    text="Qui fait la tâche ?",
    font=ctk.CTkFont(size=24, weight="bold"),
)
title_label.pack(pady=(24, 6))

subtitle_label = ctk.CTkLabel(
    root,
    text="Entrez une tâche et les trois participants.",
)
subtitle_label.pack(pady=(0, 20))

activity_entry = ctk.CTkEntry(
    root,
    width=320,
    placeholder_text="Tâche à réaliser (ex. faire la vaisselle)",
)
activity_entry.pack(pady=6)

participant_entries = []
for number in range(1, 4):
    entry = ctk.CTkEntry(
        root,
        width=320,
        placeholder_text=f"Nom de l'enfant {number}",
    )
    entry.pack(pady=6)
    participant_entries.append(entry)

status_label = ctk.CTkLabel(root, text="")
status_label.pack(pady=(18, 4))

result_label = ctk.CTkLabel(
    root,
    text="Le résultat apparaîtra ici.",
    font=ctk.CTkFont(size=18, weight="bold"),
    wraplength=380,
)
result_label.pack(pady=8)


def finish_draw(activity, participants):
    """Choisit et affiche le participant après l'animation."""
    chosen_participant = random.choice(participants)
    result_label.configure(
        text=f"{chosen_participant} doit faire :\n{activity}",
        text_color="#5eead4",
    )
    status_label.configure(text="Tirage terminé !")
    draw_button.configure(state="normal")


def animate_draw(activity, participants, remaining_steps=8):
    """Anime le tirage sans bloquer la fenêtre."""
    if remaining_steps == 0:
        finish_draw(activity, participants)
        return

    preview_participant = random.choice(participants)
    result_label.configure(text=f"Tirage en cours...\n{preview_participant}")
    root.after(
        120,
        lambda: animate_draw(activity, participants, remaining_steps - 1),
    )


def washup():
    """Valide les champs puis démarre un tirage au sort."""
    activity = activity_entry.get().strip()
    participants = [entry.get().strip() for entry in participant_entries]

    if not activity:
        status_label.configure(text="Veuillez entrer une tâche.", text_color="#fca5a5")
        result_label.configure(text="Le tirage n'a pas commencé.")
        return

    if any(not participant for participant in participants):
        status_label.configure(
            text="Veuillez entrer les trois noms.",
            text_color="#fca5a5",
        )
        result_label.configure(text="Le tirage n'a pas commencé.")
        return

    status_label.configure(text="Bonne chance à tous !", text_color="white")
    result_label.configure(text="Préparation du tirage...", text_color="white")
    draw_button.configure(state="disabled")
    animate_draw(activity, participants)


def clear_form():
    """Efface les champs et remet l'interface à son état initial."""
    activity_entry.delete(0, "end")
    for entry in participant_entries:
        entry.delete(0, "end")
    status_label.configure(text="")
    result_label.configure(text="Le résultat apparaîtra ici.", text_color="white")


draw_button = ctk.CTkButton(root, text="Lancer le tirage", command=washup)
draw_button.pack(pady=(20, 8))

clear_button = ctk.CTkButton(
    root,
    text="Effacer",
    command=clear_form,
    fg_color="transparent",
    border_width=1,
)
clear_button.pack()

root.mainloop()

