# 📝 To-Do List — Django (MVT)

Petit projet d'entraînement en **Django traditionnel (MVT)**.  
Fonctionnalités :
- Page d’accueil et page “À propos” avec la date du jour
- Liste des tâches (`/tasks/`) avec compteurs (total, actives, terminées)
- Filtre des tâches actives (`/tasks/active/`)
- Détail d’une tâche (`/tasks/<id>/`)
- Ajout rapide d’une tâche via formulaire
- Bascule terminé/actif (toggle) via bouton
- Interface simple avec un peu de style (sans héritage de templates)

---

## ⚙️ Installation & lancement

1. **Cloner le projet**  
   ```bash
   git clone <url-du-repo>
   cd todoproject
   ```

2. **Créer un environnement virtuel et l’activer**  
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```

3. **Installer les dépendances**  
   ```bash
   pip install django
   ```

4. **Effectuer les migrations**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Créer un superutilisateur (optionnel, pour l’admin)**  
   ```bash
   python manage.py createsuperuser
   ```

6. **Lancer le serveur de développement**  
   ```bash
   python manage.py runserver
   ```
   Puis ouvrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## 📂 Structure principale

```
todoproject/         # projet Django
 ├─ manage.py
 ├─ todoproject/     # configuration globale
 └─ tasks/           # application principale
     ├─ models.py    # modèle Task
     ├─ views.py     # vues (home, about, list, detail, etc.)
     ├─ urls.py      # routes de l’app
     └─ templates/   # templates HTML (home, about, tasks/list, tasks/detail)
```

---

## ✅ Fonctionnalités testées

- Ajout d’une tâche via `/tasks/`
- Compteurs automatiques via ORM (`.all()`, `.filter()`, `.count()`, `.order_by()`)
- Bascule terminé/actif
- Navigation présente sur toutes les pages
- Affichage de la date du jour (format français `JJ/MM/AAAA`)

---

## 🔗 Ressources utiles

- [Documentation Django](https://docs.djangoproject.com/fr/5.0/)
- [Tutoriel officiel Django](https://docs.djangoproject.com/fr/5.0/intro/)

---
