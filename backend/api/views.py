import json
import pandas as pd
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, views, filters
from rest_framework.response import Response

from api.serializers import RegionSerializer, DepartementSerializer, \
    CommuneSerializer, QuartierSerializer
from api.models import Region, Departement, Commune, Quartier


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class DepartementViewSet(viewsets.ModelViewSet):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer


class CommuneViewSet(viewsets.ModelViewSet):
    queryset = Commune.objects.all().order_by('nom')
    serializer_class = CommuneSerializer
    search_fields = ['^nom']
    filter_fields = ['nom']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)


class QuartierViewSet(viewsets.ModelViewSet):
    queryset = Quartier.objects.all()
    serializer_class = QuartierSerializer


def complete_data():
    df_communes = pd.read_csv(f"../input_bdd/infos-communes.csv", sep='\t',
                              encoding="utf-16")

    for _, row in df_communes.iterrows():
        q_query = Quartier.objects.filter(
            population=int(row["Population"].replace("\xa0", "")),
            commune__nom=row["Nom Com"], code_iris=""
        )
        if q_query.exists():
            if len(q_query.values()) >= 1:
                Q = q_query.all()[0]
            else:
                Q = q_query.get()
            Q.code_iris = row["Code Iris"]
            Q.score = int(row["SCORE GLOBAL "])
            Q.acces_num = int(row["ACCÈS AUX INTERFACES NUMERIQUES"])
            Q.acces_info = int(row["ACCES A L'INFORMATION"])
            Q.comp_admin = int(row["COMPETENCES ADMINISTATIVES"])
            Q.comp_num = int(row["COMPÉTENCES NUMÉRIQUES / SCOLAIRES"])
            Q.score_acces = int(row["GLOBAL ACCES"])
            Q.score_comp = int(row["GLOBAL COMPETENCES"])
            Q.save()

        for Q in Quartier.objects.all():
            if Q.acces_info == -1:
                Q.delete()


def add_geojson():
    with open('../input_bdd/contours-iris.geojson') as fd:
        geojson_str = fd.read()
    geojson = json.loads(geojson_str)
    for q in geojson["features"]:
        query = Quartier.objects.filter(
            code_iris=q["properties"]["code_iris"], geojson="")
        if query.exists():
            Q = query.get()
            Q.geojson = q
            Q.save()


class GenerateDBView(views.APIView):
    def get(self, request):
        df_regions = pd.read_csv(f"../input_bdd/infos-regions.csv", sep='\t',
                                 encoding="utf-16")

        for _, row in df_regions.iterrows():
            reg, _ = Region.objects.get_or_create(nom=row["Libreg"])
            dep, _ = Departement.objects.get_or_create(nom=row["Libdep"],
                                                       region=reg)
            com, _ = Commune.objects.get_or_create(nom=row["Libcom"],
                                                   departement=dep)

            Q = Quartier(
                commune=com,
                score_global_dep=int(float(row["SCORE GLOBAL departement 1"]
                                           .replace(',', '.'))),
                score_global_region=int(float(row["SCORE GLOBAL region 1"]
                                              .replace(',', '.'))),
                population=int(float(row["P16 Pop"].replace(',', '.'))),
                latitude=float(row["Latitude (générée)"].replace(',', '.')),
                longitude=float(row["Longitude (générée)"].replace(',', '.'))
            )
            Q.save()

        complete_data()
        add_geojson()

        return Response({})
