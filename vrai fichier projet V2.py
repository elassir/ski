
import tkinter as tk
from tkinter import messagebox, simpledialog


class Sommet:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droit = None

class ArbreB:
    def __init__(self):
        self.racine = None

    def inserer(self, valeur, noeud=None): #noeud=racine comme point de depart
        if self.racine is None:
            self.racine = Sommet(valeur)
        else:
            if noeud is None:
                noeud = self.racine
                
            if valeur < noeud.valeur:
                if noeud.gauche is None:
                    noeud.gauche = Sommet(valeur)
                else:
                    self.inserer(valeur, noeud.gauche)
            else:
                if noeud.droit is None:
                    noeud.droit = Sommet(valeur)
                else:
                    self.inserer(valeur, noeud.droit)

    
    def supprimer(self, valeur, noeud=None, parent=None):
        if self.racine is None:
            return

        if noeud is None:
            noeud = self.racine

        if valeur < noeud.valeur:
            if noeud.gauche is not None:
                self.supprimer(valeur, noeud.gauche, noeud)
        elif valeur > noeud.valeur:
            if noeud.droit is not None:
                self.supprimer(valeur, noeud.droit, noeud)
        else:  # valeur == noeud.valeur
            if noeud.gauche is not None and noeud.droit is not None:  # noeud avec deux enfants
                noeud.valeur = self.valeur_min(noeud.droit)
                self.supprimer(noeud.valeur, noeud.droit, noeud)
            elif parent is None:  # noeud à supprimer est la racine
                if noeud.gauche is not None:
                    self.racine = noeud.gauche
                else:
                    self.racine = noeud.droit
            elif parent.gauche == noeud:  # noeud à supprimer est le fils gauche
                parent.gauche = noeud.gauche if noeud.gauche is not None else noeud.droit
            else:  # noeud à supprimer est le fils droit
                parent.droit = noeud.gauche if noeud.gauche is not None else noeud.droit

    def valeur_min(self, noeud):
        if noeud.gauche is None:
            return noeud.valeur
        return self.valeur_min(noeud.gauche)
    
    def modifier(self, ancienne_valeur, nouvelle_valeur, noeud=None):
        if self.racine is None:
            return

        if noeud is None:
            noeud = self.racine

        if ancienne_valeur < noeud.valeur:
            if noeud.gauche is not None:
                self.modifier(ancienne_valeur, nouvelle_valeur, noeud.gauche)
        elif ancienne_valeur > noeud.valeur:
            if noeud.droit is not None:
                self.modifier(ancienne_valeur, nouvelle_valeur, noeud.droit)
        else:  # ancienne_valeur == noeud.valeur
            noeud.valeur = nouvelle_valeur
    
    
    def rechercher(self, valeur, noeud=None):
        if self.racine is None:
            return False

        if noeud is None:
            noeud = self.racine

        if valeur < noeud.valeur:
            if noeud.gauche is not None:
                return self.rechercher(valeur, noeud.gauche)
            return False
        elif valeur > noeud.valeur:
            if noeud.droit is not None:
                return self.rechercher(valeur, noeud.droit)
            return False
        else:  # valeur == noeud.valeur
            return True
    
    def fusion(self, autre_arbre):
        if autre_arbre.racine is not None:
            self.fusion_recursif(autre_arbre.racine)

    def fusion_recursif(self, noeud):
        if noeud is None:
            return
        self.inserer(noeud.valeur)
        self.fusion_recursif(noeud.gauche)
        self.fusion_recursif(noeud.droit)

    
    
    def decomposition(self, pivot):
        arbre_inf = ArbreB()
        arbre_sup = ArbreB()
        self.decomposition_recursif(pivot, self.racine, arbre_inf, arbre_sup)
        return arbre_inf, arbre_sup

    def decomposition_recursif(self, pivot, noeud, arbre_inf, arbre_sup):
        if noeud is None:
            return
        if noeud.valeur < pivot:
            arbre_inf.inserer(noeud.valeur)
            self.decomposition_recursif(pivot, noeud.gauche, arbre_inf, arbre_sup)
            self.decomposition_recursif(pivot, noeud.droit, arbre_inf, arbre_sup)
        else:
            arbre_sup.inserer(noeud.valeur)
            self.decomposition_recursif(pivot, noeud.gauche, arbre_inf, arbre_sup)
            self.decomposition_recursif(pivot, noeud.droit, arbre_inf, arbre_sup)

    
# Exemple d'utilisation


# Copiez ici les classes Sommet et ArbreB avec toutes les méthodes définies précédemment

class SimpleArbreApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Arbre Binaire - Insertion")
        self.geometry("800x600")
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.current_tree_index = 0
        self.arbres = []
        self.arbre_counter = 0
        self.create_widgets()

    def create_widgets(self):
        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.create_tree_button = tk.Button(self.bottom_frame, text="Créer un arbre", command=self.create_tree)
        self.create_tree_button.pack(side=tk.LEFT)

        self.previous_tree_button = tk.Button(self.bottom_frame, text="Précédent", command=self.previous_tree, state=tk.DISABLED)
        self.previous_tree_button.pack(side=tk.LEFT)

        self.next_tree_button = tk.Button(self.bottom_frame, text="Suivant", command=self.next_tree, state=tk.DISABLED)
        self.next_tree_button.pack(side=tk.LEFT)

    def show_operations(self):
        self.insert_button = tk.Button(self.bottom_frame, text="Insérer", command=self.insert_value)
        self.insert_button.pack(side=tk.LEFT)

        self.delete_button = tk.Button(self.bottom_frame, text="Supprimer", command=self.delete_value)
        self.delete_button.pack(side=tk.LEFT)

        self.modify_button = tk.Button(self.bottom_frame, text="Modifier", command=self.modify_value)
        self.modify_button.pack(side=tk.LEFT)

        self.search_button = tk.Button(self.bottom_frame, text="Rechercher", command=self.search_value)
        self.search_button.pack(side=tk.LEFT)

        self.fusion_button = tk.Button(self.bottom_frame, text="Fusion", command=self.fusion_arbres)
        self.fusion_button.pack(side=tk.LEFT)

        self.tree_label = tk.Label(self.bottom_frame, text=f"Arbre n°{self.arbre_counter}")
        self.tree_label.pack(side=tk.LEFT)
        
        self.decomposition_button = tk.Button(self.bottom_frame, text="Décomposer", command=self.decomposition)
        self.decomposition_button.pack(side=tk.LEFT)
    
    def fusion_arbres(self):
        arbre1, arbre2 = self.select_trees()

        if arbre1 and arbre2:
            arbre1.fusion(arbre2)
            self.draw_tree()
            messagebox.showinfo("Fusion", "Les arbres ont été fusionnés.")
            
    
    
         
    def select_trees(self):
        tree_indices = [f"Arbre n°{i+1}" for i in range(len(self.arbres))]
        tree1_index = simpledialog.askstring("Sélectionner l'arbre 1", f"Sélectionnez l'arbre 1 à fusionner:\n{', '.join(tree_indices)}")
        tree2_index = simpledialog.askstring("Sélectionner l'arbre 2", f"Sélectionnez l'arbre 2 à fusionner:\n{', '.join(tree_indices)}")

        try:
            tree1_index = int(tree1_index) - 1
            tree2_index = int(tree2_index) - 1
            if tree1_index < 0 or tree1_index >= len(self.arbres) or tree2_index < 0 or tree2_index >= len(self.arbres):
                raise ValueError
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des indices d'arbres valides.")
            return None, None

        return self.arbres[tree1_index], self.arbres[tree2_index]
    
    
              
    def create_tree(self):
        self.arbre = ArbreB()
        self.arbres.append(self.arbre)
        self.arbre_counter += 1
        self.draw_tree()
        messagebox.showinfo("Création d'arbre", f"Un nouvel arbre vide a été créé. (Arbre n°{self.arbre_counter})")
        if self.arbre_counter == 1:
            self.show_operations()
        else:
            self.tree_label.config(text=f"Arbre n°{self.arbre_counter}")
    

    def delete_value(self):
        value = self.get_value("Supprimer une valeur")
        if value is not None:
            self.arbre.supprimer(value)
            self.draw_tree()

    def modify_value(self):
        old_value = self.get_value("Ancienne valeur à modifier")
        if old_value is not None:
            new_value = self.get_value("Nouvelle valeur à attribuer")
            if new_value is not None:
                self.arbre.modifier(old_value, new_value)
                self.draw_tree()

    def search_value(self):
        value = self.get_value("Rechercher une valeur")
        if value is not None:
            found = self.arbre.rechercher(value)
            messagebox.showinfo("Recherche", f"Valeur {value} {'trouvée' if found else 'non trouvée'} dans l'arbre.")
    def insert_value(self):
        value = self.get_value("Insérer une valeur")
        if value is not None:
            self.arbre.inserer(value)
            self.draw_tree()

    def get_value(self, prompt):
        value = None
        while value is None:
            try:
                value = int(simpledialog.askstring(prompt, "Entrez une valeur entière :"))
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer un entier valide.")
        return value

    def draw_tree(self):
        self.canvas.delete("all")
        self._draw_tree_recursively(self.arbre.racine, 400, 30, 200)

    def _draw_tree_recursively(self, noeud, x, y, dx):
        if noeud is None:
            return

        self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="white", outline="black")
        self.canvas.create_text(x, y, text=str(noeud.valeur))

        if noeud.gauche is not None:
            self.canvas.create_line(x, y + 15, x - dx, y + 45)
            self._draw_tree_recursively(noeud.gauche, x - dx, y + 60, dx / 2)

        if noeud.droit is not None:
            self.canvas.create_line(x, y + 15, x + dx, y + 45)
            self._draw_tree_recursively(noeud.droit, x + dx, y + 60, dx / 2)

if __name__ == "__main__":
    app = SimpleArbreApp()
    app.mainloop()