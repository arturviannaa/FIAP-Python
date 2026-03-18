def recomendar_filme(idade, genero):
    genero = genero.strip().lower()

    if genero in ["ação", "acao"]:
        if idade < 14:
            return "Os Incríveis"
        return "Batman: O Cavaleiro das Trevas"

    if genero == "drama":
        if idade < 14:
            return "Extraordinário"
        return "O Lado Bom da Vida"

    return "Gênero não disponível no catálogo"

idade_usuario = int(input("Digite sua idade: "))
genero_usuario = input("Digite o genero (ação/drama): ")

recomendacao = recomendar_filme(idade_usuario, genero_usuario)
print(recomendacao)