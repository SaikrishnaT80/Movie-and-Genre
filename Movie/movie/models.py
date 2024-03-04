from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length = 200,unique = True)
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.name
    


class Movie(models.Model):
    title = models.CharField(max_length = 200)
    language = models.CharField(max_length = 20)
    release_date = models.DateField()
    duration = models.CharField(max_length = 20)
    summary = models.CharField(max_length = 600)
    genre = models.ForeignKey(Genre,on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.title
    

    


