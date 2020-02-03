from django.db import models

# Create your models here.
###
#  '1' administrador
#  '2' gestor
#  '3' professor
#  '4' secretário
#  '5' aluno
# ###


class AnoLetivo(models.Model):
    id_anoletivo = models.AutoField(primary_key=True, verbose_name='Código')
    nome = models.CharField('Nome', max_length=20, null=False, blank=False)
    ano = models.IntegerField('Ano Letivo', null=False, blank=False)
    datainicial = models.DateField('Data inicial')
    datafinal = models.DateField('Data final')

    def __str_(self):
        return self.nome


class Turma(models.Model):
    id_turma = models.AutoField(primary_key=True, verbose_name='Turma')
    nome = models.CharField('Nome da turma', max_length=20, blank=False)
    id_anoletivo = models.ForeignKey(AnoLetivo, on_delete=models.CASCADE, null=False, verbose_name='Ano Letivo')
    TURNOS = ((u'matutino', u'Matutino'), (u'vespertino', u'Vespertino'), (u'noturno', u'Noturno'))
    turno = models.CharField('Turno', max_length=20, choices=TURNOS, null=False, blank=False)
    GRAU = ((u'EI', u'Educação Infantil'), (u'EF1', u'Ensino Fundamental I'), (u'EF2', u'Ensino Fundamental II'),
            (u'EM', u'Ensino Médio'))
    graudeensino = models.CharField('Grau de ensino', max_length=100, choices=GRAU, default='EF1')
    TURMAS = ((u'A', u'A'), (u'B', u'B'), (u'C', u'C'), (u'D', u'D'), (u'E', u'E'), (u'F', u'F'))
    letraturma = models.CharField('Turma', max_length=1, choices=TURMAS, null=False, blank=False, default='A')
    ANOS = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9))
    anoturma = models.IntegerField('Ano escolar', choices=ANOS, null=False, blank=False, default=1)

    def __str__(self):
        return self.nome


class Diario(models.Model):
    id_diario = models.AutoField(primary_key=True, verbose_name='Diário', null=False, blank=True)
    id_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=False, blank=False, default=1)
    resumo1 = models.TextField('Resumo do 1º Bimestre', null=True, blank=True)
    resumo2 = models.TextField('Resumo do 2º Bimestre', null=True, blank=True)
    resumo3 = models.TextField('Resumo do 3º Bimestre', null=True, blank=True)
    resumo4 = models.TextField('Resumo do 4º Bimestre', null=True, blank=True)
    anotacoes1 = models.TextField('Anotações do 1º Bimestre', null=True, blank=True)
    anotacoes2 = models.TextField('Anotações do 2º Bimestre', null=True, blank=True)
    anotacoes3 = models.TextField('Anotações do 3º Bimestre', null=True, blank=True)
    anotacoes4 = models.TextField('Anotações do 4º Bimestre', null=True, blank=True)
    diagnostico1 = models.TextField('Diagnóstico Semestral', null=True, blank=True)
    diagnostico2 = models.TextField('Diagnóstico Final', null=True, blank=True)

    def __str__(self):
        return 'Diário da turma ' + str(self.id_turma)


