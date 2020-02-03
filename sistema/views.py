from django.shortcuts import render, redirect
from io import BytesIO
from django.http import FileResponse, HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_CENTER
from datetime import date, timedelta
from django.db.models import Q

from .models import *
from .form import *

# Create your views here.


def login_prof(request):
    return render(request, 'login_professores.html')


def submit_prof(request):
    if request.method == 'POST':
        senha = request.POST.get('password')
        perfil = request.POST.get('perfil')

        if Professor.objects.filter(cpf=senha, perfil=perfil).exists():
            professor = Professor.objects.get(cpf=senha, perfil=perfil)
            turma = Turma.objects.get(id_turma=professor.id_turma.id_turma)
            alunos = Aluno.objects.filter(id_turma=turma.id_turma)
            return render(request, 'professor_page.html', {'turma': turma, 'professor': professor, 'alunos': alunos})
        messages.error(request, 'Usuário ou senha inválida!')
        return redirect('login_prof')
    return redirect('home')


def generatePDF(request, idAluno):
    aluno = aluno_to_pdf(idAluno)
    pdf = render_to_pdf('historico.html', aluno)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'Aluno_%spdf' %('12341231')
        content = 'inline; filename="%s"' %(filename)
        download = request.GET.get('download')
        if download:
            content = 'attachment; filename="%s"' % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse('Not found')


# class GeneratePDF(View):
#     def get(self, request, *args, **kwargs):
#         aluno = aluno_to_pdf(1)
#         pdf = render_to_pdf('historico.html', aluno)
#         if pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             filename = 'Aluno_%spdf' %("12341231")
#             content = 'inline; filename="%s"' %(filename)
#             download = request.GET.get('download')
#             if download:
#                 content = 'attachment; filename="%s"' %(filename)
#             response['Content-Disposition'] = content
#             return response
#         return HttpResponse('Not found')


def diarioToPDF(request, idTurma):
    turma = turma_to_pdf(idTurma)
    pdf = render_to_pdf('diario.html', turma)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = 'Turma_%spdf' %('12341231')
        content = 'inline; filename="%s"' % (filename)
        download = request.GET.get('download')
        if download:
            content = 'attachment; filename="%s"' %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse('Not found')


# class DiarioToPDF(View):
#     def get(self, request, *args, **kwargs):
#         turma = turma_to_pdf(1)
#         pdf = render_to_pdf('diario.html', turma)
#         if pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             filename = 'Aluno_%spdf' %('12341231')
#             content = 'inline; filename="%s"' %(filename)
#             download = request.GET.get('download')
#             if download:
#                 content = 'attachment; filename="%s"' %(filename)
#             response['Content-Disposition'] = content
#             return response
#         return HttpResponse('Not found')



#def generate_view(request, *args, **kwargs):
#    template = get_template('aluno.html')
#     context = {
#         'invoice_id': 123,
#         'customer_name': 'John Cooper',
#         'amount': 1399.99,
#         'today': 'Today',
#     }
#     html = template.render(context)
#     return HttpResponse(html)


