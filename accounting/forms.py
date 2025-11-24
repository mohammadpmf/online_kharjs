from django.forms import ModelForm

from accounting.models import Kharj


class AddKharjForm(ModelForm):
    class Meta:
        model = Kharj
        fields = [
            "title",
            "type",
            "day_of_week",
            "day_of_month",
            "month",
            "year",
            "price",
        ]
