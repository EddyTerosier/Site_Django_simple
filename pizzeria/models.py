from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=120, unique=True)
    allergens = models.CharField(
        max_length=255,
        blank=True,
        help_text="gluten, lactose, oeufs, soja, etc."
    )

    def __str__(self):
        if self.allergens:
            return f"{self.name} (allergènes : {self.allergens})"
        return self.name

class Pizza(models.Model):
    title = models.CharField(max_length=120)
    prix = models.DecimalField(max_digits=7, decimal_places=2)
    disponible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    ingredients = models.ManyToManyField(
        Ingredient,
        blank=True,
        related_name="pizzas",
        help_text="Ingrédients composant la pizza"
    )

    def __str__(self):
        dispo = "✅" if self.disponible else "⛔"
        return f"{self.title} — {self.prix} € {dispo}"

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="comments")
    auteur = models.CharField(max_length=120)
    texte = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.auteur} sur {self.pizza.title}"