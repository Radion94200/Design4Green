from rest_framework import viewsets, views, filters
from rest_framework.response import Response

from api.serializers import RegionSerializer
from api.serializers import DepartementSerializer
from api.serializers import CommuneSerializer
from api.serializers import QuartierSerializer

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
    search_fields = ['^nom']
    filter_backends = (filters.SearchFilter,)


class QuartierViewSet(viewsets.ModelViewSet):
    queryset = Quartier.objects.all()
    serializer_class = QuartierSerializer


class GenerateDBView(views.APIView):
    def get(self, request):
        df_communes = pd.read_csv(f"../input_bdd/infos-communes.csv", sep='\t',
                                  encoding="utf-16")
        df_regions = pd.read_csv(f"../input_bdd/infos-regions.csv", sep='\t',
                                 encoding="utf-16")

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
                    departement=dep
                )
                com.save()

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

        return Response({})
