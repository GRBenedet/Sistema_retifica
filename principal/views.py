from django.shortcuts import render, get_object_or_404, redirect
from .models import clientes, motor, pecas, servicos, orcamentos, orcamentos_end
from .forms import ClientesForm, PecasForm, ServicosForm, MotorForm, OrcForm
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
import logging

logger = logging.getLogger(__name__)

def index(request):
    """pagina principal do sistema"""
    return render(request, 'principal/index.html')

def cliente(request,):
    """acessa a tabela dos clientes"""
    cliente = clientes.objects.order_by('id')

    context = { 'cliente': cliente}
    return render(request, 'principal/cliente.html' , context)

def motores(request):
    """acessa a tabela de motores"""
    motores = motor.objects.order_by('id')

    context = {'motores': motores}
    return render(request, 'principal/motor.html', context)

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

def novo_cliente(request):
    """adiciona um novo cliente"""
    if request.method != 'POST':
        form = ClientesForm()
    else:
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cliente'))
        
    context = {'form': form}

    return render(request, 'principal/novo_cliente.html', context)

def nova_peca(request):
    """adiciona uma nova peça"""
    if request.method != 'POST':
        form = PecasForm()
    else:
        form = PecasForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pecas'))
    context = {'form': form}

    return render(request, 'principal/nova_peca.html', context)

def novo_servico(request):
    """Adicionar um novo Serviço"""
    if request.method != 'POST':
        form = ServicosForm()
    else:
        form = ServicosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('servicos'))
    context = {'form': form}

    return render(request, 'principal/novo_servico.html', context)

def novo_motor(request):
    """Adicionar um novo Motor"""
    if request.method != 'POST':
        form = MotorForm()
    else:
        form = MotorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('motores'))
    context = {'form': form}

    return render(request, 'principal/novo_motor.html', context)

def novo_orc(request):
    """adciona um novo orcamento"""
    if request.method != 'POST':
        form = OrcForm()
    else:
        form = OrcForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('orcamentos'))
    context = {'form': form}

    return render(request, 'principal/novo_orc.html', context)

def edit_cliente(request, clientes_id):
    """edita um cliente cadastrado"""
    client = get_object_or_404(clientes, id=clientes_id)

    if request.method != 'POST':
        form = ClientesForm(instance=client)
    else:
        form = ClientesForm(instance=client, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cliente'))
    context = {'client': client, 'form': form}

    return render(request, 'principal/edit_cliente.html', context)

def edit_peca(request, pecas_id):
    """edita uma peça cadastrada"""
    pec = get_object_or_404(pecas, id=pecas_id)

    if request.method != 'POST':
        form = PecasForm(instance=pec)
    else:
        form = PecasForm(instance=pec, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pecas'))
    context = {'pec': pec, 'form': form}

    return render(request, 'principal/edit_peca.html', context)

def edit_orcamento(request, orcamentos_id):
    """editar um orcamento"""
    orc = get_object_or_404(orcamentos, id=orcamentos_id)

    if request.method != 'POST':
        form = OrcForm(instance=orc)
    else:
        form = OrcForm(instance=orc, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('orcamento'))
    context = {'orc': orc, 'form': form}

    return render(request, 'principal/edit_orcamento.html', context)

def edit_servico(request, servicos_id):
    """edita um servico"""
    serv = get_object_or_404(servicos, id=servicos_id)

    if request.method != 'POST':
        form = ServicosForm(instance=serv)
    else:
        form = ServicosForm(instance=serv, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('servicos'))
    context = {'serv': serv, 'form': form}

    return render(request, 'principal/edit_servico.html', context)

def edit_motor(request, motores_id):

    mot = get_object_or_404(motor, id=motores_id)

    if request.method != 'POST':
        form = MotorForm(instance=mot)
    else:
        form = MotorForm(instance=mot, data=request.POST)
        if  form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('motores'))
    context = {'mot': mot, 'form': form}

    return render(request, 'principal/edit_motor.html', context)

def del_cliente(request, clientes_id):
    clint = get_object_or_404(clientes, id=clientes_id)

    if request.method == 'POST':
        
            clint.delete()
            return redirect('cliente')
        
    context = {'clint': clint}

    return render(request, 'principal/del_cliente.html', context)


def del_peca(request, pecas_id):
    peca = get_object_or_404(pecas, id=pecas_id)

    if request.method == 'POST':
        peca.delete()
        return redirect('pecas')
    
    context = {'peca': peca}

    return render(request, 'principal/del_peca.html', context)

def del_orcamento(request, orcamentos_id):
    orc =get_object_or_404(orcamentos, id=orcamentos_id)

    if request.method == 'POST':
        orc.delete()
        return redirect('orcamentos')
    
    context = {'orc': orc}

    return render(request, 'principal/del_orcamento.html', context)

def del_servico(request, servicos_id):
    serv = get_object_or_404(servicos, id= servicos_id)

    if request.method == 'POST':
        serv.delete()
        return redirect('servicos')
    
    context = {'serv': serv}

    return render(request, 'principal/del_servico.html', context)

def del_motor(request, motor_id):
    mot = get_object_or_404(motor, id=motor_id)

    if request.method == 'POST':
        mot.delete()
        return redirect('motores')
    
    context = {'mot': mot}

    return render(request, 'principal/del_motor.html', context)

# Create your views here.
