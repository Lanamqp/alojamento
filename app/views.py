from django.shortcuts import render

from django.views import View

from .models import*

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html',)
    def post(self, request):
        pass

class PessoaView(View):
    template_name = 'pessoa.html'
    def get(self, request):
        pessoas = Pessoa.objects.all()  
        return render(request, 'pessoa.html', {'pessoas': pessoas})
    
    def post(self, request):
        pass

class AtividadeView(View):
    template_name = 'atividade.html'
    def get(self, request):
        atividades = Atividade.objects.all()  
        return render(request, 'atividade.html', {'atividades': atividades})
    
    def post(self, request):
        pass

class InscricaoView(View):
    template_name = 'inscricao.html'
    def get(self, request):
        inscricoes = Inscricao.objects.all()  
        return render(request, 'inscricao.html', {'inscricoes': inscricoes})
    
    def post(self, request):
        pass
from django.shortcuts import render
from django.views import View
from .models import Local

class LocalView(View):
    template_name = 'local.html'
    def get(self, request):
        locais = Local.objects.all() 
        return render(request, 'local.html', {'locais': locais})
    
    def post(self, request):
        pass

class OcupacaoView(View):
    template_name = 'ocupacao.html'
    def get(self, request):
        ocupacoes = Ocupacao.objects.all()  
        return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})
    
    def post(self, request):
        pass

class EventoView(View):
    template_name = 'evento.html'
    def get(self, request):
        eventos = Evento.objects.all()  
        return render(request, 'evento.html', {'eventos': eventos})
    
    def post(self, request):
        pass

class CategoriaView(View):
    template_name = 'categoria.html'
    def get(self, request):
        categorias = Categoria.objects.all()  
        return render(request, 'categoria.html', {'categorias': categorias})
    
    def post(self, request):
        pass
    