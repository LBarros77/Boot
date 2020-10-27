from DB import *

def head(msg):
    print("-" * 60)
    print(msg.center(60))
    print("-" * 60)

def title(msg, msg2):
    print(msg.center(30), msg2.center(30))
    print("-" * 60)

def lin():
    print("-" * 60)
    
def tools_db(user):
    dates_list = ["Hashtags", "Comentários"]
    for n, i in enumerate(dates_list):
        print(f"\033[33m{n+1}\033[m- \033[34m{i}\033[m")
    while True:
        try:
            answer = int(input("Digite uma opção: "))
            if answer == 1 or answer == 2:
                break
            else:
                print("Número invalido")
        except Exception:
            print("Opção invalida")
    if answer == 1:
        while True:
            head("hashtag")
            dates_list = ["Ver hashtags", "Adicionar hashtags", "Excluir hashtag", "Excluir lista de hashtags", "Voltar"]
            for n, date in enumerate(dates_list):
                print(f"\033[33m{n+1}\033[m- \033[34m{date}\033[m")
            while True:
                try:
                    answer = int(input("Digite uma opção: "))
                    if answer >= 1 and answer <= 5:
                        break
                    else:
                        print("Número invalido")
                except Exception:
                    print("Opção invalida")
            if answer == 1:
                head("Ver hashtags")
                hashtag_read(user)
            elif answer == 2:
                head("Adicionar hastags")
                hashtag_add(user)
            elif answer == 3:
                head("Excluir hashtag")
                hashtag_rm(user)
            elif answer == 4:
                head("Excluir lista de hashtags")
                hashtag_rm_list(user)
            else:
                break
            lin()
    else:
        while True:
            head("Comentário")
            dates_list = ["Ver comentários", "Adicionar comentários", "Excluir comentário", "Excluir lista de comentários", "Voltar"]
            for n, line in enumerate(dates_list):
                print(f"\033[33m{n+1}\033[m- \033[34m{line}\033[m")
            while True:
                try:
                    answer = int(input("Digite uma opção: "))
                    if answer >= 1 and answer <= 5:
                        break
                    else:
                        print("Número invalido")
                except Exception:
                    print("Opção invalida")
            if answer == 1:
                head("Ver comentários")
                comment_read(user)
            elif answer == 2:
                head("Adicionar comentários")
                comment_add(user)
            elif answer == 3:
                head("Excluir comentário")
                comment_rm(user)
            elif answer == 4:
                head("Excluir lista de comentários")
                comment_rm_list(user)
            else:
                break
            lin()
    menu2()

def menu2():
    '''
    Recebe nome de lista.txt
    Retorna resultados de funções: showList, add, newList ou opção sair
    '''
    options = ["Ver pessoas cadastradas", "Adicionar pessoa", "Excluir pessoa", "outros", "Voltar"]
    while True:
        head("SISTEMA DE ARMAZENAMENTO")
        for n, i in enumerate(options):
            print(f"\033[33m{n+1}\033[m- \033[34m{i}\033[m")
        lin()
        try:
            answer = int(input("Digite uma opção: "))
            if answer == 1:
                head("Lista de pessoas cadastradas")
                title("Usuário", "Senha")
                people_register(seed=True)
            elif answer == 2:
                head("Adicionar usuário")
                username = input("Usuário: ")
                people_register_add(username)
                head("Adicione as hahtags")
                hashtag_add(username)
                head("Adicione os comentários")
                comment_add(username)
            elif answer == 3:
                head("Excluir usuário")
                while True:
                    q = input("Quer continuar [S/N]? ")[0].upper()
                    if q in "SN":
                        if q == "S":
                            people_register_rm()
                            break
                        else:
                            break
            elif answer == 4:
                username = input("Usuário: ")
                head(f"Informações sobre {username}")
                tools_db(username)
            elif answer == 5:
                menu()
            else:
                print("\033[31mERRO! Digite um valor valido\033[m")
        except Exception as e:
            print(e)

def menu():
    head("LOGIN")
    while True:
        head("MENU PRINCIPAL")
        options = ["Like em explore", "Like e comentário em explore", "Like em #", "Like e comentário em #", "Like em público ativo",
         "Like e comentário em P/ativo", "Like em P/ativo de #", "Like e comentário em P/ativo de #", "Modo automatico", "Outros", "Sair do sistema"]
        for n, i in enumerate(options):
            print(f"\033[33m{n+1}\033[m- \033[34m{i}\033[m")
        lin()
        answer = int(input("Digite uma opção: "))
        if answer >= 1 and answer <= 9:
            from packages import instagram
            register = people_register(False)
            for user, password in register.items():
                print("Usuáro selecionado ", user)
                try:
                    if answer == 1:
                        head("Like em explore")
                        instagram(user, password).login()
                    elif answer == 2:
                        head("Like e comentário em explore")
                        instagram(user, password).login(comment=True)
                    elif answer == 3:
                        head("Like em #")
                        instagram(user, password).login(hashtag=True)
                    elif answer == 4:
                        head("Like e comentário em #")
                        instagram(user, password).login(comment=True, hashtag=True)
                    elif answer == 5:
                        head("Like em público ativo do axplore")
                        instagram(user, password).login(commentadors=True)
                    elif answer == 6:
                        head("Like e comentário em P/ativo do explore")
                        instagram(user, password).login(comment=True, commentadors=True)
                    elif answer == 7:
                        head("Like em P/ativo de #")
                        instagram(user, password).login(hashtag=True, commentadors=True)
                    elif answer == 8:
                        head("like e comentário em P/ativo de #")
                        instagram(user, password).login(comment=True, hashtag=True, commentadors=True)
                    elif answer == 9:
                        head("Modo automático")
                        instagram(user, password).login(automatic=True)
                    lin()
                except Exception as e:
                    print("Digite um número valido ", e)
        else:
            if answer == 10:
                menu2()
            elif answer == 11:
                head("Volte sempre!")
                break
            else:
                print("\033[31mERRO! Digite um valor valido\033[m")