class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', max_length=100, blank=False)
    datanascimento = models.DateField(null=False, verbose_name='Data de Nascimento', blank=False,
                                      help_text='DD/MM/AAAA')
    SEXOS = ((u'masculino', u'masculino'), (u'feminino', u'feminino'))
    datamatricula = models.DateField('Data da matrícula', null=False, blank=False)
    PROCEDENCIAS = ((u'NA', u'NOVATO NO ANO'), (u'PE', u'PRÓPRIA ESCOLA'), (u'A', u'APROVADO'),
                    (u'RA', u'RETIDO NO CICLO'), (u'T', u'TRANSFERIDO'),
                    (u'NFE', u'NÃO FREQUENTOU A ESCOLA NO ANO ANTERIOR'), (u'EJA', u'EDUCAÇÃO DE JOVENS E ADULTOS'))
    procedencia = models.CharField('Procedência', max_length=50, choices=PROCEDENCIAS, null=False,
                                   blank=False, default='NA')
    SITUACOES = ((u'C', u'Cursando'), (u'R', u'Reprovado'), (u'A', u'Aprovado'),
                 (u'T', u'Transferido'), (u'AB', u'Abandonou'), (u'RC', u'Recuperação'))
    situacao = models.CharField('Situação', max_length=15, choices=SITUACOES, null=False, blank=False,
                                default='C')
    sexo = models.CharField('Sexo', max_length=20, choices=SEXOS, null=False, blank=False)
    cpf = models.CharField('CPF', max_length=15, default='999.999.999-99')
    naturalidade = models.CharField(max_length=100, verbose_name='Naturalidade', null=False, blank=False)
    UFs = ((u'AC', u'AC'), (u'AL', u'AL'), (u'AP', u'AP'), (u'AM', u'AM'), (u'BA', u'BA'),
           (u'CE', u'CE'), (u'AC', u'AC'), (u'DFD', u'DF'), (u'ES', u'ES'), (u'GO', u'GO'),
           (u'MA', u'MA'), (u'MT', u'MT'), (u'MS', u'MS'), (u'MG', u'MG'), (u'PA', u'PA'),
           (u'PB', u'PB'), (u'PR', u'PR'), (u'PE', u'PE'), (u'PI', u'PI'), (u'RJ', u'RJ'),
           (u'RN', u'RN'), (u'RS', u'RS'), (u'RO', u'RO'), (u'RR', u'RR'), (u'SC', u'SC'),
           (u'SP', u'SP'), (u'AC', u'AC'), (u'SE', u'SE'), (u'TO', u'TO'), )
    uf = models.CharField(max_length=50, verbose_name='UF', choices=UFs, blank=False)
    nacionalidade = models.CharField(max_length=50, verbose_name='Nacionalidade', blank=False)
    pai = models.CharField(max_length=100, verbose_name='Nome do pai', blank=False)
    mae = models.CharField(max_length=100, verbose_name='Nome da mãe', blank=False)
    cartaoSUS = models.CharField('Nº do Cartão SUS', max_length=50, blank=True, null=True)
    endereco = models.TextField(blank=True, verbose_name='Endereço', null=True)
    telefone = models.CharField(max_length=20, verbose_name='Celular', blank=True, null=True,
                                help_text='(00) 0 0000-0000')
    id_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=False, verbose_name='Turma')
    usuario = models.CharField('Nome de usuário', max_length=20, blank=False, null=False)
    senha = models.CharField('Senha', max_length=30, blank=False, null=False, default='12345')
    perfil = models.CharField('Perfil de usuário', max_length=20, blank=False, null=False, default='5')
    transtornos = models.TextField('Transtornos', blank=True, null=True)
    observacao = models.TextField('Observações', blank=True, null=True)
    ano1 = models.IntegerField('Ano em que cursou o 1º ano', null=True, blank=True)
    escolaano1 = models.CharField('Escola em que cursou o 1º ano', max_length=100, null=True, blank=True)
    ano2 = models.IntegerField('Ano em que cursou o 2º ano', null=True, blank=True)
    escolaano2 = models.CharField('Escola em que cursou o 2º ano', max_length=100, null=True, blank=True)
    ano3 = models.IntegerField('Ano em que cursou o 3º ano', null=True, blank=True)
    escolaano3 = models.CharField('Escola em que cursou o 3º ano', max_length=100, null=True, blank=True)
    ano4 = models.IntegerField('Ano em que cursou o 4º ano', null=True, blank=True)
    escolaano4 = models.CharField('Escola em que cursou o 4º ano', max_length=100, null=True, blank=True)
    ano5 = models.IntegerField('Ano em que cursou o 5º ano', null=True, blank=True)
    escolaano5 = models.CharField('Escola em que cursou o 5º ano', max_length=100, null=True, blank=True)
    faltas1 = models.IntegerField('Faltas do 1º Bimestre', blank=True, null=False, default=0)
    faltas2 = models.IntegerField('Faltas do 2º Bimestre', blank=True, null=False, default=0)
    faltas3 = models.IntegerField('Faltas do 3º Bimestre', blank=True, null=False, default=0)
    faltas4 = models.IntegerField('Faltas do 4º Bimestre', blank=True, null=False, default=0)
    faltastotal = models.IntegerField('Total de faltas  do ano', blank=True, null=False, default=0)
    presenca1 = models.IntegerField('Presença do 1º Bimestre', null=False, blank=True, default=0)
    presenca2 = models.IntegerField('Presença do 2º Bimestre', null=False, blank=True, default=0)
    presenca3 = models.IntegerField('Presença do 3º Bimestre', null=False, blank=True, default=0)
    presenca4 = models.IntegerField('Presença do 4º Bimestre', null=False, blank=True, default=0)
    presencatotal = models.IntegerField('Total de aulas participadas no ano letivo', null=False, blank=True, default=0)
    recuperacaoLP = models.DecimalField('Nota de Português da recuperação', max_digits=6, decimal_places=2, null=False,
                                        blank=True, default=0.0)
    recuperacaoMA = models.DecimalField('Nota de Matemática da recuperação', max_digits=6, decimal_places=2, null=False,
                                        blank=True, default=0.0)
    recuperacaoHI = models.DecimalField('Nota de História da recuperação', max_digits=6, decimal_places=2, null=False,
                                        blank=True, default=0.0)
    recuperacaoGEO = models.DecimalField('Nota de Geografia da recuperação', max_digits=6, decimal_places=2, null=False,
                                         blank=True, default=0.0)
    recuperacaoCI = models.DecimalField('Nota de Ciências da recuperação', max_digits=6, decimal_places=2, null=False,
                                        blank=True, default=0.0)
    recuperacaoEA = models.DecimalField('Nota Artes da recuperação', max_digits=6, decimal_places=2, null=False,
                                        blank=True, default=0.0)
    recuperacaoEF = models.DecimalField('Nota de Educação Física da recuperação', max_digits=6, decimal_places=2,
                                        null=False, blank=True, default=0.0)
    recuperacaoER = models.DecimalField('Nota da recuperação', max_digits=6, decimal_places=2, null=False, blank=True,
                                        default=0.0)
    mediaLP = models.DecimalField('Média de Português', max_digits=6, decimal_places=2, null=False, blank=True,
                                  default=0.0)
    mediaMA = models.DecimalField('Média de Matemática', max_digits=6, decimal_places=2, null=False, blank=True,
                                  default=0.0)
    mediaHI = models.DecimalField('Média de História', max_digits=6, decimal_places=2, null=False, blank=True,
                                  default=0.0)
    mediaGEO = models.DecimalField('Média de Geografia', max_digits=6, decimal_places=2, null=False, blank=True,
                                   default=0.0)
    mediaCI = models.DecimalField('Média de Ciências', max_digits=6, decimal_places=2, null=False, blank=True,
                                  default=0.0)
    mediaEF = models.DecimalField('Média de Educação Física', max_digits=6, decimal_places=2, null=False, blank=True,
                                  default=0.0)
    mediaEA = models.DecimalField('Média de Artes', max_digits=6, decimal_places=2, null=False, blank=True,
                                  default=0.0)
    mediaER = models.DecimalField('Média de Português', max_digits=6, decimal_places=2, null=False, blank=True,
                                  default=0.0)
    mediaanualLP = models.DecimalField('Média anual de Português', max_digits=6, decimal_places=2, null=False,
                                       blank=True, default=0.0)
    mediaanualMA = models.DecimalField('Média anual de Matemática', max_digits=6, decimal_places=2, null=False,
                                       blank=True, default=0.0)
    mediaanualHI = models.DecimalField('Média anual de História', max_digits=6, decimal_places=2, null=False,
                                       blank=True, default=0.0)
    mediaanualGEO = models.DecimalField('Média anual de Geografia', max_digits=6, decimal_places=2, null=False,
                                        blank=True, default=0.0)
    mediaanualCI = models.DecimalField('Média anual de Ciências', max_digits=6, decimal_places=2, null=False,
                                       blank=True, default=0.0)
    mediaanualEF = models.DecimalField('Média anual de Educação Física', max_digits=6, decimal_places=2, null=False,
                                       blank=True, default=0.0)
    mediaanualEA = models.DecimalField('Média anual de Artes', max_digits=6, decimal_places=2, null=False, blank=True,
                                       default=0.0)
    mediaanualER = models.DecimalField('Média anual de Português', max_digits=6, decimal_places=2, null=False,
                                       blank=True, default=0.0)
    resultadofinal = models.CharField('Resultado Final', max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.nome)


