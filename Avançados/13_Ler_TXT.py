from Geral import cls, parada

while True:
    nomeArquivo = input("Informe o nome do arquivo (FIM para encerrar):\n")
    if (nomeArquivo.upper() == "FIM"):
        break

    print()

    try:
        arquivo = open(nomeArquivo, "r")
        linhas = arquivo.readlines()
        print("*** Conteúdo do arquivo:")
        for linha in linhas:
            print(linha, end="")

        print()
        parada()
        arquivo.close()
        cls()

    except IOError:
        print(f"Erro: o arquivo \"{nomeArquivo}\", não foi encontrado.\n")
