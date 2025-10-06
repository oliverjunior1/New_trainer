def kwargs_args(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

while True:
    entrada = input("Put the dates (ex: nome=Joaquim, idade=30): ").strip()
    if entrada.lower() == "fim":
        break

    try:
        # Converte a string em um dicionário usando expressão segura
        pares = entrada.split(",")
        dados = {}
        for par in pares:
            chave, valor = par.split("=")
            dados[chave.strip()] = valor.strip()

        kwargs_args(**dados)

    except Exception as e:
        print("Erro ao processar os dados:", e)