# def print_users(idaluno):
#     buffer = BytesIO()
#     doc = SimpleDocTemplate(buffer, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
#
#     # Our container for 'Flowable' objects
#     elements = []
#
#     # A large collection of style sheets pre-made for us
#     styles = getSampleStyleSheet()
#     styles.add(ParagraphStyle(name='centered', fontSize=12, spaceAfter=18, alignment=TA_CENTER))
#
#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     elements.append(Paragraph('<img src="/home/odair/escola/sistema/static/img/brasao-de-parnamirim.jpg" valign="top" />', styles['centered']))
#
#     elements.append(Paragraph('<strong>ESTADO DO RIO GRANDE DO NORTE<br/>PREFEITURA MUNICIPAL DE PARNAMIRIM<br/>SECRETARIA MUNICIPAL DE EDUCAÇÃO E CULTURA<br/>ESCOLA MUNICIPAL PROFESSORA EULINA AUGUSTA DE ALMEIDA</strong>', styles['centered']))
#
#     aluno = Aluno.objects.get(id_aluno=idaluno)
#     data = [
#         ['DADOS DO ALUNO'],
#         ['NOME:', aluno.nome],
#         ['DATA DE NASCIMENTO:\n'+str(aluno.datanascimento), 'NATURALIDADE:\n'+aluno.naturalidade, 'UF:\n'+aluno.uf, 'NACIONALIDADE:\n'+aluno.nacionalidade],
#         ['NOME DO PAI: ', aluno.mae],
#         ['NOME DA MÃE: ', aluno.pai]
#     ]
#     table = Table(data)
#
#     ts = TableStyle(
#         [
#         ('GRID',(0,0),(-1,-1),.5, colors.black),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ]
#     )
#     table.setStyle(ts)
#
#     elements.append(table)
#
#     doc.build(elements)
#
#     # Get the value of the BytesIO buffer and write it to the response.
#     pdf = buffer.getvalue()
#     buffer.close()
#     return pdf
#
#
# def imprimirTable(request, idAluno):
#     # Create the HttpResponse object with the appropriate PDF headers.
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="My Users.pdf"'
#
#     buffer = BytesIO()
#
#     pdf = print_users(idAluno)
#
#     response.write(pdf)
#     return response


def anosletivos(request):
    return render(request, 'anosletivos.html')


def registrarAnoletivo(request):
    formanoletivo = AnoLetivoForm(request.POST or None)
    if formanoletivo.is_valid():
        formanoletivo.save()
        return redirect('listAnosLetivos')
    return render(request, 'registrarAnoLetivo.html', {'form':formanoletivo})


def buscarAnoLetivo(request, idanoletivo):
    anoletivo = AnoLetivo.objects.get(id_anoletivo=idanoletivo)
    return render(request, 'verAnoLetivo.html', {'anoletivo': anoletivo})


def listAnosLetivos(request):
    anosletivos = AnoLetivo.objects.all()
    return render(request, 'listAnosLetivos.html', {'anosletivos': anosletivos})


def editarAnoLetivo(request, idAnoLetivo):
    anoletivo = AnoLetivo.objects.get(id_anoletivo=idAnoLetivo)
    formanoletivo = AnoLetivoForm(request.POST or None, instance=anoletivo)
    if formanoletivo.is_valid():
        formanoletivo.save()
        return redirect('listAnosLetivos')
    return render(request, 'registrarAnoLetivo.html',{'form': formanoletivo, 'anoletivo': anoletivo})


def deletarAnoLetivo(request, idAnoLetivo):
    anoletivo = AnoLetivo.objects.get(id_anoletivo=idAnoLetivo)
    if request.method == 'POST':
        anoletivo.delete()
        return redirect('listAnosLetivos')
    return render(request,'anoletivo-del-confirm.html', {'anoletivo': anoletivo})


def home(request):
    return render(request, 'home.html')


def turmas(request):
    return render(request,'turmas.html')


def registrarTurma(request):
        formturma = TurmaForm(request.POST or None)
        if formturma.is_valid():
            formturma.save()
            return redirect('listarTurmas')
        return render(request,'registrarTurma.html',{'form':formturma})


def buscarTurma(request, idTurma):
    turma = Turma.objects.get(id_turma=idTurma)
    alunos = Aluno.objects.filter(id_turma=idTurma)
    professor = Professor.objects.filter(id_turma=idTurma)
    disciplinas = Disciplina.objects.all()

    return render(request, 'verTurma.html', {'turma':turma, 'professor':professor,
                                             'disciplinas':disciplinas, 'alunos':alunos})


def listarTurmas(request):
    turmas = Turma.objects.all()
    return render(request, 'listarTurmas.html', {'turmas': turmas})


def editarTurma(request, idTurma):
    turma = Turma.objects.get(id_turma=idTurma)
    formturma = TurmaForm(request.POST or None, instance=turma)
    if formturma.is_valid():
        formturma.save()
        return redirect('listarTurmas')
    return render(request, 'registrarTurma.html', {'form':formturma, 'turma': turma})


