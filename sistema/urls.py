
from django.urls import path
from django.conf.urls import url
from .views import *
urlpatterns = [
    # url(r'^pdf/$', GeneratePDF.as_view()),
    # url(r'^diario/$', DiarioToPDF.as_view()),
    path('alunos/ver/<int:idAluno>/historico/', generatePDF, name='generatePDF'),
    path('turmas/ver/<int:idTurma>/diario/', diarioToPDF, name='diarioToPDF'),

    path('', home, name='home'),
    path('login/professor(a)/', login_prof, name='login_prof'),
    path('login/professor(a)/submit', submit_prof, name='submit_prof'),

    path('turmas', turmas, name='turmas'),
    path('turmas/registrar', registrarTurma, name='registrarTurma'),
    path('turmas/ver/<int:idTurma>/', buscarTurma, name='buscarTurma'),
    path('turmas/listar', listarTurmas, name='listarTurmas'),
    path('turmas/editar/<int:idTurma>/', editarTurma, name='editarTurma'),
    path('turmas/deletar/<int:idTurma>/', deletarTurma, name='deletarTurma'),

    path('anosletivos', anosletivos, name='anosletivos'),
    path('anosletivos/registrar', registrarAnoletivo, name='regAnoLetivo'),
    path('anosletivos/ver/<int:idanoletivo>/', buscarAnoLetivo, name='buscarAnoLetivo'),
    path('anosletivos/listar', listAnosLetivos, name='listAnosLetivos'),
    path('anosletivos/editar/<int:idAnoLetivo>/', editarAnoLetivo, name='editAnoLetivo'),
    path('anosletivos/deletar/<int:idAnoLetivo>/', deletarAnoLetivo, name='deletarAnoLetivo'),

    path('alunos', alunos, name='alunos'),
    path('alunos/registrar', registrarAluno, name='registrarAluno'),
    path('alunos/ver/<int:idAluno>/', buscarAluno, name='buscarAluno'),
    path('alunos/listar', listarAlunos, name='listarAlunos'),
    path('alunos/editar/<int:idAluno>/', editarAluno, name='editarAluno'),
    path('alunos/deletar/<int:idAluno>/', deletarAluno, name='deletarAluno'),

    path('professores', profs, name='profs'),
    path('professores/registrar', registrarProf, name='registrarProf'),
    path('professores/ver/<int:idProf>/', buscarProf, name='buscarProf'),
    path('professores/listar', listarProfs, name='listarProfs'),
    path('professores/editar/<int:idProf>/', editarProf, name='editarProf'),
    path('professores/deletar/<int:idProf>/', deletarProf, name='deletarProf'),

    path('disciplinas', disciplinas, name='disciplinas'),
    path('disciplinas/registrar', registrarDisc, name='registrarDisc'),
    path('disciplinas/ver/<int:idDisc>/', buscarDisc, name='buscarDisc'),
    path('disciplinas/listar', listarDiscs, name='listarDiscs'),
    path('disciplinas/editar/<int:idDisc>/', editarDisc, name='editarDisc'),
    path('disciplinas/deletar/<int:idDisc>/', deletarDisc, name='deletarDisc'),

    path('bimestres', bimestres, name='bimestres'),
    path('bimestres/registrar', regBimestre, name='regBimestre'),
    path('bimestres/ver/<int:idBim>/', buscarBimestre, name='buscarBimestre'),
    path('bimestres/listar', listBimestres, name='listBimestres'),
    path('bimestres/editar/<int:idBim>/', editBimestre, name='editBimestre'),
    path('bimestres/deletar/<int:idBim>/', delBimestre, name='delBimestre'),

    path('aulas', aulas, name='aulas'),
    path('aulas/registrar/<int:idProfessor>', regAula, name='regAula'),
    path('aulas/ver/<int:idAula>/', buscarAula, name='buscarAula'),
    path('listar/aulas/professor(a)/<int:idProfessor>', listAulas, name='listAulas'),
    path('aulas/editar/<int:idAula>/', editAula, name='editAula'),
    path('aulas/deletar/<int:idAula>/', delAula, name='delAula'),

    path('avaliacoes', avaliacoes, name='avaliacoes'),
    path('avaliacao/registrar/<int:idTurma>', regAvaliacao, name='regAvaliacao'),
    path('avaliacao/ver/<int:idAvaliacao>/', buscarAvaliacao, name='buscarAvaliacao'),
    path('avaliacao/listar/<int:idTurma>', listAvaliacoes, name='listAvaliacoes'),
    path('avaliacao/editar/<int:idAvaliacao>/', editAvaliacao, name='editAvaliacao'),
    path('avaliacao/deletar/<int:idAvaliacao>/', delAvaliacao, name='delAvaliacao'),

    path('recuperacoes', recuperacoes, name='recuperacoes'),
    path('recuperacao/registrar/<int:idturma>', reg_recuperacao, name='reg_recuperacao'),
    path('recuperacao/ver/<int:idrecuperacao>/', buscar_recuperacao, name='buscar_recuperacao'),
    path('recuperacao/listar/<int:idturma>', list_recuperacoes, name='list_recuperacoes'),
    path('recuperacao/editar/<int:idrecuperacao>/', edit_recuperacao, name='edit_recuperacao'),
    path('recuperacao/deletar/<int:idrecuperacao>/', del_recuperacao, name='del_recuperacao'),

    path('frequencias', frequencias, name='frequencias'),
#    path('frequencias/registrar', regFrequencia, name='regFrequencia'),
    path('registrar/frequencia/<int:idAula>/<int:idTurma>', registrarFrequencia, name='registrarFrequencia'),
    path('frequencias/ver/<int:idFrequencia>/', buscarFrequencia, name='buscarFrequencia'),
    path('aula/frequencia/<int:idAula>', verFrequenciaAula, name='verFrequenciaAula'),
    path('frequencias/listar/<int:idTurma>', listFrequencias, name='listFrequencias'),
    path('frequencias/editar/<int:idFrequencia>/', editFrequencia, name='editFrequencia'),
    path('frequencias/deletar/<int:idFrequencia>/', delFrequencia, name='delFrequencia'),

    # path('aluno/imprimir/<int:idAluno>', imprimirTable, name='imprimirAluno'),
]