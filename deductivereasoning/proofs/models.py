from django.db import models


class Proposition(models.Model):
    """

    """
    is_universal = models.BooleanField()
    subject = models.CharField(max_length=30)
    is_affirmative = models.BooleanField()
    predicate = models.CharField(max_length=30)
    type = models.CharField(max_length=5,default="",blank=True)


    def setPropositionType(self):
        if(self.is_universal==True and self.is_affirmative==True):
            self.type = "A"
        elif(self.is_universal==True and self.is_affirmative==False):
            self.type = "I"
        elif (self.is_universal == False and self.is_affirmative == True):
            self.type = "E"
        else:
            self.type = "O"

    def __str__(self):
        return  str(self.is_universal) + " " + self.subject + " " + str(self.is_affirmative) + " " + self.predicate

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
    type = models.CharField(max_length=1,default="")

    def __str__(self):
        return  self.major.subject + " " + self.major.predicate + "/n" + self.minor.subject + " " + self.minor.predicate + "/n" + self.conclusion.subject + " " + self.conclusion.predicate
