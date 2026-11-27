from django.forms import ModelForm, Textarea

from .models import Joke

class JokeForm(ModelForm):
    class Meta:
        model = Joke
        fields = ['question', 'answer', 'category', 'tags']
        widgets = {  # noqa: RUF012
            'question': Textarea(
                attrs={'cols': 80, 'rows': 3, 'autofocus': True}
            ),
            'answer': Textarea(
                attrs={'cols': 80, 'rows': 3, 'placeholder': 'Make it funny'}
            )
        }
        help_texts = {  # noqa: RUF012
            'question': 'No dirty jokes please.',
            'tags': 'Use Ctrl-click to select multiple tags.'
        }