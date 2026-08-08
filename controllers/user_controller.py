# Lógica de Negócio e Validações

from flask import request, jsonify
from data.database import usuarios, gerar_novo_id

def listar_usuarios():
    return jsonify(usuarios), 200

def buscar_usuario_por_id(id_usuario):
    usuario_encontrado = next((u for u in usuarios if u["id"] == id_usuario), None)
    
    if not usuario_encontrado:
        return jsonify({"erro": "Usuário não encontrado"}), 404
        
    return jsonify(usuario_encontrado), 200

def criar_usuario():
    dados = request.get_json()

    if not dados:
        return jsonify({"error": "O corpo da requisição é obrigatório e deve estar no formato JSON."}), 400

    nome = dados.get("nome")
    email = dados.get("email")

    if not nome or not str(nome).strip():
        return jsonify({"error": "O campo 'nome' é obrigatório e não pode estar em branco."}), 400

    if not email or not str(email).strip():
        return jsonify({"error": "O campo 'email' é obrigatório e não pode estar em branco."}), 400

    novo_usuario = {
        "id": gerar_novo_id(),
        "nome": nome.strip(),
        "email": email.strip()
    }

    usuarios.append(novo_usuario)
    return jsonify({"data": novo_usuario}), 201

def atualizar_usuario(id_usuario):
    usuario_encontrado = next((u for u in usuarios if u["id"] == id_usuario), None)
    
    if not usuario_encontrado:
        return jsonify({"erro": "Usuário não encontrado"}), 404
        
    dados = request.get_json()
    usuario_encontrado["nome"] = dados.get("nome", usuario_encontrado["nome"])
    usuario_encontrado["email"] = dados.get("email", usuario_encontrado["email"])
    
    return jsonify(usuario_encontrado), 200

def deletar_usuario(id_usuario):
    usuario_encontrado = next((u for u in usuarios if u["id"] == id_usuario), None)
    
    if not usuario_encontrado:
        return jsonify({"erro": "Usuário não encontrado"}), 404
        
    usuarios.remove(usuario_encontrado)
    return jsonify({"mensagem": "Usuário removido com sucesso"}), 200