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
st.image
opcao = st.sidebar.selectbox("Escolha uma área:", ["Alunos", "Professores", "Modalidades", "Faturamento"])

# TELA DE PROFESSORES
if opcao == "Professores":
    st.header("Gestão de Professores")
    
    aba_listar, aba_cadastrar  = st.tabs(["Lista de Professores", "Cadastrar Novo"])
    
                 
    with aba_listar:
        try:
            professores = servico_prof.listar_professores()
            for p in professores:
                
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
                        
                        st.divider() # Cria uma linha sutil de separação
                        st.markdown("##### ⚙️ Atualizar Dados")
                        
                        col_form1, col_form2 = st.columns(2)
                        with col_form1:
                            novo_nome = st.text_input("Nome", value=p.nome, key=f"upd_nome_{p.codigo_prof}")
                            novo_tel = st.text_input("Telefone", value=p.telefone, key=f"upd_tel_{p.codigo_prof}")
                        with col_form2:
                            novo_end = st.text_input("Endereço", value=p.endereco, key=f"upd_end_{p.codigo_prof}")
                            
                        # Botões do formulário de edição
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
            telefone = st.text_input("Telefone")
            
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
                alunos = servico_aluno.listar_alunos()
                for a in alunos:
                    
                    with st.expander(f"👤 #{a.codigo_aluno} — **{a.nome}**"):
                        
                        col_info, col_botoes = st.columns([3, 1])
                        
                        with col_info:
                            st.markdown(f"**Data de Nascimento:** `{a.data_nascimento}`")
                            st.markdown(f"**Peso:** {a.peso}")
                            st.markdown(f"**Altura:** {a.altura}")
                            st.markdown(f"**IMC:** {a.classificacao_imc}")
                            
                        with col_botoes:
                            # CORREÇÃO: Usando 'a.codigo_aluno'
                            btn_editar = st.button("✏️ Editar", key=f"btn_edit_{a.codigo_aluno}", use_container_width=True)
                            if st.button("🗑️ Excluir", key=f"btn_del_{a.codigo_aluno}", type="primary", use_container_width=True):
                                # CORREÇÃO: Usando 'servico_aluno'
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

# TELA DE MODALIDADES (Molde inicial)
elif opcao == "Modalidades":
    st.header("Gestão de Modalidades")
    aba_listar, aba_cadastrar = st.tabs(["Lista de Modalidades", "Cadastrar Novo"])
    
    


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