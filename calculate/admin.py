from django.contrib import admin
from .models import Trainings, Train, Exercise, Advices, Muscules, Dishes, Tracker

@admin.register(Trainings)
class TrainingsAdmin(admin.ModelAdmin):
    pass

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    pass

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass

@admin.register(Advices)
class AdvicesAdmin(admin.ModelAdmin):
    pass

@admin.register(Muscules)
class MusculesAdmin(admin.ModelAdmin):
    pass

@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    pass

@admin.register(Tracker)
class TrackerAdmin(admin.ModelAdmin):
    pass
