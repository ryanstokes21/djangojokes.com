from django.contrib import admin

# Register your models here.
from .models import Joke


@admin.register(Joke)
class JokeAdmin(admin.ModelAdmin):
    model = Joke
    list_display = ['question', 'created', 'updated']  # noqa: RUF012

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('slug','created', 'updated')
        return ()