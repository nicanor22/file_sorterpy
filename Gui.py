import tkinter as tk
from tkinter import filedialog, messagebox
from file_manager import classify_files_by_extension, move_files_to_folders

def run_gui(config):
    def choose_directory():
        path = filedialog.askdirectory()
        if path:
            path_var.set(path)

    def run_sort():
        path = path_var.get()
        if not path:
            messagebox.showerror("Erreur", "Veuillez choisir un dossier.")
            return
        files_by_ext = classify_files_by_extension(path, config)
        move_files_to_folders(files_by_ext, path, config)
        summary = "\n".join([f"{ext}: {len(files)} fichier(s)" for ext, files in files_by_ext.items()])
        messagebox.showinfo("Résumé du tri", summary)

    root = tk.Tk()
    root.title("File Sorter")

    tk.Label(root, text="Choisissez un dossier à trier :").pack(pady=5)
    path_var = tk.StringVar()
    tk.Entry(root, textvariable=path_var, width=50).pack(padx=10)
    tk.Button(root, text="Parcourir", command=choose_directory).pack(pady=5)
    tk.Button(root, text="Lancer le tri", command=run_sort).pack(pady=10)

    root.mainloop()
