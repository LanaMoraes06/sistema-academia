import streamlit as st

from storage.gerenciador_arquivos import GerenciadorProfessor, GerenciadorModalidade, GerenciadorMatricula
from service.professor_service import ProfessorService
from service.modalidade_service import ModalidadeService
from storage.gerenciador_arquivos import GerenciadorAlunos
from service.aluno_service import AlunoService
from service.matricula_service import MatriculaService

gen_aluno = GerenciadorAlunos()
gen_prof = GerenciadorProfessor()
gen_mod = GerenciadorModalidade()
gen_mat = GerenciadorMatricula()

servico_aluno = AlunoService(gen_aluno)
servico_prof = ProfessorService(gen_prof)
servico_mod = ModalidadeService(gen_mod, gen_prof, gen_mat)

st.set_page_config(page_title="Sistema de Academia", page_icon="💪")
st.sidebar.title("FitFema")
opcao = st.sidebar.selectbox("Escolha uma área:", ["Alunos", "Professores", "Modalidades", "Faturamento"])

# TELA DE PROFESSORES
if opcao == "Professores":
    st.header("Gestão de Professores")
    
    aba_listar, aba_cadastrar  = st.tabs(["Lista de Professores", "Cadastrar Novo"])
    
                 
    with aba_listar:
        try:
            
            pesquisa = st.text_input("", placeholder="Digite o código do professor")
            professor = servico_prof.listar_professores()           
            if pesquisa:
                try:
                    codigo_busca = int(pesquisa)
                    professor = [p for p in professor if int(p.codigo_prof) == codigo_busca]
                except ValueError:
                    st.warning("⚠️ Digite apenas números para pesquisar pelo código.")
                    professor = []
            if not professor and pesquisa:
                st.info(f"Nenhum professor encontrado com o código {pesquisa}.")
            for p in professor:
                
                with st.expander(f"👤 #{p.codigo_prof} — **{p.nome}**"):
                    
                    col_info, col_botoes = st.columns([3, 1])
                    
                    with col_info:
                        st.markdown(f"**📞 Telefone:** `{p.telefone}`")
                        st.markdown(f"**📍 Endereço:** {p.endereco}")
                        
                    with col_botoes:
                        btn_editar = st.button("✏️ Editar", key=f"btn_edit_{p.codigo_prof}", use_container_width=True)
                        if st.button("🗑️ Excluir", key=f"btn_del_{p.codigo_prof}", type="primary", use_container_width=True):
                            servico_prof.excluir(p.codigo_prof)
                            st.rerun()

                    if btn_editar or st.session_state.get(f"editando_{p.codigo_prof}", False):
                        st.session_state[f"editando_{p.codigo_prof}"] = True 
                        
                        st.divider() 
                        st.markdown("#####  Atualizar Dados")
                        
                        col_form1, col_form2 = st.columns(2)
                        with col_form1:
                            novo_nome = st.text_input("Nome", value=p.nome, key=f"upd_nome_{p.codigo_prof}")
                            novo_tel = st.text_input("Telefone", value=p.telefone, key=f"upd_tel_{p.codigo_prof}")
                        with col_form2:
                            novo_end = st.text_input("Endereço", value=p.endereco, key=f"upd_end_{p.codigo_prof}")
                            
                        
                        c_salvar, c_cancelar, _ = st.columns([2, 2, 6])
                        if c_salvar.button("✔️ Salvar", type="secondary", key=f"save_{p.codigo_prof}", use_container_width=True):
                            servico_prof.atualizar(p.codigo_prof, novo_nome, novo_end, novo_tel)
                            st.session_state[f"editando_{p.codigo_prof}"] = False
                            st.rerun()
                            
                        if c_cancelar.button("❌ Cancelar", key=f"cancel_{p.codigo_prof}", use_container_width=True):
                            st.session_state[f"editando_{p.codigo_prof}"] = False
                            st.rerun()

        except ValueError as erro:
            st.warning(str(erro))

    with aba_cadastrar:
        with st.form("form_prof", clear_on_submit=True):
            codigo = st.number_input("Código do Professor", min_value=1, step=1)
            nome = st.text_input("Nome")
            endereco = st.text_input("Endereço")
            telefone = st.text_input("Telefone", max_chars=11)
            
            btn_salvar = st.form_submit_button("Salvar Professor")
            
            if btn_salvar:
                try:
                    servico_prof.cadastrar_professor(codigo, nome, endereco, telefone)
                    st.success(f"Professor {nome} cadastrado com sucesso!")
                except ValueError as erro:
                    st.error(str(erro))

