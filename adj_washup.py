import random

import customtkinter as ctk


# Configure the appearance before creating any widgets.
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create and configure the main application window.
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

# Input field for the household activity.
activity_entry = ctk.CTkEntry(
    root,
    width=320,
    placeholder_text="Tâche à réaliser (ex. faire la vaisselle)",
)
activity_entry.pack(pady=6)

# Create the three participant input fields in a loop.
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
    """Choose a participant and display the final result."""
    # random.choice gives every entered participant an equal chance.
    chosen_participant = random.choice(participants)
    result_label.configure(
        text=f"{chosen_participant} doit faire :\n{activity}",
        text_color="#5eead4",
    )
    status_label.configure(text="Tirage terminé !")
    draw_button.configure(state="normal")


def animate_draw(activity, participants, remaining_steps=8):
    """Animate the draw without freezing the application window."""
    # Once the animation is finished, make the real selection.
    if remaining_steps == 0:
        finish_draw(activity, participants)
        return

    # This is only a visual preview, not the final result.
    preview_participant = random.choice(participants)
    result_label.configure(text=f"Tirage en cours...\n{preview_participant}")
    # after() waits without blocking Tkinter's event loop like sleep() would.
    root.after(
        120,
        lambda: animate_draw(activity, participants, remaining_steps - 1),
    )


def washup():
    """Validate the form and start a random draw."""
    # strip() removes spaces accidentally typed at the beginning or end.
    activity = activity_entry.get().strip()
    participants = [entry.get().strip() for entry in participant_entries]

    # An activity is required before starting the draw.
    if not activity:
        status_label.configure(text="Veuillez entrer une tâche.", text_color="#fca5a5")
        result_label.configure(text="Le tirage n'a pas commencé.")
        return

    # All three participant names are required for a fair draw.
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
    """Clear all inputs and restore the initial interface state."""
    # delete(0, "end") removes the complete content of an entry widget.
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

