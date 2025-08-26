from django.contrib import admin, messages
from django.db.models import Count
from .models import Pizza, Ingredient, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ("auteur", "texte", "created_at")
    readonly_fields = ("created_at",)


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ["title", "prix", "disponible", "created_at"]
    list_filter = ["disponible", "created_at"]
    search_fields = ["title"]
    ordering = ["disponible", "-created_at"]
    date_hierarchy = "created_at"
    readonly_fields = ["created_at"]
    fields = ["title", "prix", "disponible", "ingredients", "created_at"]
    list_per_page = 10

    actions = ["rendre_disponible", "rendre_indisponible"]

    filter_horizontal = ("ingredients",)
    inlines = [CommentInline]

    def rendre_disponible(self, request, queryset):
        n = queryset.update(disponible=True)
        self.message_user(request, f"{n} pizza(s) rendue(s) disponible(s).", level=messages.SUCCESS)
    rendre_disponible.short_description = "Rendre disponibles"

    def rendre_indisponible(self, request, queryset):
        n = queryset.update(disponible=False)
        self.message_user(request, f"{n} pizza(s) rendue(s) indisponible(s).", level=messages.WARNING)
    rendre_indisponible.short_description = "Rendre indisponibles"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_comment_count=Count("comments"))

    @admin.display(description="Nb commentaires", ordering="_comment_count")
    def nb_comments(self, obj):
        return obj._comment_count

    def get_list_display(self, request):
        base = list(super().get_list_display(request))
        if "nb_comments" not in base:
            base.append("nb_comments")
        return base


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "allergens")
    search_fields = ("name", "allergens")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pizza", "auteur", "created_at")
    search_fields = ("auteur", "texte", "pizza__title")
    list_filter = ("created_at", "pizza")
    date_hierarchy = "created_at"