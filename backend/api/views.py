from rest_framework import viewsets, views
from rest_framework.response import Response

from api.serializers import *
import pandas as pd


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class DepartementViewSet(viewsets.ModelViewSet):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer


class CommuneViewSet(viewsets.ModelViewSet):
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializer
    filter_fields = ["nom"]


class QuartierViewSet(viewsets.ModelViewSet):
    queryset = Quartier.objects.all()
    serializer_class = QuartierSerializer


class GenerateDBView(views.APIView):
    def get(self, request):
        #df_communes = pd.read_csv(f"../input_bdd/infos-communes.csv", sep='\t',
        #                          encoding="utf-16")
        df_regions = pd.read_csv(f"../input_bdd/infos-regions.csv", sep='\t',
                                 encoding="utf-16")
        #df_regions = df_regions.sort_values("Libcom")
        #df_communes = df_communes.sort_values("Nom Com")
        for _, row in df_regions.iterrows():
            reg_query = Region.objects.filter(nom=row["Libreg"])
            if reg_query.exists():
                reg = reg_query.get()
            else:
                reg = Region(
                    nom=row["Libreg"]
                )
                reg.save()

            dep_query = Departement.objects.filter(nom=row["Libdep"])
            if dep_query.exists():
                dep = dep_query.get()
            else:
                dep = Departement(
                    nom=row["Libdep"],
                    region=reg
                )
                dep.save()

            com_query = Commune.objects.filter(nom=row["Libcom"])
            if com_query.exists():
                com = com_query.get()
            else:
                com = Commune(
                    nom=row["Libcom"],
                    department=dep
                )
                com.save()

            Q = Quartier(
                commune=com,
                score_global_dep=int(float(row["SCORE GLOBAL departement 1"].replace(',', '.'))),
                score_global_region=int(float(row["SCORE GLOBAL region 1"].replace(',', '.'))),
                population=int(float(row["P16 Pop"].replace(',', '.'))),
                latitude=float(row["Latitude (générée)"].replace(',', '.')),
                longitude=float(row["Longitude (générée)"].replace(',', '.'))
            )
            Q.save()

        return Response({})
