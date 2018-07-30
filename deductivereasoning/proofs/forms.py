from django import forms

class MajorSubmissionForm(forms.Form):
<<<<<<< HEAD
    is_universal_major = forms.BooleanField(required=True)
=======


    is_universal_major = forms.BooleanField(required=True)

>>>>>>> ed15fc71b3c7657b79472404287945d263bac417
    subject_major = forms.CharField(
        max_length=255,
        label='Major subject',
    )
<<<<<<< HEAD
    is_affirmative_major = forms.BooleanField(required=True)
    predicate_major = forms.CharField(
        max_length=255,
        label='Major predicate',
    )
    is_universal_minor = forms.BooleanField(required=True)
    subject_minor = forms.CharField(
        max_length=255,
        label='Major subject',
    )
    is_affirmative_minor = forms.BooleanField(required=True)
    predicate_minor = forms.CharField(
        max_length=255,
        label='Major predicate',
    )
    is_universal_conclusion = forms.BooleanField(required=True)
    subject_conclusion = forms.CharField(
        max_length=255,
        label='Major subject',
    )
    is_affirmative_conclusion = forms.BooleanField(required=True)
    predicate_conclusion = forms.CharField(
        max_length=255,
        label='Major predicate',
=======

    is_affirmative_major = forms.BooleanField(required=True)

    predicate_major = forms.CharField(
        max_length=255,
        label=('Major predicate'),
    )

    is_universal_minor = forms.BooleanField(required=True)

    subject_minor = forms.CharField(
        max_length=255,
        label=('Major subject'),
    )

    is_affirmative_minor = forms.BooleanField(required=True)

    predicate_minor = forms.CharField(
        max_length=255,
        label=('Major predicate'),
    )

    is_universal_conclusion = forms.BooleanField(required=True)

    subject_conclusion = forms.CharField(
        max_length=255,
        label=('Major subject'),
    )

    is_affirmative_conclusion = forms.BooleanField(required=True)

    predicate_conclusion = forms.CharField(
        max_length=255,
        label=('Major predicate'),
>>>>>>> ed15fc71b3c7657b79472404287945d263bac417
    )
