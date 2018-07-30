from django.db import models



def universal(universal):
    if universal == True:
        return "All"
    else:
        return "Some"

def affirmative(affirmative):
    if affirmative == True:
        return "Are"
    else:
        return "Are not"

class Proposition(models.Model):
    """

    """
    is_universal = models.BooleanField()
    subject = models.CharField(max_length=30)
    is_affirmative = models.BooleanField()
    predicate = models.CharField(max_length=30)
    type = models.CharField(max_length=5,default="",blank=True)

    def __str__(self):
        return universal(self.is_universal) + " " + self.subject + " " + affirmative(self.is_affirmative) + " " + self.predicate

class Proof(models.Model):
    """

    """
    major = models.ForeignKey(
        Proposition,
        related_name='major',
        on_delete=models.CASCADE,
    )
    minor = models.ForeignKey(
        Proposition,
        related_name='minor',
        on_delete=models.CASCADE,
    )
    conclusion = models.ForeignKey(
        Proposition,
        related_name='conclusion',
        on_delete=models.CASCADE,
    )
    type = models.CharField(max_length=5,default="")

    def __str__(self):
        return  (universal(self.major.is_universal)+ " " + self.major.subject + " " + affirmative(self.major.is_affirmative) + " " + self.major.predicate + "___" 
            + universal(self.minor.is_universal)+ " " + self.minor.subject + " " + affirmative(self.minor.is_affirmative) + " " + self.minor.predicate + "___" 
            + universal(self.conclusion.is_universal)+ " " + self.conclusion.subject + " " + affirmative(self.conclusion.is_affirmative) + " " + self.conclusion.predicate)

