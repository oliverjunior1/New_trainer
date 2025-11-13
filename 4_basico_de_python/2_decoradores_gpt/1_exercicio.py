def log_execucao(x):
    def wrapper(*args, **kwargs):
        print("########################")
        x(*args, **kwargs)
        print("########################")
    return wrapper

@log_execucao
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Joaquim")