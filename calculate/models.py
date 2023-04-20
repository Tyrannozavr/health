from django.db import models


class Trainings(models.Model):
    h1 = models.CharField(max_length=40)
    slug = models.SlugField()
    description = models.CharField(max_length=50)

class Train(models.Model):
    training = models.ForeignKey(Trainings, on_delete=models.CASCADE)
    h2 = models.CharField(max_length=40)
    content = models.CharField(max_length=200)

    # например trainings h1 = день первый slug это к примеру ссылка, можешь заменить просто на charfield
    # дальше, h2 разминка, description = стройность пантеры, content сама тренировка.
    # ниже практические советы и реки они тоже записывааются в train и через fk связывааются с треней, в общем сколько
    # нужно, столько на одной странице и можно добавить