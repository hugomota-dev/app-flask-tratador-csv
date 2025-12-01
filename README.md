# Projeto: Tratador de Arquivos CSV

### Versão: 1.0

### Status: Em desenvolvimento

## 1. Visão Geral do Projeto

Este projeto utiliza Flask com uma estrutura de *Application Factory* e integração de *frontend* moderna via Tailwind CSS v4.x e PostCSS.

### 1.1 Estrutura de Pastas e Arquivos

A estrutura do projeto é organizada de forma modular (ou pacote):

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

## 2. Configuração do Ambiente Python (Backend)

Esta seção aborda a configuração do ambiente virtual e as dependências Python.

### 2.1 Criar e Ativar um Ambiente Virtual

No terminal (usando Bash ou PowerShell no VS Code), execute o comando para criar o ambiente virtual chamado `.venv`:

```bash
python -m venv .venv
```

Antes de começar a trabalhar no projeto, ative o ambiente virtual:
```bash
# Para Linux/macOS ou terminal bash (meu uso no VScode)
. .venv/Scripts/activate

# Para Windows (Command Prompt)
.venv\Scripts\activate
```

### 2.2 Criar e Ativar um Ambiente Virtual
Dentro do ambiente virtual, instale o Flask e as bibliotecas auxiliares:
```bash
pip install Flask python-dotenv livereload
```

### 2.3 Gerar o Arquivo de Requisitos
Após instalar todas as dependências Python, use este comando para gerar o arquivo requirements.txt que lista exatamente quais pacotes seu projeto precisa:

```bash
pip freeze > requirements.txt
```

## 3. Configuração do Frontend (Tailwind CSS v4.x via PostCSS)

Esta seção configura as ferramentas de frontend usando Node.js e NPM.

### 3.1 Inicializar o NPM e Instalar Dependências do Tailwind
Execute este comando na raiz do seu projeto para criar o arquivo package.json e instalar os pacotes necessários:
```bash
npm init -y
npm install -D tailwindcss@next @tailwindcss/postcss postcss autoprefixer @tailwindcss/cli concurrently
```

### 3.2 Criar Arquivos de Configuração Manuais (Formato .mjs)

Crie manualmente os arquivos tailwind.config.mjs e postcss.config.mjs na raiz do seu projeto.
Crie tailwind.config.mjs:

```bash
// tailwind.config.mjs
export default {
  content: [
    "./application/templates/**/*.html",
    "./application/static/src/**/*.{js,ts}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};

```

Crie postcss.config.mjs:
```bash
// postcss.config.mjs
export default {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};

```

### 3.3 Criar Arquivo de Entrada CSS
Crie o diretório application/static/src/ e o arquivo CSS de entrada:
Crie o arquivo application/static/src/input.css:

```bash
/* application/static/src/input.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

```

## 4. Orquestração e Execução do Projeto

Esta seção configura os scripts para rodar o servidor Flask e o compilador Tailwind simultaneamente.

### 4.1 Configurar Scripts no package.json
Edite o arquivo package.json (criado no Passo 3.1) para adicionar os scripts de compilação do CSS e o script dev que usa concurrently.

```bash
{
  # ... (outras chaves) ...
  "scripts": {
    "build:css": "tailwindcss --input application/static/src/input.css --output application/static/dist/output.css",
    "watch:css": "tailwindcss --input application/static/src/input.css --output application/static/dist/output.css --watch",
    "start:flask": "python csv_handler_run.py",
    
    # NOVO: Script principal que roda ambos simultaneamente
    "dev": "concurrently \"npm run start:flask\" \"npm run watch:css\""
  },
  # ... (devDependencies atualizadas) ...
}

```

### 4.2 Vincular o CSS Compilado no Template Flask

Atualize seu template base (application/templates/base.html) para garantir que ele aponte para o arquivo de saída compilado (output.css).


```html
<!-- ... dentro do <head> ... -->
    <link rel="stylesheet" href="{{ url_for('static', filename='dist/output.css') }}">
    <!-- ... -->
```

### 4.3 Iniciar o Ambiente de Desenvolvimento

Abra seu terminal na raiz do projeto e inicie ambos os processos com um único comando:
```bash
npm run dev
```



### Bibliografia

- https://flask.palletsprojects.com/en/stable/installation/
- https://kinsta.com/pt/blog/aplicativo-python-flask/
- https://jinja.palletsprojects.com/en/stable/templates/
- https://livereload.readthedocs.io/en/latest/integrations/flask.html