def deletarTurma(request, idTurma):
    turma = Turma.objects.get(id_turma=idTurma)
    if request.method == 'POST':
        turma.delete()
        return redirect('listarTurmas')
    return render(request, 'turma-del-confirm.html', {'turma': turma})


def alunos(request):
    return render(request,'alunos.html')


def registrarAluno(request):
    formaluno = AlunoForm(request.POST or None)
    if formaluno.is_valid():
        formaluno.save()
        return redirect('listarAlunos')
    return render(request, 'registrarAluno.html', {'form': formaluno})


def buscarAluno(request, idAluno):
    aluno = Aluno.objects.get(id_aluno=idAluno)
    avaliacoes = Avaliacao.objects.filter(id_aluno=idAluno, id_turma=aluno.id_turma.id_turma).order_by('id_disciplina')
    disciplinas = Disciplina.objects.all()
    rendimento_escolar = []

    for disciplina in disciplinas:
        soma = 0.0
        for avaliacao in avaliacoes:
            if avaliacao.id_disciplina.id_disciplina == disciplina.id_disciplina:
                soma += float(avaliacao.nota)
        media_disciplina = [disciplina, soma/4]
        rendimento_escolar.append(media_disciplina)

    return render(request, 'verAluno.html', {'aluno':aluno,'avaliacoes':avaliacoes, 'rendimento_escolar': rendimento_escolar})


def turma_to_pdf(idTurma):
    turma = Turma.objects.get(id_turma=idTurma)
    professor = Professor.objects.get(id_turma=idTurma)
    alunos = Aluno.objects.filter(id_turma=idTurma)
    frequencias = Frequencia.objects.filter(id_turma=idTurma)

    meses = []

    for num_mes in range(1,13,1):
        meses.append([num_mes, []])

    for mes in range(0,12,1):
        for id_aluno in range(1,51,1):
            meses[mes][1].append([id_aluno, []])

    for mes in range(0,12,1):
        for id_aluno in range(0,50,1):
            for dia in range(1,32,1):
                meses[mes][1][id_aluno][1].append(' ')

    for frequencia in frequencias:
        string_frequencias = frequencia.frequencia.split(',')
        for string_f in string_frequencias:
            list_freq = string_f.split(':')
            idaluno = list_freq[0]
            freq = list_freq[1]
            data = frequencia.id_aula.dataaula
            meses[data.month-1][1][int(idaluno)-1][1][data.day-1] = freq

    mes = []
    for dia in range(1,32,1):
        mes.append(dia)

    contador = len(alunos)
    linhas = []
    for item in range(contador+1,51,1):
        linhas.append(item)

    return {'turma': turma, 'professor':professor, 'alunos':alunos, 'linhas': linhas, 'mes':mes, 'frequencias': meses}


def aluno_to_pdf(idAluno):
    aluno = Aluno.objects.get(id_aluno=idAluno)
    avaliacoes = Avaliacao.objects.filter(id_aluno=idAluno, id_turma=aluno.id_turma.id_turma)
    disciplinas = Disciplina.objects.all()
    rendimento_escolar = []

    for disciplina in disciplinas:
        soma = 0.0
        for avaliacao in avaliacoes:
            if avaliacao.id_disciplina.id_disciplina == disciplina.id_disciplina:
                soma += float(avaliacao.nota)
        media_disciplina = [disciplina, soma/4]
        rendimento_escolar.append(media_disciplina)

    return {'aluno':aluno, 'avaliacoes':avaliacoes, 'rendimento_escolar':rendimento_escolar}


def listarAlunos(request):
    alunos = Aluno.objects.all()
    return render(request,'listarAlunos.html',{'alunos':alunos})


def editarAluno(request, idAluno):
    aluno = Aluno.objects.get(id_aluno=idAluno)
    formaluno = AlunoForm(request.POST or None, instance=aluno)
    if formaluno.is_valid():
        formaluno.save()
        return redirect('listarAlunos')
    return render(request, 'registrarAluno.html',{'form':formaluno, 'aluno':aluno})


