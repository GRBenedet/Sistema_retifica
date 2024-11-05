from django.shortcuts import render
from .models import clientes

def index(request):
    """pagina principal do sistema"""
    return render(request, 'principal/index.html')

def cliente(request):
    """acessa a tabela dos clientes"""
    cliente = clientes.objects.order_by('id')
    
    context = { 'cliente': cliente}
    return render(request, 'principal/cliente.html' , context)

# Create your views here.
