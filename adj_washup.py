import itertools
import json
import random
from datetime import date, timedelta
from pathlib import Path

import customtkinter as ctk


# Configure the appearance before creating any widgets.
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create and configure the main application window.
root = ctk.CTk()
root.title("Adj_WashUp")
root.geometry("480x700")
root.resizable(False, False)

HISTORY_PATH = Path.home() / ".adj_washup_history.json"

title_label = ctk.CTkLabel(
    root,
    text="Répartition des tâches",
    font=ctk.CTkFont(size=24, weight="bold"),
)
title_label.pack(pady=(24, 6))

subtitle_label = ctk.CTkLabel(
    root,
    text="Entrez les trois tâches et les trois enfants.",
)
subtitle_label.pack(pady=(0, 20))

# Create the three household task fields.
activity_entries = []
for number in range(1, 4):
    entry = ctk.CTkEntry(
        root,
        width=340,
        placeholder_text=f"Tâche {number} (ex. faire la vaisselle)",
    )
    entry.pack(pady=6)
    activity_entries.append(entry)

# Create the three participant input fields.
participant_entries = []
for number in range(1, 4):
    entry = ctk.CTkEntry(
        root,
        width=340,
        placeholder_text=f"Nom de l'enfant {number}",
    )
    entry.pack(pady=6)
    participant_entries.append(entry)

status_label = ctk.CTkLabel(root, text="")
status_label.pack(pady=(18, 4))

result_label = ctk.CTkLabel(
    root,
    text="Les affectations apparaîtront ici.",
    font=ctk.CTkFont(size=16, weight="bold"),
    wraplength=400,
)
result_label.pack(pady=8)


def load_history():
    """Load the previous daily assignment, if one is available."""
    try:
        with HISTORY_PATH.open(encoding="utf-8") as history_file:
            history = json.load(history_file)
    except (OSError, json.JSONDecodeError):
        return None
    return history if isinstance(history, dict) else None


def save_history(assignments):
    """Persist today's assignment so tomorrow's draw can avoid repeats."""
    with HISTORY_PATH.open("w", encoding="utf-8") as history_file:
        json.dump(
            {"date": date.today().isoformat(), "assignments": assignments},
            history_file,
            ensure_ascii=False,
            indent=2,
        )


def format_assignments(assignments):
    return "\n".join(
        f"{participant} : {activity}"
        for participant, activity in assignments.items()
    )


def choose_assignments(activities, participants, previous_assignments):
    """Choose a random one-to-one assignment without yesterday's repeats."""
    possibilities = []
    for activity_order in itertools.permutations(activities):
        assignment = dict(zip(participants, activity_order))
        if all(
            previous_assignments.get(participant) != activity
            for participant, activity in assignment.items()
        ):
            possibilities.append(assignment)
    return random.choice(possibilities)


def finish_draw(activities, participants, previous_assignments):
    """Choose and display the final assignment for all three children."""
    assignments = choose_assignments(activities, participants, previous_assignments)
    result_label.configure(text=format_assignments(assignments), text_color="#5eead4")
    try:
        save_history(assignments)
        status_label.configure(text="Tirage terminé !")
    except OSError:
        status_label.configure(
            text="Tirage terminé, mais l'historique n'a pas pu être sauvegardé.",
            text_color="#fca5a5",
        )
    draw_button.configure(state="normal")


def animate_draw(activities, participants, previous_assignments, remaining_steps=8):
    """Animate the draw without freezing the application window."""
    if remaining_steps == 0:
        finish_draw(activities, participants, previous_assignments)
        return

    preview = choose_assignments(activities, participants, previous_assignments)
    result_label.configure(text=f"Tirage en cours...\n{format_assignments(preview)}")
    root.after(
        120,
        lambda: animate_draw(
            activities,
            participants,
            previous_assignments,
            remaining_steps - 1,
        ),
    )


def washup():
    """Validate the form and start a random draw."""
    activities = [entry.get().strip() for entry in activity_entries]
    participants = [entry.get().strip() for entry in participant_entries]

    if any(not activity for activity in activities):
        status_label.configure(text="Veuillez entrer les trois tâches.", text_color="#fca5a5")
        result_label.configure(text="Le tirage n'a pas commencé.")
        return

    if len({activity.casefold() for activity in activities}) != 3:
        status_label.configure(
            text="Les trois tâches doivent être différentes.",
            text_color="#fca5a5",
        )
        result_label.configure(text="Le tirage n'a pas commencé.")
        return

    if any(not participant for participant in participants):
        status_label.configure(text="Veuillez entrer les trois noms.", text_color="#fca5a5")
        result_label.configure(text="Le tirage n'a pas commencé.")
        return

    if len({participant.casefold() for participant in participants}) != 3:
        status_label.configure(
            text="Les trois enfants doivent avoir des noms différents.",
            text_color="#fca5a5",
        )
        result_label.configure(text="Le tirage n'a pas commencé.")
        return

    history = load_history()
    today = date.today()
    previous_assignments = {}
    if history and history.get("date") in {
        today.isoformat(),
        (today - timedelta(days=1)).isoformat(),
    }:
        stored_assignments = history.get("assignments", {})
        if isinstance(stored_assignments, dict):
            previous_assignments = stored_assignments

    status_label.configure(text="Bonne chance à tous !", text_color="white")
    result_label.configure(text="Préparation du tirage...", text_color="white")
    draw_button.configure(state="disabled")
    animate_draw(activities, participants, previous_assignments)


def clear_form():
    """Clear all inputs and restore the initial interface state."""
    for entry in activity_entries:
        entry.delete(0, "end")
    for entry in participant_entries:
        entry.delete(0, "end")
    status_label.configure(text="")
    result_label.configure(text="Les affectations apparaîtront ici.", text_color="white")


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