def deletarAluno(request, idAluno):
    aluno = Aluno.objects.get(id_aluno=idAluno)
    if request.method == 'POST':
        aluno.delete()
        return redirect('listarAlunos')
    return render(request,'aluno-del-confirm.html',{'aluno':aluno})


def profs(request):
    return render(request,'profs.html')


def registrarProf(request):
    formprof = ProfessorForm(request.POST or None)
    if formprof.is_valid():
        formprof.save()
        return redirect('listarProfs')
    return render(request, 'registrarProf.html', {'form': formprof})


def buscarProf(request, idProf):
    professor = Professor.objects.get(id_professor=idProf)
    return render(request, 'verProf.html', {'professor':professor})


def listarProfs(request):
    professores = Professor.objects.all()
    return render(request,'listarProfs.html',{'professores':professores})


def editarProf(request, idProf):
    professor = Professor.objects.get(id_professor=idProf)
    formprofessor = ProfessorForm(request.POST or None, instance=professor)
    if formprofessor.is_valid():
        formprofessor.save()
        return redirect('listarProfs')
    return render(request, 'registrarProf.html',{'form':formprofessor, 'professor':professor})


def deletarProf(request, idProf):
    professor = Professor.objects.get(id_professor=idProf)
    if request.method == 'POST':
        professor.delete()
        return redirect('listarProfs')
    return render(request,'professor-del-confirm.html',{'professor':professor})


def disciplinas(request):
    return render(request,'disciplinas.html')


def registrarDisc(request):
    formdisc = DisciplinaForm(request.POST or None)
    if formdisc.is_valid():
        formdisc.save()
        return redirect('listarDiscs')
    return render(request, 'registrarDisc.html', {'form': formdisc})


def buscarDisc(request, idDisc):
    disciplina = Disciplina.objects.get(id_disciplina=idDisc)
    return render(request, 'verDisc.html', {'disciplina':disciplina})


def listarDiscs(request):
    disciplinas = Disciplina.objects.all()
    return render(request,'listarDiscs.html',{'disciplinas':disciplinas})


def editarDisc(request, idDisc):
    disciplina = Disciplina.objects.get(id_disciplina=idDisc)
    formdisc = DisciplinaForm(request.POST or None, instance=disciplina)
    if formdisc.is_valid():
        formdisc.save()
        return redirect('listarDiscs')
    return render(request, 'registrarDisc.html',{'form':formdisc, 'disciplina':disciplina})


def deletarDisc(request, idDisc):
    disciplina = Disciplina.objects.get(id_disciplina=idDisc)
    if request.method == 'POST':
        disciplina.delete()
        return redirect('listarDiscs')
    return render(request,'disciplina-del-confirm.html',{'disciplina':disciplina})


def bimestres(request):
    return render(request,'bimestres.html')


def regBimestre(request):
    formbim = BimestreForm(request.POST or None)
    if formbim.is_valid():
        formbim.save()
        return redirect('listBimestres')
    return render(request, 'regBimestre.html', {'form': formbim})


def buscarBimestre(request, idBim):
    bimestre = Bimestre.objects.get(id_bimestre=idBim)
    return render(request, 'verBimestre.html', {'bimestre':bimestre})


def listBimestres(request):
    bimestres = Bimestre.objects.all()
    return render(request,'listBimestres.html',{'bimestres':bimestres})


def editBimestre(request, idBim):
    bimestre = Bimestre.objects.get(id_bimestre=idBim)
    formbim = BimestreForm(request.POST or None, instance=bimestre)
    if formbim.is_valid():
        formbim.save()
        return redirect('listBimestres')
    return render(request, 'regBimestre.html',{'form':formbim, 'bimestre':bimestre})


def delBimestre(request, idBim):
    bimestre = Bimestre.objects.get(id_bimestre=idBim)
    if request.method == 'POST':
        bimestre.delete()
        return redirect('listBimestres')
    return render(request,'bimestre-del-confirm.html',{'bimestre':bimestre})


def aulas(request):
    return render(request,'aulas.html')


