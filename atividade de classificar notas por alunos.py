alunos = {"Alexandre":{"Portugues": [9.5,10] ,"Matematica": [10,10] ,"Ingles":[7.3,10] ,"Geografia": [8.5,10]},
"Artur":{"Portugues": [9.5,10],"Matematica": [8,10],"Ingles": [7.3,10],"Geografia": [8.5,10]},
"Jose":{"Portugues": [9.5,10] ,"Matematica": [1,10] ,"Ingles": [7.3,10],"Geografia": [8.5,10]} }


def media_por_aluno(notas):
    for nomes, materias in alunos.items():
        print(f"aluno {nomes}")
        for materia, notas in materias.items():
            media= sum(notas)/len(notas)
            print(f"{materia}: {media}")

def media_geral_dos_alunos():
    for nomes, materias in alunos.items():
        print(f"Aluno: {alunos}")
        total = 0
        quantidade = 0
        for materias, notas in materias.items():
            print(f"Materia: {notas}")
            total += notas
            quantidade += 1 
            media= total/quantidade
            print(f"Media geral de {nomes}:{media:.2f}")


def media_por_materia():
    materias= {}
    for nomes,materias in alunos.items():
        for materias, notas in materias.items():
            if materias not in materias:
                materias=[materia]= []
            materias=[materia].append(notas)
            print("Media por materia")
            for materias,notas in materias.items():
                media= sum(notas)/len(notas)
            print(f"Media geral de {nomes}:{media:.2f}")
                
def melhor_aluno():
    for nomes,materias in alunos.items():
        todas_notas=[]
        for materias,notas in materias.items():
            todas_notas.extend(notas)
            media = sum(todas_notas)/len(todas_notas)
            if media_por_aluno > 8.5:
                print(f"Aluno destaque do mês:{nomes} com sua incrivel media de {media:.2f}")
            else:
                print(f"Alunos abaixo da media:{nomes}")
 
def atualizar_notas():
    for nomes,materias in alunos.items():
        if nomes in alunos:
            for materias,notas in materias.items():
                if materias in notas:
                    alunos[nomes][materias].append(notas)
                    print(f"Nota {notas} adicionar para o aluno {nomes} na materia {materias}")
                else:
                    print(f"Materia {materias} não encontrada para o aluno {nomes}.")
            else:
                print(f"Aluno {nomes} não encontrado.")


def menu():
    print("/n===MENU===")
    print("1- Media por aluno")
    print("2- Media geral")
    print("3- Media por materia")
    print("4- Melhor aluno")
    print("5- Atualizaação de notas")
    print("6- sair")


alunos={}
while True: 
    opcao=input("Escolha uma opção")
    if opcao == '1':
        media_por_aluno()
    elif opcao == '2':
        media_geral_dos_alunos()
    elif opcao == '3':
        media_por_materia()
    elif opcao == '4':
        melhor_aluno()
    elif opcao == '5':
        atualizar_notas()
    elif opcao == '6':
        print("Encerrando o programa...")
    break
else:
    print("opção invalida")
menu()


