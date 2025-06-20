import os
import shutil  # Préparation pour les modules suivants

def demander_chemin_dossier():
    """
    Demande un chemin de dossier et vérifie s'il existe.
    """
    while True:
        chemin = input("Entrez le chemin du dossier à classer : ").strip()
        if os.path.isdir(chemin):
            return chemin
        else:
            print("Chemin invalide. Veuillez entrer un dossier qui existe.")

def est_fichier_cache(nom_fichier):
    """
    Vérifie si un fichier est caché (commence par un point).
    """
    return nom_fichier.startswith(".")

def lister_fichiers_recursif(chemin_dossier, ignorer_fichiers_caches=True):
    """
    Liste tous les fichiers du dossier et de ses sous-dossiers.
    Retourne les chemins relatifs.
    """
    fichiers = []
    try:
        for racine, _, noms_fichiers in os.walk(chemin_dossier):
            for nom in noms_fichiers:
                if ignorer_fichiers_caches and est_fichier_cache(nom):
                    continue
                chemin_relatif = os.path.relpath(os.path.join(racine, nom), chemin_dossier)
                fichiers.append(chemin_relatif)
    except Exception as e:
        print(f"Erreur lors de l'accès au dossier : {e}")
    return fichiers

def identifier_extension(nom_fichier):
    """
    Retourne l'extension du fichier, ou None s'il n'en a pas.
    """
    if '.' in nom_fichier:
        ext = os.path.splitext(nom_fichier)[1].lower()
        return ext[1:] if ext else None
    return None

def scanner_dossier(chemin_dossier, ignorer_fichiers_caches=True, recursif=False):
    """
    Scanne le dossier (optionnellement récursif) et retourne :
    - liste des fichiers
    - dictionnaire {extension: [fichiers]}
    - liste des fichiers sans extension
    """
    if recursif:
        fichiers = lister_fichiers_recursif(chemin_dossier, ignorer_fichiers_caches)
    else:
        fichiers = []
        try:
            for nom in os.listdir(chemin_dossier):
                chemin_complet = os.path.join(chemin_dossier, nom)
                if os.path.isfile(chemin_complet):
                    if ignorer_fichiers_caches and est_fichier_cache(nom):
                        continue
                    fichiers.append(nom)
        except Exception as e:
            print(f"Erreur lors de l'accès au dossier : {e}")

    fichiers_par_extension = {}
    sans_extension = []

    for nom_fichier in fichiers:
        ext = identifier_extension(nom_fichier)
        if ext:
            fichiers_par_extension.setdefault(ext.upper(), []).append(nom_fichier)
        else:
            sans_extension.append(nom_fichier)

    return {
        "tous_les_fichiers": fichiers,
        "fichiers_par_extension": fichiers_par_extension,
        "sans_extension": sans_extension
    }
