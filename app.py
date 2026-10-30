import os
import sqlite3
import gradio as gr

# Nome do banco de dados
DB_NAME = "hospital_inventory.db"


# Criar a tabela do banco de dados
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS assets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                location TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)

        conn.commit()


# Consultar os ativos cadastrados
def list_assets():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, name, quantity, location, status
            FROM assets
            ORDER BY id DESC
        """)

        return cursor.fetchall()


# Cadastrar um ativo
def add_asset(name, quantity, location, status):
    if not name or not name.strip():
        return (
            "Erro: Informe o nome do ativo.",
            list_assets(),
            name,
            quantity,
            location
        )

    try:
        if quantity is None or not float(quantity).is_integer():
            return (
                "Erro: Informe uma quantidade inteira.",
                list_assets(),
                name,
                quantity,
                location
            )

        quantity = int(quantity)

    except (ValueError, TypeError):
        return (
            "Erro: Informe uma quantidade válida.",
            list_assets(),
            name,
            quantity,
            location
        )

    if quantity < 0:
        return (
            "Erro: A quantidade não pode ser negativa.",
            list_assets(),
            name,
            quantity,
            location
        )

    if not location:
        return (
            "Erro: Selecione um local.",
            list_assets(),
            name,
            quantity,
            location
        )

    if not status:
        return (
            "Erro: Selecione um status.",
            list_assets(),
            name,
            quantity,
            location
        )

    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO assets (name, quantity, location, status)
                VALUES (?, ?, ?, ?)
            """, (name.strip(), quantity, location, status))

            conn.commit()

        return (
            "Ativo cadastrado com sucesso!",
            list_assets(),
            "",
            1,
            None
        )

    except sqlite3.Error:
        return (
            "Erro ao salvar o ativo no banco de dados.",
            list_assets(),
            name,
            quantity,
            location
        )


# Inicializar o banco de dados
init_db()


# Criar a interface do sistema
with gr.Blocks(title="Inventário Hospitalar") as demo:

    gr.Markdown("# Sistema de Inventário Hospitalar")

    gr.Markdown(
        "Sistema para cadastro e consulta de equipamentos e materiais de TI."
    )

    with gr.Tabs():

        # Aba de cadastro
        with gr.TabItem("Cadastro de Ativos"):

            asset_name = gr.Textbox(
                label="Nome do Ativo",
                placeholder="Ex: Computador Dell"
            )

            asset_qty = gr.Number(
                label="Quantidade",
                value=1,
                precision=0
            )

            asset_location = gr.Dropdown(
                label="Local",
                choices=[
                    "Bancada A de Estoque",
                    "Bancada B de Estoque",
                    "UTI - Setor Técnico",
                    "Pronto Socorro - Rack Principal"
                ],
                value=None
            )

            asset_status = gr.Dropdown(
                label="Status",
                choices=[
                    "Normal",
                    "Estoque Crítico",
                    "Manutenção Necessária"
                ],
                value="Normal"
            )

            submit_btn = gr.Button(
                "Cadastrar Ativo",
                variant="primary"
            )

            output_message = gr.Textbox(
                label="Mensagem",
                interactive=False
            )

        # Aba de consulta
        with gr.TabItem("Consulta de Estoque"):

            refresh_btn = gr.Button("Atualizar Lista")

            asset_table = gr.Dataframe(
                headers=[
                    "ID",
                    "Nome do Ativo",
                    "Quantidade",
                    "Local",
                    "Status"
                ],
                value=list_assets(),
                interactive=False
            )

    # Cadastrar ativo e atualizar a tabela
    submit_btn.click(
        fn=add_asset,
        inputs=[
            asset_name,
            asset_qty,
            asset_location,
            asset_status
        ],
        outputs=[
            output_message,
            asset_table,
            asset_name,
            asset_qty,
            asset_location
        ]
    )

    # Atualizar a lista de ativos
    refresh_btn.click(
        fn=list_assets,
        inputs=None,
        outputs=asset_table
    )

# Iniciar a aplicação
if __name__ == "__main__":
    import os

    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7862)),
        share=False
    )
