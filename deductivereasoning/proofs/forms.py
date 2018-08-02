from django import forms


TRUE_FALSE_CHOICES_UNIVERSAL = (
    (True, 'All'),
    (False, 'Some')
)
TRUE_FALSE_CHOICES_AFFIRMATIVE = (
    (True, 'Are'),
    (False, 'Are not')
)
class MajorSubmissionForm(forms.Form):
    is_universal_major = forms.ChoiceField(
        choices=TRUE_FALSE_CHOICES_UNIVERSAL,
        required=True,
        label="Universal",
        widget=forms.Select,
    )
    subject_major = forms.CharField(
        max_length=255,
        label='Major subject',
        required=False
    )
    is_affirmative_major = forms.ChoiceField(
        choices=TRUE_FALSE_CHOICES_AFFIRMATIVE,
        required=True,
        label="Universal",
        widget=forms.Select,
        )
    predicate_major = forms.CharField(
        max_length=255,
        label='Major predicate',
        required=False
    )
    is_universal_minor = forms.ChoiceField(
        choices=TRUE_FALSE_CHOICES_UNIVERSAL,
        required=True,
        label="Universal",
        widget=forms.Select,
    )
    subject_minor = forms.CharField(
        max_length=255,
        label='Major subject',
        required=False
    )
    is_affirmative_minor = forms.ChoiceField(
        choices=TRUE_FALSE_CHOICES_AFFIRMATIVE,
        required=True,
        label="Universal",
        widget=forms.Select,
    )
    predicate_minor = forms.CharField(
        max_length=255,
        label='Major predicate',
        required=False
    )
    is_universal_conclusion = forms.ChoiceField(
        choices=TRUE_FALSE_CHOICES_UNIVERSAL,
        required=True,
        label="Universal",
        widget=forms.Select,
    )
    subject_conclusion = forms.CharField(
        label='Major subject',
        required=False,
        widget=forms.Select,
    )
    is_affirmative_conclusion = forms.ChoiceField(
        choices=TRUE_FALSE_CHOICES_AFFIRMATIVE,
        required=True,
        label="Universal",
        widget=forms.Select,
        )
    predicate_conclusion = forms.CharField(
        label='Major predicate',
        required=False,
        widget=forms.Select,
)