def regAula(request, idProfessor):
    if request.POST:
        aula = Aula()
        aula.nome = request.POST.get('nome')
        id_disciplina = request.POST.get('id_disciplina')
        aula.id_disciplina = Disciplina.objects.get(id_disciplina=id_disciplina)
        professor = Professor.objects.get(id_professor=idProfessor)
        aula.id_professor = professor
        turma = professor.id_turma
        aula.id_turma = turma
        id_bimestre = request.POST.get('id_bimestre')
        aula.id_bimestre = Bimestre.objects.get(id_bimestre=id_bimestre)
        aula.chamada = False
        aula.avaliacao = request.POST.get('avaliacao')
        aula.dataaula = request.POST.get('dataaula')
        aula.competenciaBNCC = request.POST.get('competenciaBNCC')
        aula.metodologia = request.POST.get('metodologia')
        aula.objetivo = request.POST.get('objetivo')
        aula.recursos = request.POST.get('recursos')
        aula.save()
        return redirect('listAulas', idProfessor)
    professor = Professor.objects.get(id_professor=idProfessor)
    disciplinas = Disciplina.objects.all()
    turma = Turma.objects.get(id_turma=professor.id_turma.id_turma)
    bimestres = Bimestre.objects.filter(id_anoletivo=turma.id_anoletivo)
    return render(request, 'regAula.html', {'professor': professor, 'turma': turma, 'disciplinas': disciplinas,
                                            'bimestres': bimestres})


def buscarAula(request, idAula):
    aula = Aula.objects.get(id_aula=idAula)
    return render(request, 'verAula.html', {'aula':aula})


def listAulas(request, idProfessor):
    aulas = Aula.objects.filter(id_professor=idProfessor)
    return render(request, 'listAulas.html', {'aulas':aulas})


def editAula(request, idAula):
    aula = Aula.objects.get(id_aula=idAula)
    formaula = AulaForm(request.POST or None, instance=aula)
    if formaula.is_valid():
        formaula.save()
        return redirect('listAulas', aula.id_professor.id_professor)
    return render(request, 'regAula.html', {'form': formaula, 'aula': aula})


def delAula(request, idAula):
    aula = Aula.objects.get(id_aula=idAula)
    professor = aula.id_professor
    if request.method == 'POST':
        aula.delete()
        return redirect('listAulas', professor.id_professor)
    return render(request,'aula-del-confirm.html',{'aula':aula})


def avaliacoes(request):
    return render(request,'avaliacoes.html')


def regAvaliacao(request, idTurma):
    Q1 = Q(situacao='C')
    Q2 = Q(situacao='RC')
    alunos = Aluno.objects.filter(Q1 | Q2, id_turma=idTurma)
    turma = Turma.objects.get(id_turma=idTurma)
    if request.method == 'POST':
        idDisc = request.POST['idDisc']
        disciplina = Disciplina.objects.get(id_disciplina=idDisc)
        idBim = request.POST['idBim']
        bimestre = Bimestre.objects.get(id_bimestre=idBim)
        for aluno in alunos:
            if str(aluno.id_aluno) in request.POST:
                avaliacao = Avaliacao()
                avaliacao.id_aluno = aluno
                avaliacao.id_turma = turma
                avaliacao.dataavaliacao = request.POST['dataavaliacao']
                avaliacao.id_disciplina = disciplina
                avaliacao.id_bimestre = bimestre
                avaliacao.nota = float(request.POST[str(aluno.id_aluno)])
                avaliacao.nomeavaliacao = request.POST['nomeavaliacao']
                avaliacao.save()
                set_situacao_aluno(aluno.id_aluno, turma.id_turma, disciplina.id_disciplina)
        return redirect('listAvaliacoes', idTurma)
    professor = Professor.objects.get(id_turma=idTurma)
    disciplinas = Disciplina.objects.all()
    bimestres = Bimestre.objects.all()
    return render(request, 'regAvaliacao.html', {'turma':turma, 'alunos':alunos, 'professor':professor, 'bimestres':bimestres, 'disciplinas':disciplinas})


