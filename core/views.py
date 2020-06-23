from django.shortcuts import render, redirect
from core.models import Evento


# Create your views here.

# def index(request):
#     return redirect('/agenda')


# def consulta_eventos(request, evento):
#     if evento:
#         Evento.objects.get(titulo=evento)
#         return Evento.titulo
#     else:
#         return HttpResponse('A pesquisa não retornou nenhum registro.')

def lista_eventos(request):
    # usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario)
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
