from django.db import models

class clientes(models.Model):
    """Lista de clientes"""
    nome = models.CharField(max_length=30)
    cpfcnpj = models.IntegerField()
    end = models.CharField(max_length=100)
    tel = models.IntegerField()
    obs = models.CharField(max_length=200, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        """devolve uma representação do modelo"""
        return self.nome
    
class motor(models.Model):
    nomemotor = models.CharField(max_length=50)
    cilindrada = models.IntegerField()
    combustivel = models.CharField(max_length=12)
    tecnologia = models.CharField(max_length=20 , blank=True, null=True)
    cilindros = models.IntegerField()

    def __str__(self):
        """devolve uma representação do modelo"""
        return self.nomemotor
    
class pecas(models.Model):
    """lista de peças"""
    cod = models.IntegerField()
    nome = models.CharField(max_length=30)
    med = models.CharField(max_length=10, blank=True, null=True)
    aplic = models.ForeignKey(motor, on_delete=models.PROTECT)
    
    def __str__(self):
        """devolve um representação do modelo"""
        return self.nome



# Create your models here.