class Professor(models.Model):
    id_professor = models.AutoField(primary_key=True, null=False)
    nome = models.CharField('Nome', max_length=50, blank=False, null=False)
    licenciatura = models.CharField('Licenciatura', max_length=20, blank=False, null=False)
    NIVEIS = ((u'NE-1', u'NE-1'), (u'N-1', u'N-1'), (u'N-2', u'N-2'), (u'N-3', u'N-3'))
    nivel = models.CharField('Nível', max_length=5, choices=NIVEIS, blank=False, null=False)
    CLASSES = ((u'A', u'A'), (u'B', u'B'), (u'C', u'C'), (u'D', u'D'), (u'E', u'E'), (u'F', u'F'), (u'G', u'G'),
               (u'H', u'H'), (u'I', u'I'), (u'J', u'J'))
    classe = models.CharField('Classe', max_length=1, choices=CLASSES, blank=False, null=False)
    matricula = models.CharField('Matrícula', max_length=10, blank=False, null=False)
    datanascimento = models.DateField('Data de Nascimento', blank=False, null=False, help_text='DD/MM/AAAA')
    telefone = models.CharField('Telefone', max_length=20, help_text='(00) 0 0000-0000')
    cpf = models.CharField('CPF', max_length=20, blank=False, null=False, default='999.999.999-99')
    VINCULOS = ((u'efetivo', u'efetivo'), (u'seletivo', u'seletivo'), (u'estagiário', 'estagiário'))
    vinculo = models.CharField('Vínculo', max_length=10, choices=VINCULOS, blank=False, null=False)
    dataadmissao = models.DateField('Data de admissão', blank=False, null=False)
    id_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, verbose_name='Turma', blank=False, null=False)
    perfil = models.CharField('Perfil de usuário', max_length=20, blank=False, null=False, default='3')

    def __str__(self):
        return str(self.nome)


