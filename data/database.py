# Simulador de Banco de Dados em Memória

usuarios = [
    {"id": 1, "nome": "Pedro Oliveira", "email": "pedro@email.com"},
    {"id": 2, "nome": "Ana Silva", "email": "ana@email.com"}
]

proximo_id = 3

def gerar_novo_id():
    global proximo_id
    id_atual = proximo_id
    proximo_id += 1
    return id_atual