from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.urls import path
from rest_framework import views
from . import pdf
from .models import *
from rest_framework.response import Response


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def msg_acces_info(score):
    if score > 100:
        message ="Nous vous conseillons d'agir auprès des personnes isolées ou éloignées de points d'information/médiation numérique, mais également celles éloignées de points d'information sociale ou administrative ou non locutrice du français afin de faire baisser l'indice."    
    else:
        message = "Votre score est suffisant dans cette catégorie."
    return message

def msg_acces_num(score):
    if score > 100:
        message ="Nous vous conseillons d'agir auprès des personnes âgées, des personnes non diplômées ou bien des personnes en situation de handicap afin de faire baisser l'indice."  
    else:
        message = "Votre score est suffisant dans cette catégorie."
    return message

def msg_comp_num(score):
    if score > 100:
        message = "Nous vous conseillons d'agir auprès des jeunes, des personnes nées à l'étranger, des personnes en situation de précarité ou bien de celles éloignées des lieux de médiation sociale afin de faire baisser l'indice."
    else:
        message = "Votre score est suffisant dans cette catégorie."
    return message

def msg_comp_admin(score):
    if score > 100:
        message = " Nous vous conseillons d'agir auprès des foyers qui rencontrent des difficultés à s'équiper, notamment celles non équipée d'un ordinateur ou non abonnées à une FAI. Par ailleurs il est aussi possible de vérifier et d'améliorer la qualité et quantité de couverture 2G,THD,HD de votre territoire afin de faire baisser l'indice."
    else:
        message = "Votre score est suffisant dans cette catégorie."
    return message




class ViewPDF(views.APIView):
    def get(self, request):
        if "commune" in request.query_params.keys():
            c_query = Commune.objects.filter(nom=request.query_params[
                "commune"])
        if c_query.exists():
            commune = c_query.get()
            q_query = Quartier.objects.filter(commune=commune)
            quartiers = q_query.values()
            score_global,dep,reg,population,acces_num,acces_info=0,0,0,0,0,0
            comp_admin, comp_num, score_acces, score_comp, num = 0,0,0,0,0
            for i in quartiers:
                num += 1
                score_global += i["score"]
                dep += i["score_global_dep"]
                reg += i["score_global_region"]
                population += i["population"]
                acces_num += i["acces_num"]
                acces_info += i["acces_info"]
                comp_admin += i["comp_admin"]
                comp_num += i["comp_num"]
                score_acces += i["score_acces"]
                score_comp += i["score_comp"]
            nom = commune.nom
            departement = commune.departement.nom
            region = commune.departement.region.nom
            dic = {
                "nom": nom,
                "departement": departement,
                "region": region,
                "score_departement": dep//num,
                "score_region": reg//num,
                "score": score_global//num,
                "acces_num": acces_num//num,
                "acces_info": acces_info//num,
                "comp_num": comp_num//num,
                "comp_admin": comp_admin//num,
                "score_acces": score_acces//num,
                "score_comp": score_comp//num, 
                "msg_acces_info": msg_acces_info(acces_info//num),
                "msg_acces_num": msg_acces_info(acces_num//num),
                "msg_comp_admin": msg_comp_admin(comp_admin//num),
                "msg_comp_num": msg_comp_num(comp_num//num)
                }
        pdf = render_to_pdf('../template/pdf_template.html', dic)
        return HttpResponse(pdf, content_type='application/pdf')


# Automaticly downloads to PDF file
class DownloadPDF(views.APIView):
    def get(self, request):

        pdf = render_to_pdf('../template/pdf_template.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" % ("12341231")
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response


def index(request):
    context = {}
    return render(request, '../template/index.html', context)
