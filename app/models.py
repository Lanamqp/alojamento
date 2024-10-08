from django.db import models
class Cidade(models.Model):
        nome = models.CharField(max_length=100)
        uf = models.CharField(max_length=2)
        
        class Meta:
            verbose_name = "Cidade"
            verbose_name_plural = "Cidades"

        def __str__(self):
            return f'{self.nome}-{self.uf}'
class Curso(models.Model):
        nome = models.CharField(max_length=100)
        
        class Meta:
            verbose_name = "Curso"
            verbose_name_plural = "Cursos"

        def __str__(self):
            return f'{self.nome}'

class Turma(models.Model):
        nome = models.CharField(max_length=100)
        
        class Meta:
            verbose_name = "Turma"
            verbose_name_plural = "Turmas"

        def __str__(self):
            return f'{self.nome}'



class Alojamento(models.Model):
        nome = models.CharField(max_length=100)
        
        class Meta:
            verbose_name = "Alojamento"
            verbose_name_plural = "Alojamentos"

        def __str__(self):
            return f'{self.nome}'


class Quarto(models.Model):
        alojamento = models.ForeignKey(Alojamento, on_delete=models.CASCADE)
        numero_quarto = models.CharField(max_length=3)
        max_pessoas_quarto = models.CharField(max_length=3)


        
        class Meta:
            verbose_name = "Quarto"
            verbose_name_plural = "Quartos"

        def __str__(self):
            return f'Quarto {self.numero_quarto} - Max: {self.max_pessoas_quarto} pessoas'
        


class Pessoa(models.Model):
        nome = models.CharField(max_length=100)
        cpf = models.CharField(max_length=11)
        cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
        curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
        turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
        quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE, related_name='pessoas')
        class Meta:
            verbose_name_plural = "Pessoas"

        def __str__(self):
            return f'{self.nome} - {self.curso}'