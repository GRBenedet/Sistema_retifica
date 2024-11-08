from django.db import models

class clientes(models.Model):
    """Lista de clientes"""
    nome = models.CharField(max_length=30)
    cpfcnpj = models.BigIntegerField()
    end = models.CharField(max_length=100)
    tel = models.BigIntegerField()
    obs = models.CharField(max_length=200, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        """devolve uma representação do modelo"""
        return str(self.nome)
    
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
    cod = models.BigIntegerField()
    nome = models.CharField(max_length=30)
    med = models.CharField(max_length=10, blank=True, null=True)
    aplic = models.ManyToManyField(motor)
    custo = models.FloatField(blank=True, null=True)
    valor = models.FloatField()
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """devolve um representação do modelo"""
        return self.nome
    
class servicos(models.Model):
    """lista de serviços"""
    cod = models.BigIntegerField()
    nome = models.CharField(max_length=20)
    valor = models.FloatField()
    obs = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        """retorna modelo de serviços"""
        return self.nome

class orcamentos(models.Model):
    """lista de orçamentos ativos"""
    cliente = models.ForeignKey(clientes, on_delete=models.CASCADE)
    buy_pecas = models.ManyToManyField(pecas, blank=True, null=True)
    ativos_servicos = models.ManyToManyField(servicos, blank=True, null=True)
    preco_final = models.FloatField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """retorna modelo para orçamentos"""
        return self.id

class orcamentos_end(models.Model):
    """lista de orçamentos finalizados"""
    orcamentos_end = models.ForeignKey(orcamentos, on_delete=models.PROTECT)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """retorna modelo para orcamento finalizado"""

        return self.orcamentos_end
    
class notas(models.Model):
    """tabela de notas dadas entrada"""
    cod = models.BigIntegerField()
    dist = models.CharField(max_length=30)
    prod = models.ManyToManyField(pecas)
    quant = models.IntegerField()
    custo = models.FloatField()
    custototal = models.FloatField(blank=True, null=True)


# Create your models here.
