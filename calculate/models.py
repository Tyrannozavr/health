from django.db import models


# вот сюда вроде по задумке записывается день пятый, ссылка на него и т.д
class Trainings(models.Model):
    h1 = models.CharField(max_length=40)
    slug = models.SlugField()
    description = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)

class Train(models.Model):
    training = models.ForeignKey(Trainings, on_delete=models.CASCADE)
    h2 = models.CharField(max_length=40)
    content = models.CharField(max_length=200)

    # например trainings h1 = день первый slug это к примеру ссылка, можешь заменить просто на charfield
    # дальше, h2 разминка, description = стройность пантеры, content сама тренировка.
    # ниже практические советы и реки они тоже записывааются в train и через fk связывааются с треней, в общем сколько
    # нужно, столько на одной странице и можно добавить

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    video = models.URLField(max_length=30, verbose_name='url для видео', null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    content = models.CharField(max_length=255)


'здесь советы к упражнению, их может быть несколько и их всегда разное кол-во решил вынести в отдельную таблицу'
class Advices(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

class Muscules(models.Model):
    name = models.CharField(max_length=40)
    exercise = models.ManyToManyField(Exercise)


class Dishes(models.Model):
    name = models.CharField(max_length=50)
    calories = models.IntegerField()

# счетчик калорий, каждый день 4 блюда, обед завтрак перекус и ужин
class Tracker(models.Model):
    date = models.DateField(auto_created=True)
    breakfast = models.ForeignKey(Dishes, on_delete=models.SET_NULL, null=True, blank=True,
                                  verbose_name='завтрак', related_name='breakfast')
    launch = models.ForeignKey(Dishes, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='обед', related_name='launch')
    dinner = models.ForeignKey(Dishes, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Ужин', related_name='dinner')
    snack = models.ForeignKey(Dishes, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='перекус', related_name='snack')


class Scrub(models.Model):
    name = models.CharField(max_length=100)
    compound = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    technik = models.TextField()

