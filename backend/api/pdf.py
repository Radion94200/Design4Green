from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from rest_framework.response import Response
from xhtml2pdf import pisa
from rest_framework import views

from .models import Commune, Quartier


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
        message = "Nous vous conseillons d'agir auprès des personnes isolées " \
                  "ou éloignées de points d'information/médiation numérique, " \
                  "mais également celles éloignées de points d'information " \
                  "sociale ou administrative ou non locutrice du français " \
                  "afin de faire baisser l'indice."
    else:
        message = "Votre score est suffisant dans cette catégorie."
    return message


def msg_acces_num(score):
    if score > 100:
        message = "Nous vous conseillons d'agir auprès des personnes âgées, " \
                  "des personnes non diplômées ou bien des personnes en " \
                  "situation de handicap afin de faire baisser l'indice."
    else:
        message = "Votre score est suffisant dans cette catégorie."
    return message


def msg_comp_num(score):
    if score > 100:
        message = "Nous vous conseillons d'agir auprès des jeunes, des" \
                  " personnes nées à l'étranger, des personnes en " \
                  "situation de précarité ou bien de celles éloignées " \
                  "des lieux de médiation sociale afin de faire baisser" \
                  " l'indice."
    else:
        message = "Votre score est suffisant dans cette catégorie."
    return message


def msg_comp_admin(score):
    if score > 100:
        message = "Nous vous conseillons d'agir auprès des foyers " \
                  "qui rencontrent des difficultés à s'équiper, " \
                  "notamment celles non équipée d'un ordinateur " \
                  "ou non abonnées à une FAI. Par ailleurs il est " \
                  "aussi possible de vérifier et d'améliorer la qualité " \
                  "et quantité de couverture 2G,THD,HD de votre territoire " \
                  "afin de faire baisser l'indice."
    else:
        message = "Votre score est suffisant dans cette catégorie."
    return message


def init_dic(nom, region, departement):
    dic = {
        "nom": nom,
        "departement": departement,
        "region": region,
        "score_departement": 0,
        "score_region": 0,
        "score": 0,
        "acces_num": 0,
        "acces_info": 0,
        "comp_num": 0,
        "comp_admin": 0,
        "score_acces": 0,
        "score_comp": 0
    }
    return dic


def update_dic(dic, quartiers):
    num = 0
    for i in quartiers:
        num += 1
        dic["score"] += i["score"]
        dic["score_departement"] += i["score_global_dep"]
        dic["score_region"] += i["score_global_region"]
        dic["acces_num"] += i["acces_num"]
        dic["acces_info"] += i["acces_info"]
        dic["comp_admin"] += i["comp_admin"]
        dic["comp_num"] += i["comp_num"]
        dic["score_acces"] += i["score_acces"]
        dic["score_comp"] += i["score_comp"]
    return dic, num


def avg_dic(dic, num):
    dic["score_departement"] = dic["score_departement"] // num
    dic["score_region"] = dic["score_region"] // num
    dic["score"] = dic["score"] // num
    dic["acces_num"] = dic["acces_num"] // num
    dic["acces_info"] = dic["acces_info"] // num
    dic["comp_num"] = dic["comp_num"] // num
    dic["comp_admin"] = dic["comp_admin"] // num
    dic["score_acces"] = dic["score_acces"] // num
    dic["score_comp"] = dic["score_comp"] // num
    dic["msg_acces_info"] = msg_acces_info(dic["acces_info"])
    dic["msg_acces_num"] = msg_acces_num(dic["acces_num"])
    dic["msg_comp_admin"] = msg_comp_admin(dic["comp_admin"])
    dic["msg_comp_num"] = msg_comp_num(dic["comp_num"])
    return dic


def get_pdf(request):
    pdf = None
    if "commune" in request.query_params.keys():
        c_query = Commune.objects.filter(nom=request.query_params[
            "commune"])
        if c_query.exists():
            commune = c_query.get()
            q_query = Quartier.objects.filter(commune=commune)
            quartiers = q_query.values()
            dic = init_dic(commune.nom, commune.departement.region.nom,
                           commune.departement.nom)
            dic, num = update_dic(dic, quartiers)
            dic = avg_dic(dic, num)

            pdf = render_to_pdf('../template/pdf_template.html', dic)
    return pdf


class ViewPDF(views.APIView):
    def get(self, request):
        pdf = get_pdf(request)
        if pdf is not None:
            response = HttpResponse(pdf, content_type='application/pdf')
        else:
            response = Response({})
        return response


class DownloadPDF(views.APIView):
    def get(self, request):
        pdf = get_pdf(request)
        if pdf is not None:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Rapport_%s.pdf" % request.query_params["commune"]
            content = "attachment; filename=%s" % filename
            response['Content-Disposition'] = content
        else:
            response = Response({})
        return response