#TELA ALUNOS
elif opcao == "Alunos":
    st.header("Gestão de Alunos")
    
    aba_listar, aba_cadastrar = st.tabs(["Lista de Alunos", "Cadastrar Novo"])
    
    with aba_cadastrar:
        with st.form("form_prof", clear_on_submit=True):
            codigo = st.number_input("Código do Aluno", min_value=1, step=1)
            nome = st.text_input("Nome")
            data_nascimento = st.date_input("Data de Nascimento")
            peso = st.number_input("Peso (kg)", min_value=0.0, step=0.1, format="%.1f")
            altura = st.number_input("Altura (metros - ex: 1.75)", min_value=0.0, step=0.01, format="%.2f")
            
            
            btn_salvar = st.form_submit_button("Salvar Aluno")
            
            if btn_salvar:
                try:
                    servico_aluno.cadastrar_aluno(codigo, nome, data_nascimento, peso, altura)
                    st.success(f"Aluno(a) {nome} cadastrado com sucesso!")
                except ValueError as erro:
                    st.error(str(erro))
                    
    with aba_listar:
            try:
                pesquisa = st.text_input("", placeholder="Digite o código do aluno")
                alunos = servico_aluno.listar_alunos()            
                if pesquisa:
                    try:
                        codigo_busca = int(pesquisa)
                        alunos = [a for a in alunos if int(a.codigo_aluno) == codigo_busca]
                    except ValueError:
                        st.warning("⚠️ Digite apenas números para pesquisar pelo código.")
                        alunos = []

                if not alunos and pesquisa:
                    st.info(f"Nenhum aluno encontrado com o código {pesquisa}.")
                for a in alunos:
                    
                    with st.expander(f"👤 #{a.codigo_aluno} — **{a.nome}**"):
                        
                        col_info, col_botoes = st.columns([3, 1])
                        
                        with col_info:
                            st.markdown(f"**Data de Nascimento:** `{a.data_nascimento}`")
                            st.markdown(f"**Peso:** {a.peso}")
                            st.markdown(f"**Altura:** {a.altura}")
                            st.markdown(f"**IMC:** {a.classificacao_imc}")
                            
                        with col_botoes:
                            btn_editar = st.button("✏️ Editar", key=f"btn_edit_{a.codigo_aluno}", use_container_width=True)
                            if st.button("🗑️ Excluir", key=f"btn_del_{a.codigo_aluno}", type="primary", use_container_width=True):
                                servico_aluno.excluir(a.codigo_aluno)
                                st.rerun()
    
                        if btn_editar or st.session_state.get(f"editando_{a.codigo_aluno}", False):
                            st.session_state[f"editando_{a.codigo_aluno}"] = True 
                            
                            st.divider()
                            st.markdown("##### Atualizar Dados")
                            
                            col_form1, col_form2 = st.columns(2)
                            with col_form1:
                                novo_nome = st.text_input("Nome", value=a.nome, key=f"upd_nome_{a.codigo_aluno}")
                                novo_peso = st.number_input("Peso (kg)", value=float(a.peso), key=f"upd_peso_{a.codigo_aluno}", format="%.1f")
                            with col_form2:
                                nova_altura = st.number_input("Altura (m)", value=float(a.altura), key=f"upd_altura_{a.codigo_aluno}", format="%.2f")
                            
                            c_salvar, c_cancelar, _ = st.columns([2, 2, 6])
                            if c_salvar.button("✔️ Salvar", type="secondary", key=f"save_{a.codigo_aluno}", use_container_width=True):
                            
                                servico_aluno.atualizar(a.codigo_aluno, novo_nome, novo_peso, nova_altura)
                                st.session_state[f"editando_{a.codigo_aluno}"] = False
                                st.rerun()
                                
                            if c_cancelar.button("❌ Cancelar", key=f"cancel_{a.codigo_aluno}", use_container_width=True):
                                st.session_state[f"editando_{a.codigo_aluno}"] = False
                                st.rerun()
    
            except ValueError as erro:
                st.warning(str(erro))