def set_situacao_aluno(id_aluno, id_turma, id_disciplina):
    avaliacoes = Avaliacao.objects.filter(id_aluno=id_aluno, id_turma=id_turma, id_disciplina=id_disciplina)
    aluno = Aluno.objects.get(id_aluno=id_aluno)
    if aluno.situacao != 'T' and aluno.situacao != 'AB':
        soma = 0.0
        for avaliacao in avaliacoes:
            soma += float(avaliacao.nota)
        if len(avaliacoes) >= 4:
            if soma/4 < 6.0:
                aluno.situacao = 'RC'
        aluno.save()


def set_situacao_aluno_2(id_aluno, id_turma, id_disciplina):
    avaliacoes = Avaliacao.objects.filter(id_aluno=id_aluno, id_turma=id_turma, id_disciplina=id_disciplina)
    recuperacao = Recuperacao.objects.get(id_aluno=id_aluno, id_turma=id_turma, id_disciplina=id_disciplina)
    aluno = Aluno.objects.get(id_aluno=id_aluno)
    soma = 0.0

    for avaliacao in avaliacoes:
        soma += float(avaliacao.nota)

    soma += float(recuperacao.nota)

    if soma >= 6.0:
        aluno.situacao = 'C'
    else:
        aluno.situacao = 'R'

    aluno.save()


def set_resultado(id_aluno, id_turma):
    disciplinas = Disciplina.objects.all()
    avaliacoes = Avaliacao.objects.filter(id_aluno=id_aluno, id_turma=id_turma)
    aluno = Aluno.objects.get(id_aluno=id_aluno)
    resultados = []
    num_bimestres = Bimestre.objects.count()
    completou = True
    for disciplina in disciplinas:
        if Avaliacao.objects.filter(id_aluno=id_aluno, id_turma=id_turma, id_disciplina=disciplina.id_disciplina).count() < num_bimestres:
            completou = False
    if completou:
        situacao = 'A'
        for disciplina in disciplinas:
            media = 0.0
            for avaliacao in avaliacoes:
                if avaliacao.id_disciplina.id_disciplina == disciplina.id_disciplina:
                    media += float(avaliacao.nota)
            resultados.append([disciplina, media/num_bimestres])
    for resultado in resultados:
        if resultado[1] < 6.0:
            if Recuperacao.objects.filter(id_aluno=id_aluno, id_turma=id_turma, id_disciplna=resultado[0].id_disciplina).exists():
                recuperacao = Recuperacao.objects.get(id_aluno=id_aluno, id_turma=id_turma, id_disciplna=resultado[0].id_disciplina)
                if (resultado[1] * 2 + recuperacao.nota / 3) < 6.0:
                    situacao = 'R'
    aluno.situacao = situacao
    aluno.save()


def buscarAvaliacao(request, idAvaliacao):
    avaliacao = Avaliacao.objects.get(id_avaliacao = idAvaliacao)
    return render(request, 'verAvaliacao.html', {'avaliacao': avaliacao})


def listAvaliacoes(request, idTurma):
    turma = Turma.objects.get(id_turma=idTurma)
    avaliacoes = Avaliacao.objects.filter(id_turma=turma.id_turma)
    bimestres = Bimestre.objects.filter(id_anoletivo=turma.id_anoletivo.id_anoletivo)
    disciplinas = Disciplina.objects.all()

    return render(request,'listAvaliacoes.html',{'avaliacoes':avaliacoes, 'bimestres':bimestres, 'disciplinas': disciplinas})


def editAvaliacao(request, idAvaliacao):
    avaliacao = Avaliacao.objects.get(id_avaliacao=idAvaliacao)
    formavaliacao = AvaliacaoForm(request.POST or None, instance = avaliacao)
    if formavaliacao.is_valid():
        formavaliacao.save()
        return redirect('listAvaliacoes')
    return render(request, 'regAvaliacao.html', {'form': formavaliacao, 'avaliacao': avaliacao})


def delAvaliacao(request, idAvaliacao):
    avaliacao = Avaliacao.objects.get(id_avaliacao = idAvaliacao)
    if request.method == 'POST':
        avaliacao.delete()
        return redirect('listAvaliacoes')
    return render(request,'avaliacao-del-confirm.html',{'avaliacao': avaliacao})


