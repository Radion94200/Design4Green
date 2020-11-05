from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.urls import path
from . import pdf

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


data = { 
"id": 1,
            "nom": "Liévin",
            "departement": "PAS DE CALAIS",
            "region": "HAUTS DE FRANCE",
            "quartiers": [
                {
                    "id": 1313,
                    "score": 132,
                    "score_acces": 158,
                    "score_comp": 107,
                    "score_global_dep": 136,
                    "score_global_region": 132,
                    "population": 1569,
                    "acces_num": 81,
                    "acces_info": 196,
                    "comp_admin": 126,
                    "comp_num": 97,
                    "code_iris": "625100502",
                    "latitude": 50.425182626,
                    "longitude": 2.762660025
                },
                {
                    "id": 12974,
                    "score": 103,
                    "score_acces": 100,
                    "score_comp": 106,
                    "score_global_dep": 105,
                    "score_global_region": 103,
                    "population": 2551,
                    "acces_num": 81,
                    "acces_info": 109,
                    "comp_admin": 106,
                    "comp_num": 106,
                    "code_iris": "625100601",
                    "latitude": 50.435390589,
                    "longitude": 2.757943777
                },
                {
                    "id": 13317,
                    "score": 103,
                    "score_acces": 96,
                    "score_comp": 109,
                    "score_global_dep": 104,
                    "score_global_region": 103,
                    "population": 2419,
                    "acces_num": 81,
                    "acces_info": 103,
                    "comp_admin": 89,
                    "comp_num": 120,
                    "code_iris": "625100602",
                    "latitude": 50.42334407,
                    "longitude": 2.75682565
                },
                {
                    "id": 15928,
                    "score": 99,
                    "score_acces": 88,
                    "score_comp": 111,
                    "score_global_dep": 101,
                    "score_global_region": 99,
                    "population": 301,
                    "acces_num": 81,
                    "acces_info": 92,
                    "comp_admin": 102,
                    "comp_num": 115,
                    "code_iris": "625100603",
                    "latitude": 50.429109876,
                    "longitude": 2.743475472
                },
                {
                    "id": 16293,
                    "score": 99,
                    "score_acces": 90,
                    "score_comp": 109,
                    "score_global_dep": 101,
                    "score_global_region": 99,
                    "population": 2205,
                    "acces_num": 81,
                    "acces_info": 94,
                    "comp_admin": 100,
                    "comp_num": 113,
                    "code_iris": "625100201",
                    "latitude": 50.415687839,
                    "longitude": 2.794484628
                },
                {
                    "id": 17238,
                    "score": 98,
                    "score_acces": 89,
                    "score_comp": 107,
                    "score_global_dep": 100,
                    "score_global_region": 98,
                    "population": 2369,
                    "acces_num": 81,
                    "acces_info": 93,
                    "comp_admin": 96,
                    "comp_num": 113,
                    "code_iris": "625100503",
                    "latitude": 50.424414229,
                    "longitude": 2.769821099
                },
                {
                    "id": 17727,
                    "score": 98,
                    "score_acces": 100,
                    "score_comp": 96,
                    "score_global_dep": 100,
                    "score_global_region": 98,
                    "population": 2139,
                    "acces_num": 81,
                    "acces_info": 109,
                    "comp_admin": 101,
                    "comp_num": 93,
                    "code_iris": "625100501",
                    "latitude": 50.429146568,
                    "longitude": 2.765940475
                },
                {
                    "id": 19737,
                    "score": 96,
                    "score_acces": 90,
                    "score_comp": 101,
                    "score_global_dep": 97,
                    "score_global_region": 96,
                    "population": 2858,
                    "acces_num": 81,
                    "acces_info": 95,
                    "comp_admin": 109,
                    "comp_num": 97,
                    "code_iris": "625100401",
                    "latitude": 50.436891116,
                    "longitude": 2.77484039
                },
                {
                    "id": 21004,
                    "score": 94,
                    "score_acces": 82,
                    "score_comp": 107,
                    "score_global_dep": 96,
                    "score_global_region": 94,
                    "population": 2779,
                    "acces_num": 81,
                    "acces_info": 82,
                    "comp_admin": 89,
                    "comp_num": 116,
                    "code_iris": "625100104",
                    "latitude": 50.411257385,
                    "longitude": 2.780987683
                },
                {
                    "id": 32626,
                    "score": 84,
                    "score_acces": 73,
                    "score_comp": 96,
                    "score_global_dep": 86,
                    "score_global_region": 84,
                    "population": 1448,
                    "acces_num": 81,
                    "acces_info": 69,
                    "comp_admin": 79,
                    "comp_num": 104,
                    "code_iris": "625100302",
                    "latitude": 50.432632297,
                    "longitude": 2.777203055
                },
                {
                    "id": 46567,
                    "score": 67,
                    "score_acces": 55,
                    "score_comp": 79,
                    "score_global_dep": 70,
                    "score_global_region": 67,
                    "population": 153,
                    "acces_num": 81,
                    "acces_info": 42,
                    "comp_admin": 152,
                    "comp_num": 43,
                    "code_iris": "625100106",
                    "latitude": 50.423240577,
                    "longitude": 2.792804786
                }
            ]
        }
#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('../template/pdf_template.html', data)
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('../template/pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response

def index(request):
	context = {}
	return render(request, '../template/index.html', context)
