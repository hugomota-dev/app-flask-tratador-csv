# 📄 Especificação de Requisitos — Tratador de Arquivos CSV

**Versão:** 1.0  
**Status:** Em desenvolvimento  
**Autor:** HM  
**Data:** 01/12/2025

---

## 1. Visão Geral do Projeto
O **Tratador de Arquivos CSV** é uma aplicação web em **Flask** cujo objetivo é permitir que usuários enviem um arquivo CSV, selecionem colunas específicas e gerem um novo arquivo filtrado. A proposta é entregar uma ferramenta simples, rápida e eficiente para manipulação de dados tabulares.

---

## 2. Objetivos do Sistema
- Facilitar a seleção e filtragem de colunas de arquivos CSV.  
- Gerar rapidamente um novo arquivo CSV com somente as colunas desejadas.  
- Disponibilizar uma interface simples e responsiva (Tailwind CSS).  
- Garantir execução leve e consistente.

---

## 3. Escopo do Sistema

### 3.1 Funcionalidades Inclusas
- [ ] Upload de arquivo CSV  
- [ ] Validação do arquivo enviado  
- [ ] Leitura segura e processamento do CSV  
- [ ] Exibição dinâmica das colunas disponíveis  
- [ ] Interface para seleção de colunas  
- [ ] Geração do novo CSV filtrado  
- [ ] Download automático do arquivo gerado  
- [ ] Layout responsivo usando Tailwind CSS  
- [ ] Tratamento de erros amigáveis

### 3.2 Funcionalidades Futuras (Opcional)
- [ ] Histórico de arquivos enviados  
- [ ] Renomeação de colunas  
- [ ] Limpeza automática dos dados (trim, remoção de caracteres)  
- [ ] Exportação para XLSX  
- [ ] Criação de presets de seleção de colunas  
- [ ] API para automação externa

---

## 4. Público-Alvo
- Usuários que precisam extrair colunas específicas de CSV  
- Profissionais de TI  
- Analistas de dados  
- Usuários que manipulam planilhas no dia a dia

---

## 5. Requisitos Funcionais

### RF01 — Upload do Arquivo
- [ ] Permitir upload apenas de arquivos `.csv`.  
- [ ] Exibir erro quando o arquivo for inválido.  
- [ ] Validar existência do arquivo antes do processamento.

### RF02 — Leitura e Processamento
- [ ] Ler o CSV enviado pelo usuário.  
- [ ] Detectar automaticamente os nomes das colunas.  
- [ ] Tratar delimitadores comuns (`,`, `;`, `\t`).  

### RF03 — Seleção de Colunas
- [ ] Exibir ao usuário a lista de todas as colunas detectadas.  
- [ ] Permitir selecionar/desmarcar colunas.  
- [ ] Validar que ao menos uma coluna seja selecionada.  

### RF04 — Geração do CSV Final
- [ ] Processar e gerar um novo CSV somente com as colunas selecionadas.  
- [ ] Nomear o arquivo como `<nome_original>_filtrado.csv`.  
- [ ] Disponibilizar o arquivo final para download.  

### RF05 — Interface
- [ ] Utilizar Tailwind CSS (CDN ou build local conforme preferência).  
- [ ] Exibir feedback visual durante o processamento (loading / sucesso / erro).  
- [ ] Utilizar componentes reutilizáveis (header, footer, button).

---

## 6. Requisitos Não Funcionais

### RNF01 — Desempenho
- [ ] Processar CSVs de até **20 MB** de forma eficiente.  
- [ ] Carregar páginas em ~1 segundo (ambiente local razoável).

### RNF02 — Usabilidade
- [ ] Interface simples e direta.  
- [ ] Feedback claro ao usuário em caso de erro.

### RNF03 — Manutenibilidade
- [ ] Estrutura do projeto no formato *application package* (pacote Flask).  
- [ ] Separação entre rotas, serviços e templates.  
- [ ] Componentização no diretório `templates/components`.

### RNF04 — Segurança
- [ ] Não armazenar arquivos permanentemente no servidor.  
- [ ] Excluir temporários após o download ou após o fim da sessão.  
- [ ] Limitar tamanho máximo de upload por configuração.

---

## 7. Restrições
- Usar Python 3.14+ e Flask.  
- Tailwind CSS via CDN (ou build local, se preferir).  
- Projeto ideal para execução local / VPS simples (não exige infra cloud avançada na versão 1.0).

---

## 8. Fluxo Geral do Usuário
- [ ] Usuário acessa a página inicial.  
- [ ] Usuário faz upload do arquivo CSV.  
- [ ] Sistema detecta e exibe as colunas.  
- [ ] Usuário seleciona as colunas desejadas.  
- [ ] Usuário clica em **Gerar CSV**.  
- [ ] Sistema processa e inicia download do CSV filtrado.

---

## 9. Fluxo Técnico Interno
- [ ] Receber arquivo → salvar temporariamente em memória (não persistir em disco).  
- [ ] Ler CSV (pandas ou csv builtin) tratando separadores e encoding.  
- [ ] Listar colunas e renderizar seleção para o usuário.  
- [ ] Receber lista de colunas selecionadas.  
- [ ] Filtrar dataframe e aplicar transformações (se houver).  
- [ ] Gerar CSV resultante na memória e enviar como download.  
- [ ] Limpar quaisquer buffers/temporários.

---

## 10. Regras de Negócio
- [ ] Se existir coluna com nome (case-insensitive) `cpf trabalhador`, aplicar deduplicação por CPF.  
- [ ] Normalizar CPFs removendo caracteres não numéricos e preenchendo zeros à esquerda (11 dígitos).  
- [ ] Manter a ordem de colunas conforme seleção do usuário.  
- [ ] Não armazenar arquivos de usuários após o processo.

---

## 11. Critérios de Aceite
- [ ] Página inicial renderiza corretamente.  
- [ ] Upload aceita apenas CSVs válidos.  
- [ ] Colunas são listadas corretamente após upload.  
- [ ] Arquivo final contém apenas as colunas selecionadas e mantém integridade dos dados.  
- [ ] Download do CSV é acionado sem deixar cópia no servidor.  
- [ ] Layout é responsivo em desktop e mobile.

---

## 12. Checklist Geral do Projeto
- [ ] Criar estrutura base do projeto (pacote Flask).  
- [ ] Implementar Application Factory.  
- [ ] Implementar rotas: `/`, `/upload`, `/processar`.  
- [ ] Implementar serviço de processamento CSV (csv_service).  
- [ ] Criar templates: `base.html`, `index.html`, `select_columns.html`.  
- [ ] Criar components: `components/button.html`, `components/header.html`, `components/footer.html`.  
- [ ] Integrar Tailwind (CDN ou build).  
- [ ] Implementar JS modular (filePreview, columnSelector, downloadHelper).  
- [ ] Escrever README.md e docs básicos.  
- [ ] Subir projeto para GitHub e documentar issues/milestones.

---

## 13. Anexos / Observações
- Recomenda-se usar macros Jinja para componentes reutilizáveis (botão, header, footer).  
- Manter o build do Tailwind separado (npm) se for customizar estilos profundamente; para MVP, CDN é suficiente.  
- Em produção, configurar limites de upload e tempo de execução (worker / gunicorn).

---

**Fim do documento.**
