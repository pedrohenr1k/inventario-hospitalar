#  Sistema de Inventário Hospitalar

##  Sobre o Projeto

O Sistema de Inventário Hospitalar é um MVP (Produto Mínimo Viável) desenvolvido para facilitar o cadastro e a consulta de equipamentos e materiais de TI em um ambiente hospitalar.

A aplicação permite registrar ativos, informar suas quantidades, definir os locais de armazenamento e acompanhar seus status.

##  Funcionalidades

- **Cadastro de ativos:** registro do nome e da quantidade dos equipamentos.
- **Definição de localização:** seleção do local onde o ativo está armazenado.
- **Controle de status:** classificação dos ativos como Normal, Estoque Crítico ou Manutenção Necessária.
- **Consulta de estoque:** visualização dos ativos cadastrados em uma tabela.
- **Banco de dados local:** armazenamento das informações utilizando SQLite.
- **Validação de dados:** verificação de campos obrigatórios e da quantidade informada.

##  Tecnologias Utilizadas

- **Python:** linguagem de programação utilizada no desenvolvimento.
- **Gradio:** biblioteca utilizada para construir a interface web.
- **SQLite:** banco de dados utilizado para armazenar os ativos.
- **GitHub:** plataforma utilizada para hospedar o código-fonte.

##  Estrutura do Projeto

```text
inventario-hospitalar/
├── app.py
├── .gitignore
└── README.md
```

O arquivo `hospital_inventory.db` é criado localmente quando a aplicação é executada, caso ainda não exista.

##  Como Executar o Projeto

### 1. Instale o Python

Instale o Python em seu computador e verifique se ele está disponível no terminal.

### 2. Instale a dependência

Abra o terminal na pasta do projeto e execute:

```bash
pip install gradio
```

### 3. Execute a aplicação

No terminal, execute:

```bash
python app.py
```

### 4. Acesse o sistema

Abra o navegador e acesse:

http://127.0.0.1:7861

##  Banco de Dados

O sistema utiliza SQLite para armazenar os ativos cadastrados.

Cada registro possui os seguintes campos:

| Campo | Descrição |
|---|---|
| ID | Identificador único do ativo |
| Nome | Nome do equipamento ou material |
| Quantidade | Quantidade registrada |
| Local | Local de armazenamento |
| Status | Situação atual do ativo |

## Objetivo do MVP

Demonstrar uma solução inicial para o controle de equipamentos e materiais de TI em um ambiente hospitalar, oferecendo recursos básicos de cadastro e consulta de estoque.

##  Status do Projeto

MVP em desenvolvimento.
