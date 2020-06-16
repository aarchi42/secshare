from django.forms import ModelForm
from .models import Verification


class Verifyform(ModelForm):
    class Meta:
        model = Verification
        fields = ['verify']
