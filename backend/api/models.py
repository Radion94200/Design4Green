from django.db import models

class Commune(models.Model):
    department = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    epci = models.CharField(max_length=30)
    population = models.IntegerField()
    score_dep_global = models.IntegerField()
    score_global_epci = models.IntegerField()
    score_global_region = models.IntegerField()
    agg_score_global_region = models.IntegerField()
    geometry = models.CharField(max_length=30)
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    def __init__(self, departement, region, ecpi, population, score_dep_global,
                 score_global_ecpi, score_global_region, agg_score_global_region,
                 geometry, latitude, longitude):
        self.department = departement
        self.region = region
        self.epci = ecpi
        self.population = population
        self.score_dep_global =score_dep_global
        self.score_global_epci = score_global_ecpi
        self.score_global_region = score_global_region
        self.agg_score_global_region = agg_score_global_region
        self.geometry = geometry
        self.latitude = latitude
        self.longitude = longitude
