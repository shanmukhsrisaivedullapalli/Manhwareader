# models.py

from django.db import models

class Manga(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    chapter_number = models.PositiveIntegerField()
    number_of_pictures = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.manga.name} - Chapter {self.chapter_number}"