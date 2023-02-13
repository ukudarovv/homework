from django.db import models


class Child(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя', blank=True)

    class Meta:
        verbose_name = 'Ребенок'
        verbose_name_plural = 'Дети'

    def __str__(self):
        return "{}".format(self.name)


class Parent(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя', blank=True)
    children = models.ManyToManyField(Child)

    class Meta:
        verbose_name = 'Родитель'
        verbose_name_plural = 'Родители'

    def __str__(self):
        return "{}".format(self.name)
