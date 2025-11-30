import json
from pathlib import Path #import pojedynczej funkcji Path
from tkinter import messagebox

import customtkinter as ctk


DATA_FILE = Path("people.json")


class PersonForm(ctk.CTk):
    """Simple form that collects and persists personal data."""

    def __init__(self):
        super().__init__()
        self.title("Formularz danych")
        self.geometry("420x260")

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        self._build_widgets()

    def _build_widgets(self) -> None:
        self.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(self, text="Imie:").grid(
            row=0, column=0, padx=16, pady=(20, 10), sticky="e")
        self.first_name_entry = ctk.CTkEntry(self)
        self.first_name_entry.grid(
            row=0, column=1, padx=16, pady=(20, 10), sticky="ew")

        ctk.CTkLabel(self, text="Nazwisko:").grid(
            row=1, column=0, padx=16, pady=10, sticky="e")
        self.last_name_entry = ctk.CTkEntry(self)
        self.last_name_entry.grid(
            row=1, column=1, padx=16, pady=10, sticky="ew")

        ctk.CTkLabel(self, text="Wiek:").grid(
            row=2, column=0, padx=16, pady=10, sticky="e")
        ages = [str(age) for age in range(18, 71)]
        self.age_combobox = ctk.CTkComboBox(
            self, values=ages, state="readonly")
        self.age_combobox.set(ages[0])
        self.age_combobox.grid(row=2, column=1, padx=16, pady=10, sticky="ew")

        self.save_button = ctk.CTkButton(
            self, text="Zapisz", command=self._save_person)
        self.save_button.grid(row=3, column=0, columnspan=2,
                              padx=16, pady=20, sticky="ew")

    def _save_person(self) -> None:
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        age = self.age_combobox.get()

        if not first_name or not last_name:
            messagebox.showwarning("Brak danych", "Uzupelnij imie i nazwisko.")
            return

        record = {
            "firstName": first_name,
            "lastName": last_name,
            "age": int(age),
        }

        existing = []
        if DATA_FILE.exists():
            try:
                existing = json.loads(DATA_FILE.read_text(encoding="utf-8"))
                if not isinstance(existing, list):
                    existing = []
            except json.JSONDecodeError:
                existing = []

        existing.append(record)
        DATA_FILE.write_text(json.dumps(
            existing, indent=2, ensure_ascii=False), encoding="utf-8")

        messagebox.showinfo("Sukces", "Dane zapisane do pliku JSON.")
        self.first_name_entry.delete(0, ctk.END)
        self.last_name_entry.delete(0, ctk.END)
        self.age_combobox.set(str(record["age"]))


def main() -> None:
    app = PersonForm()
    app.mainloop()


if __name__ == "__main__":
    main()