class Secretaria(models.Model):
    id_secretaria = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', max_length=50, blank=False, null=False)
    matricula = models.CharField('Matrícula', max_length=10, blank=False, null=False)
    datanascimento = models.DateField('Data de Nascimento', blank=False, null=False, help_text='DD/MM/AAAA')
    endereco = models.TextField('Endereço', blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=20, help_text='(00) 0 0000-0000')
    cpf = models.CharField('CPF', max_length=20, blank=False, null=False, default='999.999.999-99')
    VINCULOS = ((u'efetivo', u'efetivo'), (u'seletivo', u'seletivo'), (u'estagiário', 'estagiário'))
    vinculo = models.CharField('Vínculo', max_length=10, choices=VINCULOS, blank=False, null=False)
    dataadmissao = models.DateField('Data de admissão', blank=False, null=False)
    usuario = models.CharField('Nome de usuário', max_length=20, blank=False, null=False)
    senha = models.CharField('Senha', max_length=30, blank=False, null=False, default='12345')
    perfil = models.CharField('Perfil de usuário', max_length=20, blank=False, null=False, default='4')

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    id_disciplina = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nome


class Bimestre(models.Model):
    id_bimestre = models.AutoField(primary_key=True)
    BIMESTRES = ((u'1', u'1ª Bimestre'), (u'2', u'2ª Bimestre'), (u'3', u'3ª Bimestre'), (u'4', u'4ª Bimestre'), )
    nome = models.CharField('Nome do Bimestre', max_length=5, choices=BIMESTRES, null=False, blank=False)
    id_anoletivo = models.ForeignKey(AnoLetivo, on_delete=models.CASCADE, null=False, verbose_name='Ano Letivo')
    datainicio = models.DateField('Data Inicial')
    datafim = models.DateField('Data Final')

    def __str__(self):
        return self.nome


class Aula(models.Model):
    id_aula = models.AutoField(primary_key=True)
    nome = models.CharField('Título da Aula', max_length=100)
    dataaula = models.DateField('Data da aula', blank=False)
    objetivo = models.TextField('Objetivo', blank=False, null=False, max_length=500)
    competenciaBNCC = models.TextField('Competências da BNCC', max_length=500, blank=True, null=True)
    metodologia = models.TextField('Metodologia', blank=True, null=True, max_length=500)
    recursos = models.TextField('Recursos didáticos', blank=True, null=True, max_length=500)
    avaliacao = models.TextField('Avaliação', blank=True, null=True, max_length=500)
    chamada = models.BooleanField('Chamada', null=False, default=False)
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    id_professor = models.ForeignKey(Professor, on_delete=models.CASCADE, verbose_name='Professor')
    id_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, verbose_name='Turma')
    id_bimestre = models.ForeignKey(Bimestre, on_delete=models.CASCADE, verbose_name='Bimestre')

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    id_avaliacao = models.AutoField(primary_key=True)
    nomeavaliacao = models.CharField('Título da avaliacao', max_length=100, blank=False, null=False)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    dataavaliacao = models.DateField('Data da Avaliação', null=False, blank=False)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, verbose_name='Aluno')
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    id_bimestre = models.ForeignKey(Bimestre, on_delete=models.CASCADE, verbose_name='Bimestre')
    id_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, verbose_name='Turma')

    def __str__(self):
        return self.nomeavaliacao


class Recuperacao(models.Model):
    id_recuperacao = models.AutoField(primary_key=True)
    nomerecuperacao = models.CharField('Título da avaliacao', max_length=100, blank=False, null=False)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    datarecuperacao = models.DateField('Data da Avaliação', null=False, blank=False)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, verbose_name='Aluno')
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    id_bimestre = models.ForeignKey(Bimestre, on_delete=models.CASCADE, verbose_name='Bimestre')
    id_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, verbose_name='Turma')

    def __str__(self):
        return self.nomerecuperacao


class Frequencia(models.Model):
    id_frequencia = models.AutoField(primary_key=True)
    id_turma = models.ForeignKey(Turma, on_delete=models.CASCADE, verbose_name='Aluno')
    id_aula = models.ForeignKey(Aula, on_delete=models.CASCADE, verbose_name='Aula')
    frequencia = models.TextField('Frequência', blank=False, null=False)

    def __str__(self):
        return str(self.id_frequencia)
