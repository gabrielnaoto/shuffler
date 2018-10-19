from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        from core.models import Student
        students = ['Acauã Emanuel Ribeiro;B',
                    'Adrian Grosch;A',
                    'Adrian Schlei;B',
                    'Adriano Henrique dos Santos;B',
                    'Alan Marcos Kubiak;B',
                    'Bianca Santana Hillesheim;A',
                    'Carla Tahís Dalmolin;B',
                    'Cesar Augusto Freire;B',
                    'Eduardo Radloff;A',
                    'Elias Celso Mendes;A',
                    'Eloisa Renata Schons;B',
                    'Ericson Franzen;A',
                    'Gustavo Ceola;B',
                    'Haroldo Luiz Beyer Bacellar;B',
                    'Igor Ceola;B',
                    'Igor Hafemann;B',
                    'Igor José Xavier;A',
                    'Jackson Castilho da Luz;B',
                    'Jackson Correa Gutz;B',
                    'Jean Carlos Tessarollo;B',
                    'João Elias Engelbrecht Kayser;A',
                    'João Victor Cardoso de Souza;B',
                    'Jonas Figueredo;B',
                    'José Carvalho Matos Júnior;B',
                    'Juarez da Cunha;B',
                    'Karolayne Silveira Mendes;A',
                    'Leandro Luiz Schoninger Filho;B',
                    'Lucas Lombardi Floriano;B',
                    'Lucas Samuél Karsten;A',
                    'Maicon Amarante Mendes;B',
                    'Marcelo Fellipe Hammes;A',
                    'Márcio Schroeder da Costa;B',
                    'Matheus Henrique Costa;B',
                    'Matheus Henrique Setoyama da Maia;B',
                    'Matheus Parro de Sousa;A',
                    'Mauricio Manoel Sagaz;A',
                    'Maurício Sucheuski;A',
                    'Rafael Oliveira Silva;B',
                    'Rafael Vinícius Schneider;A',
                    'Rafael Zink;A',
                    'Raimundo Nonato da Silva Nascimento;A',
                    'Renan Ricardo Holler;B',
                    'Rodrigo Cassiano;A',
                    'Roger Henrique Cavichioli;B',
                    'Rudney Dolla;A',
                    'Ryan Carlos Meneghelli;B',
                    'Thiago Samuel Stahnke;A']

        for student in students:
            partial = student.split(';')
            Student.objects.get_or_create(name=partial[0], rank=partial[1])
