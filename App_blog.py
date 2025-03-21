from blog import show_menu, add_post, add_user, query_users_posts

while True:
    show_menu()
    try:
        option = int(input("Selecione uma opção:\n"))
    except ValueError:
        print("Entrada deve ser um número.")
        continue
    
    match option:
        case 1:
            add_user()
        case 2:
            add_post()
        case 3:
            query_users_posts()
        case 4:
            print("Saindo!")
            break
        case _:
            print("Opção inválida!")
            continue
                