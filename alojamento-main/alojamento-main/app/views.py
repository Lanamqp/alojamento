from django.shortcuts import render
from django.views import View
from .models import Cidade, Curso, Turma, Alojamento, Quarto, Pessoa

# View para a página inicial
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        pass

# View para exibir a lista de Pessoas
class PessoaView(View):
    template_name = 'pessoa.html'

    def get(self, request):
        pessoas = Pessoa.objects.all()  
        return render(request, self.template_name, {'pessoas': pessoas})
    
    def post(self, request):
        pass

# View para exibir a lista de Cidades
class CidadeView(View):
    template_name = 'cidade.html'

    def get(self, request):
        cidades = Cidade.objects.all()  
        return render(request, self.template_name, {'cidades': cidades})
    
    def post(self, request):
        pass

# View para exibir a lista de Cursos
class CursoView(View):
    template_name = 'curso.html'

    def get(self, request):
        cursos = Curso.objects.all()  
        return render(request, self.template_name, {'cursos': cursos})
    
    def post(self, request):
        pass

# View para exibir a lista de Turmas
class TurmaView(View):
    template_name = 'turma.html'

    def get(self, request):
        turmas = Turma.objects.all()  
        return render(request, self.template_name, {'turmas': turmas})
    
    def post(self, request):
        pass

# View para exibir a lista de Alojamentos
class AlojamentoView(View):
    template_name = 'alojamentos.html'

    def get(self, request):
        alojamentos = Alojamento.objects.all()  
        return render(request, self.template_name, {'alojamentos': alojamentos})
    
    def post(self, request):
        pass

# View para exibir a lista de Quartos
class QuartoView(View):
    template_name = 'quarto.html'

    def get(self, request):
        quartos = Quarto.objects.all()  
        return render(request, self.template_name, {'quartos': quartos})
    
    def post(self, request):
        pass