def frequencias(request):
    return render(request,'frequencias.html')


def registrarFrequencia(request, idAula, idTurma):
    if request.method == 'POST':
        aula = Aula.objects.get(id_aula=idAula)
        turma = Turma.objects.get(id_turma=idTurma)
        alunos = Aluno.objects.filter(id_turma=idTurma)
        frequencias = ''
        bim = aula.id_bimestre
        for aluno in alunos:
            freq = request.POST.get(str(aluno.id_aluno))
            if freq == 'F':
                if bim.nome == '1':
                    aluno.faltas1 += 1
                elif bim.nome == '2':
                    aluno.faltas2 += 1
                elif bim.nome == '3':
                    aluno.faltas3 += 1
                else:
                    aluno.faltas4 += 1
            elif freq == 'P' or freq == 'FJ':
                if bim.nome == '1':
                    aluno.presenca1 += 1
                elif bim.nome == '2':
                    aluno.presenca2 += 1
                elif bim.nome == '3':
                    aluno.presenca3 += 1
                else:
                    aluno.presenca4 += 1
            aluno.faltastotal += aluno.faltas1 + aluno.faltas2 + aluno.faltas3 + aluno.faltas4
            aluno.presencatotal += aluno.presenca1 + aluno.presenca2 + aluno.presenca3 + aluno.presenca4
            aluno.save()
            frequencias = frequencias + str(aluno.id_aluno) + ':' + freq + ','

        frequencias = frequencias[0:len(frequencias)-1]

        frequencia = Frequencia()
        frequencia.id_turma = turma
        frequencia.id_aula = aula
        frequencia.frequencia = frequencias
        frequencia.save()
        aula.chamada = True
        aula.save()
        return redirect('listFrequencias', idTurma)
    alunos = Aluno.objects.filter(id_turma=idTurma)
    aula = Aula.objects.get(id_aula=idAula)
    return render(request, 'registrar-frequencia.html',{'alunos':alunos, 'aula':aula})


def buscarFrequencia(request, idFrequencia):
    frequencia = Frequencia.objects.get(id_frequencia = idFrequencia)
    id = frequencia.id_frequencia
    aula = frequencia.id_aula
    turma = frequencia.id_turma
    freq = frequencia.frequencia.split(',')
    list_alunos = []
    for itens in freq:
        aluno_e_freq = itens.split(':')
        id = aluno_e_freq[0]
        aluno = Aluno.objects.get(id_aluno=id)
        aluno_e_freq[0] = aluno
        list_alunos.append(aluno_e_freq)
    tipos = ['P','FJ','F']
    return render(request, 'verFrequencia.html', {'id':id, 'frequencia': list_alunos, 'turma':turma, 'aula':aula, 'tipos_frequencia':tipos})

def verFrequenciaAula(request, idAula):
    frequencia = Frequencia.objects.get(id_aula=idAula)
    strings_frequencia = frequencia.frequencia.split(',')
    list_alunos = []

    for itens in strings_frequencia:
        aluno_e_freq = itens .split(':')
        idaluno = aluno_e_freq[0]
        aluno = Aluno.objects.get(id_aluno=idaluno)
        aluno_e_freq[0] = aluno
        list_alunos.append(aluno_e_freq)
    tipos = ['P','FJ','F']
    return render(request, 'verFrequenciaAula.html', {'frequencia':frequencia, 'alunos':list_alunos, 'tipos_frequencia':tipos})


def listFrequencias(request, idTurma):
    frequencias = Frequencia.objects.filter(id_turma=idTurma)
    return render(request,'listFrequencias.html',{'frequencias':frequencias})


def editFrequencia(request, idFrequencia):
    frequencia = Frequencia.objects.get(id_frequencia=idFrequencia)
    formfrequencia = FrequenciaForm(request.POST or None, instance = frequencia)
    if formfrequencia.is_valid():
        formfrequencia.save()
        return redirect('listFrequencias')
    return render(request, 'registrar-frequencia.html', {'form': formfrequencia, 'frequencia': frequencia})


