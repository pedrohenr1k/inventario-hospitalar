# Mapeamento de Endpoints e Verbos HTTP

from flask import Blueprint
from controllers.user_controller import (
    listar_usuarios,
    buscar_usuario_por_id,
    criar_usuario,
    atualizar_usuario,
    deletar_usuario
)

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/usuarios", methods=["GET"])
def get_usuarios():
    return listar_usuarios()

@user_bp.route("/usuarios/<int:id>", methods=["GET"])
def get_usuario_por_id(id):
    return buscar_usuario_por_id(id)

@user_bp.route("/usuarios", methods=["POST"])
def post_usuario():
    return criar_usuario()

@user_bp.route("/usuarios/<int:id>", methods=["PUT"])
def put_usuario(id):
    return atualizar_usuario(id)

@user_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def delete_usuario(id):
    return deletar_usuario(id)