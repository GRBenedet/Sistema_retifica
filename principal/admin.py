from django.contrib import admin
from principal.models import clientes, pecas, motor, servicos, orcamentos, orcamentos_end

admin.site.register(clientes)
admin.site.register(pecas)
admin.site.register(motor)
admin.site.register(servicos)
admin.site.register(orcamentos)
admin.site.register(orcamentos_end)

# Register your models here.