# TELA DE MODALIDADES 
elif opcao == "Modalidades":
    st.header("Gestão de Modalidades")
    
    aba_listar, aba_cadastrar = st.tabs(["Lista de Modalidades", "Cadastrar Nova"])
    
    with aba_listar:
        pesquisa = st.text_input("", placeholder="Ex: 1", key="pesq_mod")
        
        try:
            modalidades = servico_mod.listar_modalidade()
            
            if pesquisa:
                try:
                    codigo_busca = int(pesquisa)
                    modalidades = [m for m in modalidades if int(m.codigo_modalidade) == codigo_busca]
                except ValueError:
                    st.warning("⚠️ Digite apenas números para pesquisar pelo código.")
                    modalidades = []

            if not modalidades and pesquisa:
                st.info(f"Nenhuma modalidade encontrada com o código {pesquisa}.")

            for m in modalidades:
                with st.expander(f" #{m.codigo_modalidade} — **{m.descricao}**"):
                    col_info, col_botoes = st.columns([3, 1])
                    
                    with col_info:
                        try:
                            prof = servico_prof.buscar_cod(m.codigo_prof)
                            nome_exibicao = prof.nome
                        except:
                            nome_exibicao = f"Código {m.codigo_prof}"

                        st.markdown(f"**Professor Responsável:** {nome_exibicao}")
                        st.markdown(f"**Valor da Aula:** R$ {float(m.valor_aula):.2f}")
                        st.markdown(f"**Ocupação:** {m.total_alunos} de {m.limite_alunos} alunos")
                        
                    with col_botoes:
                        btn_editar = st.button("✏️ Editar", key=f"btn_edit_mod_{m.codigo_modalidade}", use_container_width=True)
                        if st.button("🗑️ Excluir", key=f"btn_del_mod_{m.codigo_modalidade}", type="primary", use_container_width=True):
                            servico_mod.excluir(m.codigo_modalidade)
                            st.rerun()

                    # Formulário de Edição
                    if btn_editar or st.session_state.get(f"editando_mod_{m.codigo_modalidade}", False):
                        st.session_state[f"editando_mod_{m.codigo_modalidade}"] = True 
                        
                        st.divider()
                        st.markdown("##### Atualizar Dados da Modalidade")
                        
                        col_f1, col_f2 = st.columns(2)
                        with col_f1:
                            nova_desc = st.text_input("Descrição", value=m.descricao, key=f"upd_desc_{m.codigo_modalidade}")
                            novo_prof = st.number_input("Código do Professor", value=int(m.codigo_prof), step=1, key=f"upd_prof_{m.codigo_modalidade}")
                        with col_f2:
                            novo_valor = st.number_input("Valor (R$)", value=float(m.valor_aula), min_value=0.0, format="%.2f", key=f"upd_val_{m.codigo_modalidade}")
                            novo_limite = st.number_input("Limite de Alunos", value=int(m.limite_alunos), min_value=1, step=1, key=f"upd_lim_{m.codigo_modalidade}")
                        
                        c_salvar, c_cancelar, _ = st.columns([2, 2, 6])
                        if c_salvar.button("✔️ Salvar", type="secondary", key=f"save_mod_{m.codigo_modalidade}", use_container_width=True):
                            # Nota: Passamos o m.total_alunos original para não perder a contagem de quem já está matriculado!
                            servico_mod.atualizar(m.codigo_modalidade, nova_desc, novo_prof, novo_valor, novo_limite, m.total_alunos)
                            st.session_state[f"editando_mod_{m.codigo_modalidade}"] = False
                            st.rerun()
                            st.rerun()

        except ValueError as erro:
            st.warning(str(erro))

    with aba_cadastrar:
        st.markdown("#### Vincular Professor")
        cod_prof = st.number_input("Digite o Código do Professor responsável:", min_value=0, step=1, key="cad_mod_prof")
        
        if cod_prof > 0:
            try:
                prof = servico_prof.buscar_cod(cod_prof)
                st.success(f"Professor responsável: **{prof.nome}**")
                
                with st.form("form_modalidade", clear_on_submit=True):
                    st.markdown("#### Dados da Modalidade")
                    
                    codigo = st.number_input("Código da Modalidade", min_value=1, step=1)
                    descricao = st.text_input("Descrição (Ex: Musculação, Pilates)")
                    
                    c1, c2 = st.columns(2)
                    with c1:
                        valor = st.number_input("Valor da Aula (R$)", min_value=0.0, step=10.0, format="%.2f")
                    with c2:
                        limite = st.number_input("Limite Máximo de Alunos", min_value=1, step=1)
                    
                    btn_salvar = st.form_submit_button("Salvar Modalidade")
                    
                    if btn_salvar:
                        try:
                            servico_mod.cadastrar_modalidade(codigo, descricao, cod_prof, valor, limite, total_alunos=0)
                            st.success(f"A modalidade {descricao} foi cadastrada com sucesso!")
                        except ValueError as erro:
                            st.error(str(erro))
                            
            except ValueError:
                st.warning("⚠️ Não encontramos nenhum professor com este código. Por favor, verifique.")
    


# TELA DE FATURAMENTO                                

elif opcao == "Faturamento":
    st.header("Relatório de Faturamento por Modalidade")
    
    with st.form("form_faturamento"):
        cod_mod = st.number_input("Digite o Código da Modalidade", min_value=1, step=1)
        btn_calcular = st.form_submit_button("Calcular Faturamento")
        
        if btn_calcular:
            try:

                descricao, nome_prof, total = servico_mod.calcular_faturamento(cod_mod)
                
                st.success("Cálculo realizado com sucesso!")
                
                col1, col2, col3 = st.columns(3)
                col1.metric("Modalidade", descricao)
                col2.metric("Professor", nome_prof)
                col3.metric("Total Faturado", f"R$ {total:.2f}")
                
            except ValueError as erro:
                st.error(str(erro))