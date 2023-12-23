from django import forms
from .models import ConcernMessage

from .models import ConversationMessage

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={"class": "w-full py-4 px-6 rounded-xl border"}
            )
        }


class ConcernMessageForm(forms.ModelForm):
    class Meta:
        model = ConcernMessage
        fields = ("name", "email", "message")
        widgets = {
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "email": forms.EmailInput(attrs={"class": INPUT_CLASSES}),
            "message": forms.Textarea(attrs={"class": INPUT_CLASSES, "rows": 4}),
        }
