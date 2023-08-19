import datetime
import pytz

from django import forms
from django.core.exceptions import ValidationError

from todo.models import Tag, Task


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    deadline = forms.DateTimeField(required=False)  # to remove UI null validation

    class Meta:
        model = Task
        fields = "__all__"

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        created_at = datetime.datetime.now(tz=pytz.UTC)
        if deadline and created_at and deadline <= created_at:
            raise ValidationError("Deadline must be later than creation date.")
        return deadline
