"""
URL configuration for SIS_Retifica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('clientes', views.cliente, name='cliente'),
    path('motores', views.motores, name='motores'),
    path('peças', views.peças, name='pecas'),
    path('serviços', views.servico, name='servicos'),
    path('orcamentos', views.orcamento, name='orcamentos'),
    path('orcamentobaixa', views.orcamento_end, name='orcamento_end'),
    path('novo_cliente', views.novo_cliente, name='novo_cliente'),
    path('nova_peca', views.nova_peca, name='nova_peca'),
    path('novo_servico', views.novo_servico, name='novo_servico'),
    path('novo_motor', views.novo_motor, name='novo_motor'),
    path('novo_orc', views.novo_orc, name='novo_orc'),
    path('edit_cliente/<int:clientes_id>', views.edit_cliente, name='edit_cliente'),
    path('edit_peça/<int:pecas_id>', views.edit_peca, name='edit_peca'),
    path('edit_orcamento/<int:orcamentos_id>', views.edit_orcamento, name='edit_orcamento'),
    path('edit_servico/<int:servicos_id>', views.edit_servico, name='edit_servico'),
    path('edit_motor/<int:motores_id>', views.edit_motor, name='edit_motor'),
    path('del_cliente/<int:clientes_id>', views.del_cliente, name='del_cliente'),
    path('del_peca/<int:pecas_id>', views.del_peca, name='del_peca'),
    path('del_orcamento/<int:orcamentos_id>', views.del_orcamento, name='del_orcamento'),
    path('del_servico/<int:servicos_id>', views.del_servico, name='del_servico'),
    path('del_motor/<int:motor_id>', views.del_motor, name='del_motor'),

    
]
