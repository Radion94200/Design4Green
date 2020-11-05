from django.db import models


class Region(models.Model):
    nom = models.CharField(max_length=255)


class Departement(models.Model):
    nom = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class Commune(models.Model):
    nom = models.CharField(max_length=255)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)

    def quartiers(self):
        return Quartier.objects\
            .filter(commune__nom=self.nom)\
            .values(
                "id",
                "score",
                "score_acces",
                "score_comp",
                "score_global_dep",
                "score_global_region",
                "population",
                "acces_num",
                "acces_info",
                "comp_admin",
                "comp_num",
                "code_iris",
                "latitude",
                "longitude"
            )


class Quartier(models.Model):
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    # Score par rapport Region / Departement
    score_global_dep = models.IntegerField(default=-1)
    score_global_region = models.IntegerField(default=-1)
    score = models.IntegerField(default=-1)
    # Map
    code_iris = models.CharField(max_length=255, default="")
    geojson = models.TextField(default="")
    # Indicateurs
    population = models.IntegerField(default=-1)
    acces_num = models.IntegerField(default=-1)
    acces_info = models.IntegerField(default=-1)
    comp_admin = models.IntegerField(default=-1)
    comp_num = models.IntegerField(default=-1)
    score_acces = models.IntegerField(default=-1)
    score_comp = models.IntegerField(default=-1)
    # Geographie
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
