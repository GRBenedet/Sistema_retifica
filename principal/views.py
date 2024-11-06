from django.shortcuts import render
from .models import clientes, pecas, servicos, orcamentos, orcamentos_end

def index(request):
    """pagina principal do sistema"""
    return render(request, 'principal/index.html')

def cliente(request):
    """acessa a tabela dos clientes"""
    cliente = clientes.objects.order_by('id')
    context = { 'cliente': cliente}
    return render(request, 'principal/cliente.html' , context)

def peças(request):
    """acessa a tabela de pecas"""
    peca = pecas.objects.order_by('id')

    context = {'peca': peca}
    return render(request, 'principal/pecas.html', context)

def servico(request):
    """acessas a tabela de serviços"""
    serv = servicos.objects.order_by('id')

    context = {'servico': serv}
    return render(request, 'principal/servicos.html', context)

def orcamento(request):
    """acessa a tabela de orcamentos ativos"""
    orc = orcamentos.objects.order_by('id')

    context = {'orcamento': orc}
    return render(request, 'principal/orcamento.html', context)

def orcamento_end(request):
    orc_end = orcamentos_end.objects.order_by('id')

    context = {'orcamento_end': orc_end}
    return render(request, 'principal/orcamento_end.html', context)

# Create your views here.
