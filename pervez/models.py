from django.db import models
from embed_video.fields import EmbedVideoField

class Cls(models.Model):
    clss = models.IntegerField(null=True, blank=True)
    # sub = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.clss)


class Subject(models.Model):
    sub_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.sub_type

class Notes(models.Model):
    clss = models.ForeignKey(Cls, null=True, on_delete=models.CASCADE)
    sub = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    notes = models.CharField(max_length=200, null=True)
    notesfile = models.FileField(null=True)

    def __str__(self):
        return self.notes + " " + str(self.clss)

class QuestionAnswer(models.Model):
    clss = models.ForeignKey(Cls, on_delete=models.CASCADE)
    sub = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    question_desc = models.CharField(max_length=200, null=True)
    question = models.FileField(null=True, blank=True)
    answer_desc = models.CharField(max_length=200, null=True)
    answers = models.FileField(null=True, blank=True)


    def __str__(self):
        return "qna "+ str(self.sub) + " " + str(self.clss)

# class Lectures(models.Model):
#     clss = models.ForeignKey(Cls, on_delete=models.CASCADE, null=True)
#     sub = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
#     chaper = models.CharField(null=True, blank=True,max_length=200)
#     link




class Lectures(models.Model):
    subject = (
        ('Physics','Physics'),
        ('Chemistry','Chemistry'),
        ('Maths','Maths'),
    )
    clsses = (
        (7,7),
        (8,8),
        (9,9),
        (10,10),
    )
    chapter = models.CharField(max_length=200, null=True, blank=True)
    clss = models.IntegerField(null=True, choices=clsses, blank=True)
    sub = models.CharField(max_length=200, choices=subject, null=True)

    def __str__(self):
        return self.chapter + " " + str(self.clss)

class SubTopic(models.Model):
    chapter = models.ForeignKey(Lectures, null=True, on_delete=models.CASCADE)
    sub_topic = models.CharField(max_length=200, null=True, blank=True)
    vedio = EmbedVideoField(null=True)

    def __str__(self):
        return str(self.chapter) + self.sub_topic