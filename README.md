# 💪 Sistema de Gerenciamento de Academia

Um sistema completo de gestão para academias desenvolvido em **Python**, focado em regras de negócio robustas no Back-end e uma interface gráfica interativa e moderna construída com **Streamlit**. O projeto utiliza persistência de dados local em arquivos `.txt` e aplica conceitos avançados de Programação Orientada a Objetos (POO).

## 🚀 Funcionalidades

O sistema é dividido em 4 módulos principais, todos contendo operações completas de CRUD (Criar, Ler, Atualizar, Excluir) e validações de regras de negócio:

*   **👨‍🏫 Gestão de Professores:** Cadastro de profissionais com validação de código único e atualização de dados de contato.
*   **🏋️‍♀️ Gestão de Alunos:** Controle de alunos com cálculo automático de IMC (Índice de Massa Corporal) baseado no peso e altura informados.
*   **🏅 Gestão de Modalidades:** Criação de aulas (ex: Musculação, Pilates), vinculação obrigatória a um professor responsável, definição de mensalidade e limite máximo de alunos por turma.
*   **📝 Gestão de Matrículas:** Sistema inteligente que vincula alunos às modalidades, validando automaticamente a disponibilidade de vagas (lotação) e restituindo a vaga em caso de cancelamento da matrícula.
*   **💰 Relatórios:** Cálculo em tempo real do faturamento bruto por modalidade, cruzando a quantidade de alunos matriculados com o valor da aula.

## 🏗️ Arquitetura do Projeto

O projeto foi desenhado utilizando o conceito de **Separação de Responsabilidades (Clean Architecture)**, isolando a interface, as regras de negócio e o armazenamento:

> GERENCIAMENTO-ACADEMIA/
> │
> ├── app.py                  # Frontend (Interface Gráfica com Streamlit)
> ├── model/                  # Entidades do Domínio (POO)
> │   └── entidades.py        # Classes: Aluno, Professor, Modalidade, Matricula
> ├── service/                # Regras de Negócio e Lógica de Aplicação
> │   ├── aluno_service.py
> │   ├── professor_service.py
> │   ├── modalidade_service.py
> │   └── matricula_service.py
> ├── storage/                # Persistência de Dados
> │   └── gerenciador_arquivos.py # Manipulação de arquivos .txt para cada entidade
> └── structure/              # Estruturas de Dados Customizadas
>     └── arvore_binaria.py

## 🛠️ Tecnologias Utilizadas

*   **Linguagem:** Python 3.x
*   **Frontend / UI:** Streamlit
*   **Armazenamento:** Arquivos de Texto (`.txt`)
*   **Paradigma:** Programação Orientada a Objetos (POO)

## ⚙️ Como Executar o Projeto

1.  Certifique-se de ter o [Python](https://www.python.org/) instalado em sua máquina.
2.  Clone este repositório ou faça o download dos arquivos.
3.  Abra o terminal na pasta raiz do projeto (`GERENCIAMENTO-ACADEMIA`).
4.  Instale a biblioteca do Streamlit executando o comando:
    `pip install streamlit`
5.  Inicie a aplicação com o comando:
    `streamlit run app.py`
6.  O sistema será aberto automaticamente no seu navegador padrão (geralmente no endereço `http://localhost:8501`).


*Focado em desenvolvimento Back-end, POO e Arquitetura de Software.*