def delFrequencia(request, idFrequencia):
    frequencia = Frequencia.objects.get(id_frequencia = idFrequencia)
    if request.method == 'POST':
        frequencia.delete()
        return redirect('listFrequencias')
    return render(request,'frequencia-del-confirm.html',{'frequencia': frequencia})


def recuperacoes(request):
    return render(request,'recuperacoes.html')


def reg_recuperacao(request, idturma):
    if request.method == 'POST':
        idDisc = request.POST['idDisc']
        disciplina = Disciplina.objects.get(id_disciplina=idDisc)
        idBim = request.POST['idBim']
        bimestre = Bimestre.objects.get(id_bimestre=idBim)
        turma = Turma.objects.get(id_turma=idturma)
        alunos = Aluno.objects.filter(id_turma=idturma, situacao='RC')
        for aluno in alunos:
            if str(aluno.id_aluno) in request.POST:
                recuperacao = Recuperacao()
                recuperacao.id_aluno = aluno
                recuperacao.id_turma = turma
                recuperacao.datarecuperacao = request.POST['datarecuperacao']
                recuperacao.id_disciplina = disciplina
                recuperacao.id_bimestre = bimestre
                recuperacao.nota = float(request.POST[str(aluno.id_aluno)])
                recuperacao.nomeavaliacao = request.POST['nomerecuperacao']
                recuperacao.save()
                set_resultado(aluno.id_aluno, turma.id_turma)
        return redirect('list_recuperacoes', idturma)
    turma = Turma.objects.get(id_turma=idturma)
    professor = Professor.objects.get(id_turma=idturma)
    disciplinas = Disciplina.objects.all()
    alunos = Aluno.objects.filter(id_turma=idturma, situacao='RC')
    bimestres = Bimestre.objects.all()
    return render(request, 'reg-recuperacao.html', {'turma':turma, 'alunos':alunos, 'professor':professor,
                                                    'bimestres':bimestres, 'disciplinas':disciplinas})


# def set_situacao_aluno(id_aluno, id_turma, id_disciplina):
#     avaliacoes = Avaliacao.objects.filter(id_aluno=id_aluno, id_turma=id_turma, id_disciplina=id_disciplina)
#     aluno = Aluno.objects.get(id_aluno=id_aluno)
#     if aluno.situacao != 'T' and aluno.situacao != 'AB':
#         soma = 0.0
#         for avaliacao in avaliacoes:
#             soma += float(avaliacao.nota)
#         if len(avaliacoes) >= 4:
#             if soma/4 < 6.0:
#                 aluno.situacao = 'RC'
#         aluno.save()


def buscar_recuperacao(request, idrecuperacao):
    recuperacao = Recuperacao.objects.get(id_recuperacao=idrecuperacao)
    return render(request, 'ver-recuperacao.html', {'recuperacao': recuperacao})


def list_recuperacoes(request, idturma):
    turma = Turma.objects.get(id_turma=idturma)
    recuperacoes = Recuperacao.objects.filter(id_turma=turma.id_turma)
    bimestres = Bimestre.objects.filter(id_anoletivo=turma.id_anoletivo.id_anoletivo)
    disciplinas = Disciplina.objects.all()

    return render(request,'list-recuperacoes.html',{'recuperacoes': recuperacoes, 'bimestres': bimestres,
                                                    'disciplinas': disciplinas})


def edit_recuperacao(request, idrecuperacao):
    recuperacao = Recuperacao.objects.get(id_recuperacao=idrecuperacao)
    formrecuperacao = RecuperacaoForm(request.POST or None, instance=recuperacao)
    if formrecuperacao.is_valid():
        formrecuperacao.save()
        return redirect('list_recuperacoes')
    return render(request, 'reg-recuperacao.html', {'form': formrecuperacao, 'recuperacao': recuperacao})


def del_recuperacao(request, idrecuperacao):
    recuperacao = Recuperacao.objects.get(id_recuperacao = idrecuperacao)
    if request.method == 'POST':
        recuperacao.delete()
        return redirect('list_recuperacoes')
    return render(request,'recuperacao-del-confirm.html',{'recuperacao': recuperacao})