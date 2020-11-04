from django.db import models


class Region(models.Model):
    nom = models.CharField(max_length=255)


class Departement(models.Model):
    nom = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class Commune(models.Model):
    nom = models.CharField(max_length=255)
    department = models.ForeignKey(Departement, on_delete=models.CASCADE)


class Quartier(models.Model):
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    # Score par rapport Region / Departement
    score_global_dep = models.IntegerField()
    score_global_region = models.IntegerField()
    #score = models.IntegerField()
    # Indicateurs
    population = models.IntegerField()
    #acces_num = models.IntegerField()
    #acces_info = models.IntegerField()
    #comp_admin = models.IntegerField()
    #comp_num = models.IntegerField()
    #score_acces = models.IntegerField()
    #score_comp = models.IntegerField()
    # Geographie
    latitude = models.FloatField()
    longitude = models.FloatField()
