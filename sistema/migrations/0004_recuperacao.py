# Generated by Django 3.0.2 on 2020-02-01 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_auto_20200201_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recuperacao',
            fields=[
                ('id_recuperacao', models.AutoField(primary_key=True, serialize=False)),
                ('nomerecuperacao', models.CharField(max_length=100, verbose_name='Título da avaliacao')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=5)),
                ('datarecuperacao', models.DateField(verbose_name='Data da Avaliação')),
                ('id_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.Aluno', verbose_name='Aluno')),
                ('id_bimestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.Bimestre', verbose_name='Bimestre')),
                ('id_disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.Disciplina', verbose_name='Disciplina')),
                ('id_turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.Turma', verbose_name='Turma')),
            ],
        ),
    ]