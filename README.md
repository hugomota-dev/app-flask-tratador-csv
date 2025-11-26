# Projeto: Tratador de Arquivos CSV

### Versão: 1.0

### Status: Em desenvolvimento

1. Visão Geral do Projeto

### Criar um ambiente

No terminal bashdo VScode execute o comando:

```bash
python -m venv .venv
```

### Ative o ambiente virtual

Antes de começar a trabalhar no projeto, ative o ambiente virtual que você criou:

```bash
. .venv/Scripts/activate
```

### Instale o Flask

Dentro do ambiente virtual, use o seguinte comando para instalar o Flask:

```bash
pip install Flask
```

### Instale a pacote python-dotenv

Esse pacote permitirá usar variáveis de ambiente no projeto:

```bash
pip install python-dotenv
```

### Estrutura de pastas e arquivos. Usando o aplicativo como pacote.

```csharp
project/
│
├── application/
│   ├── __init__.py              # Criação da app (Application Factory)
│   ├── routes.py                # Rotas principais
│   │
│   ├── services/                # Regras de negócio (tratamento CSV)
│   │   ├── __init__.py
│   │   └── csv_service.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   │
│   │   └── components/
│   │       ├── _button.html
│   │       ├── _footer.html
│   │       └── _header.html
│   │
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │
│   └── config.py                # Configurações opcionais
│
├── instance/
│   └── config.py                # Configurações locais (git-ignore)
│
├── csv_handler_run.py        # Arquivo para rodar a aplicação
├── requirements.txt
└── README.md

```

### Facilitadores para ambiente de desenvolvimento:

O Livereload é um recurso que proporciona atualização automática do navegador durante o desenvolvimento, sempre que alterações são feitas no código ou nos templates. Isso aprimora o fluxo de trabalho de desenvolvimento, eliminando a necessidade de atualizações manuais do navegador.
Instale o livereload com pip:

```bash
pip install livereload
```


### Bibliografia

- https://flask.palletsprojects.com/en/stable/installation/
- https://kinsta.com/pt/blog/aplicativo-python-flask/
- https://jinja.palletsprojects.com/en/stable/templates/
- https://livereload.readthedocs.io/en/latest/integrations/flask.html
