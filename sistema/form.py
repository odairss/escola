from django import forms
from django.forms import ModelForm, DateInput, DateTimeInput, PasswordInput, IntegerField
from .models import *

class AnoLetivoForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = AnoLetivo
        dateinput = DateInput()
        dateinput.input_type = 'date'
        fields =  ['ano', 'nome', 'datainicial', 'datafinal']
        widgets = {'datainicial': dateinput, 'datafinal':dateinput}

class TurmaForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Turma
        fields = ['nome', 'id_anoletivo', 'turno', 'anoturma', 'letraturma', 'graudeensino']


class AlunoForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Aluno
        dateinput = DateInput()
        dateinput.input_type = 'date'
        fields = ['id_turma', 'nome', 'cpf', 'datanascimento', 'situacao', 'sexo', 'naturalidade', 'datamatricula', 'procedencia',
                  'uf','nacionalidade', 'pai','mae','cartaoSUS','endereco','telefone', 'usuario', 'senha',
                  'perfil','observacao','transtornos', 'ano1', 'escolaano1',  'ano2', 'escolaano2',
                  'ano3', 'escolaano3',  'ano4', 'escolaano4',  'ano5', 'escolaano5']
        widgets = {'datanascimento': dateinput, 'senha':PasswordInput, 'datamatricula': dateinput}



class ProfessorForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Professor
        fields = ['nome', 'cpf', 'datanascimento', 'matricula', 'licenciatura', 'nivel', 'classe', 'vinculo',
                  'telefone', 'dataadmissao', 'id_turma', 'perfil']
        dateinput = DateInput()
        dateinput.input_type = 'date'
        widgets = {'datanascimento':dateinput, 'dataadmissao':dateinput}


class SecretariaForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Secretaria
        fields = ['nome', 'cpf', 'datanascimento', 'matricula', 'vinculo',
                  'telefone', 'dataadmissao', 'endereco', 'usuario','senha', 'perfil']
        dateinput = DateInput()
        dateinput.input_type = 'date'
        widgets = {'datanascimento':dateinput, 'dataadmissao':dateinput, 'senha':PasswordInput}


class BimestreForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Bimestre
        fields = ['nome', 'datainicio', 'datafim', 'id_anoletivo']
        dateinput = DateInput()
        dateinput.input_type = 'date'
        widgets = {'datainicio':dateinput, 'datafim':dateinput}


class DisciplinaForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Disciplina
        fields = ['nome']


class AulaForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Aula
        dataaula = DateInput()
        dataaula.input_type = 'date'
        fields = ['nome', 'id_professor', 'id_disciplina', 'id_turma', 'id_bimestre', 'dataaula', 'objetivo', 'competenciaBNCC', 'metodologia', 'recursos', 'avaliacao']
        widgets = {'dataaula': dataaula}


class AvaliacaoForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Avaliacao
        dateinput = DateInput()
        dateinput.input_type = 'date'
        fields = ['id_bimestre', 'id_disciplina', 'id_turma', 'dataavaliacao', 'nomeavaliacao', 'nota', 'id_aluno']
        widgets = {'dataavaliacao':dateinput}


class RecuperacaoForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Recuperacao
        dateinput = DateInput()
        dateinput.input_type = 'date'
        fields = ['id_bimestre', 'id_disciplina', 'id_turma', 'datarecuperacao', 'nomerecuperacao', 'nota', 'id_aluno']
        widgets = {'datarecuperacao':dateinput}


class FrequenciaForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Frequencia
        fields = ['id_aula', 'id_turma', 'frequencia']
