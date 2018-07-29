from django.forms import ModelForm
from django.db.models import fields
from proofs.models import *

class MajorSubmissionForm(ModelForm):
    class Meta:
        model = Proposition
        fields = {"is_universal","is_affirmative","subject", "predicate",}
