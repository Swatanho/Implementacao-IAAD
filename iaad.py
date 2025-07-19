import streamlit as st
import os
import mysql.connector
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

conn = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="Bilombra250!",
    database="programaçõesdefilmes"
)

cursor = conn.cursor()

st.title("Sistema de Programação de Filmes")

tabelas = ["Filme", "Canal", "Exibicao", "Elenco"]
tabela = st.selectbox("Escolha a tabela:", tabelas)

if st.button(f"Visualizar {tabela}"):
    cursor.execute(f"SELECT * FROM {tabela}")
    dados = cursor.fetchall()
    colunas = [i[0] for i in cursor.description]
    df = pd.DataFrame(dados, columns=colunas)
    
    st.subheader(f"Dados da tabela {tabela}")
    st.dataframe(df, use_container_width=True)

st.divider()
st.subheader(f"CRUD - {tabela}")

if tabela == "Filme":
    aba = st.radio("Escolha a ação:", ["Inserir", "Atualizar", "Excluir"])
    
    if aba == "Inserir":
        with st.form("form_filme"):
            num = st.number_input("ID", step=1)
            nome = st.text_input("Nome")
            ano = st.number_input("Ano", step=1)
            duracao = st.number_input("Duração (min)", step=1)
            if st.form_submit_button("Inserir"):
                try:
                    cursor.execute(
                        "INSERT INTO Filme (num_filme, nome, ano, duracao) VALUES (%s, %s, %s, %s)",
                        (num, nome, ano, duracao)
                    )
                    conn.commit()
                    st.success("Filme inserido com sucesso!")
                except Exception as e:
                    st.error(f"Erro: {e}")

    elif aba == "Atualizar":
        with st.form("update_filme"):
            num = st.number_input("ID do Filme", step=1)
            nome = st.text_input("Novo Nome")
            ano = st.number_input("Novo Ano", step=1)
            duracao = st.number_input("Nova Duração", step=1)
            if st.form_submit_button("Atualizar"):
                cursor.execute("UPDATE Filme SET nome=%s, ano=%s, duracao=%s WHERE num_filme=%s",
                               (nome, ano, duracao, num))
                conn.commit()
                st.success("Filme atualizado com sucesso!")

    elif aba == "Excluir":
        with st.form("delete_filme"):
            num = st.number_input("ID do Filme", step=1)
            if st.form_submit_button("Excluir"):
                cursor.execute("DELETE FROM Filme WHERE num_filme = %s", (num,))
                conn.commit()
                st.success("Filme excluído com sucesso!")

elif tabela == "Canal":
    aba = st.radio("Escolha a ação:", ["Inserir", "Atualizar", "Excluir"])
    
    if aba == "Inserir":
        with st.form("form_canal"):
            num = st.number_input("Número do Canal", step=1)
            nome = st.text_input("Nome do Canal")
            if st.form_submit_button("Inserir"):
                cursor.execute("INSERT INTO Canal (num_canal, nome) VALUES (%s, %s)", (num, nome))
                conn.commit()
                st.success("Canal inserido com sucesso!")

    elif aba == "Atualizar":
        with st.form("update_canal"):
            num = st.number_input("Número do Canal", step=1)
            nome = st.text_input("Novo Nome")
            if st.form_submit_button("Atualizar"):
                cursor.execute("UPDATE Canal SET nome=%s WHERE num_canal=%s", (nome, num))
                conn.commit()
                st.success("Canal atualizado com sucesso!")

    elif aba == "Excluir":
        with st.form("delete_canal"):
            num = st.number_input("Número do Canal", step=1)
            if st.form_submit_button("Excluir"):
                cursor.execute("DELETE FROM Canal WHERE num_canal=%s", (num,))
                conn.commit()
                st.success("Canal excluído com sucesso!")

elif tabela == "Elenco":
    aba = st.radio("Escolha a ação:", ["Inserir", "Atualizar", "Excluir"])
    
    if aba == "Inserir":
        with st.form("form_elenco"):
            num_filme = st.number_input("Número do Filme", step=1)
            nome_ator = st.text_input("Nome do Ator")
            protagonista = st.checkbox("Protagonista?")
            if st.form_submit_button("Inserir"):
                cursor.execute(
                    "INSERT INTO Elenco (num_filme, nome_ator, protagonista) VALUES (%s, %s, %s)",
                    (num_filme, nome_ator, protagonista)
                )
                conn.commit()
                st.success("Ator inserido no elenco com sucesso!")

    elif aba == "Atualizar":
        with st.form("update_elenco"):
            id_elenco = st.number_input("ID do Elenco", step=1)
            nome_ator = st.text_input("Novo nome do ator")
            protagonista = st.checkbox("É protagonista?")
            if st.form_submit_button("Atualizar"):
                cursor.execute(
                    "UPDATE Elenco SET nome_ator=%s, protagonista=%s WHERE id_elenco=%s",
                    (nome_ator, protagonista, id_elenco)
                )
                conn.commit()
                st.success("Elenco atualizado!")

    elif aba == "Excluir":
        with st.form("delete_elenco"):
            id_elenco = st.number_input("ID do Elenco", step=1)
            if st.form_submit_button("Excluir"):
                cursor.execute("DELETE FROM Elenco WHERE id_elenco=%s", (id_elenco,))
                conn.commit()
                st.success("Registro excluído do elenco!")

elif tabela == "Exibicao":
    aba = st.radio("Escolha a ação:", ["Inserir", "Excluir"])

    if aba == "Inserir":
        with st.form("form_exibicao"):
            num_filme = st.number_input("Número do Filme", step=1)
            num_canal = st.number_input("Número do Canal", step=1)
            data = st.date_input("Data da Exibição")
            hora = st.time_input("Hora da Exibição")
            if st.form_submit_button("Inserir"):
                try:
                    cursor.execute(
                        "INSERT INTO Exibicao (num_filme, num_canal, data_exibicao, hora_exibicao) VALUES (%s, %s, %s, %s)",
                        (num_filme, num_canal, data, hora)
                    )
                    conn.commit()
                    st.success("Exibição adicionada!")
                except Exception as e:
                    st.error(f"Erro: {e}")

    elif aba == "Excluir":
        with st.form("delete_exibicao"):
            id_exibicao = st.number_input("ID da Exibição", step=1)
            if st.form_submit_button("Excluir"):
                cursor.execute("DELETE FROM Exibicao WHERE id_exibicao=%s", (id_exibicao,))
                conn.commit()
                st.success("Exibição excluída!")

# criação de trigger para impedir que haja conflito de horários de exibição

st.header("Criar trigger: impedir conflito de horário em Exibicao")

if st.button("Criar trigger chk_exibicao_no_overlap"):
    try:
        cursor.execute("DROP TRIGGER IF EXISTS chk_exibicao_no_overlap")
        conn.commit()
        trigger_sql = """
        CREATE TRIGGER chk_exibicao_no_overlap
        BEFORE INSERT ON Exibicao
        FOR EACH ROW
        BEGIN
          IF EXISTS (
            SELECT 1 FROM Exibicao
            WHERE num_canal = NEW.num_canal
              AND data_exibicao = NEW.data_exibicao
              AND hora_exibicao = NEW.hora_exibicao
          ) THEN
            SIGNAL SQLSTATE '45000'
              SET MESSAGE_TEXT = 'Conflito: horário já ocupado neste canal';
          END IF;
        END
        """
        cursor.execute(trigger_sql)
        conn.commit()
        st.success("Trigger criada com sucesso!")
    except mysql.connector.Error as e:
        st.error(f"Erro ao criar trigger: {e}")

cursor.close()
conn.close()

