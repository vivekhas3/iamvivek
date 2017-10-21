from django.views.generic import TemplateView
from django.shortcuts import HttpResponse
from settings import BASE_DIR
class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = {}
        return context
def download(request):
    with open(BASE_DIR + '/../static/VivekSoundrapandi.pdf', 'r') as pdf:
	response = HttpResponse(pdf.read(),content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=VivekSoundrapandi.pdf'
	return response
