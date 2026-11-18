
import os
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Central Vanielle 2.5 | Demonstração",
    page_icon="💙",
    layout="wide"
)

# =====================================================
# CONFIGURAÇÃO DE ACESSO
# =====================================================

def obter_segredo(chave, padrao):
    try:
        return st.secrets.get(chave, os.getenv(chave, padrao))
    except Exception:
        return os.getenv(chave, padrao)


def login():
    st.markdown("""
        <div style="text-align:center; padding:35px 0 20px;">
            <h1 style="color:white;">💙 Central Vanielle 2.5</h1>
            <p style="color:#d7e5f5;">Ambiente demonstrativo • Tokio Marine</p>
        </div>
    """, unsafe_allow_html=True)

    with st.form("login"):
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        entrar = st.form_submit_button("Entrar", use_container_width=True)

    if entrar:
        usuario_correto = obter_segredo("DEMO_USER", "tokio")
        senha_correta = obter_segredo("DEMO_PASSWORD", "TROQUE-ESTA-SENHA")

        if usuario == usuario_correto and senha == senha_correta:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Usuário ou senha inválidos.")


if not st.session_state.get("authenticated", False):
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg,#061a33,#123b65);
        }
        [data-testid="stForm"] {
            background: white;
            padding: 28px;
            border-radius: 15px;
            border: 1px solid #d8e3ef;
        }
        [data-testid="stForm"] label,
        [data-testid="stForm"] p {
            color: #172b45 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    login()
    st.stop()


# =====================================================
# IDENTIDADE VISUAL E CONTRASTE
# =====================================================

st.markdown("""
<style>

/* FUNDO PRINCIPAL */
.stApp {
    background: #eef3f9;
    color: #172b45;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* TEXTOS */
h1, h2, h3, h4, p, label {
    color: #172b45 !important;
}

/* MENU LATERAL */
[data-testid="stSidebar"] {
    background: #061a33;
}

[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #dce8f5 !important;
}

/* CARTÕES */
.metric-card {
    background: #ffffff;
    border: 1px solid #d7e1ed;
    border-left: 5px solid #1264a3;
    border-radius: 12px;
    padding: 20px;
    min-height: 115px;
    box-shadow: 0 2px 8px rgba(10,35,65,0.06);
}

.metric-label {
    color: #52657d !important;
    font-size: 14px;
    font-weight: 600;
}

.metric-value {
    color: #102b49 !important;
    font-size: 28px;
    font-weight: 800;
    margin-top: 8px;
}

/* TABELAS */
[data-testid="stDataFrame"] {
    background: #ffffff;
    border: 1px solid #d7e1ed;
    border-radius: 10px;
}

/* GRÁFICOS */
[data-testid="stVegaLiteChart"],
[data-testid="stArrowVegaLiteChart"] {
    background: #ffffff;
    border: 1px solid #d7e1ed;
    border-radius: 10px;
    padding: 12px;
}

/* CAMPOS */
input, textarea {
    color: #172b45 !important;
    background: #ffffff !important;
}

/* BOTÕES */
.stButton button,
.stDownloadButton button,
.stFormSubmitButton button {
    background: #1264a3;
    color: #ffffff !important;
    border: none;
    border-radius: 8px;
    font-weight: 600;
}

.stButton button:hover,
.stDownloadButton button:hover {
    background: #0b4778;
    color: #ffffff !important;
}

/* AVISOS */
[data-testid="stAlert"] {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# BASE FICTÍCIA DA DEMONSTRAÇÃO
# =====================================================

data = pd.DataFrame([
    {
        "Seguradora": "Tokio Marine",
        "Cliente": "Cliente Demonstração 01",
        "Documento": "***.***.***-01",
        "Telefone": "(51) 90000-0001",
        "Apólice": "DEMO-1001",
        "Produto": "Automóvel",
        "Parcela": "03/10",
        "Vencimento": "05/11/2026",
        "Valor": 420.50,
        "Status": "Inadimplente"
    },
    {
        "Seguradora": "Tokio Marine",
        "Cliente": "Cliente Demonstração 02",
        "Documento": "***.***.***-02",
        "Telefone": "(51) 90000-0002",
        "Apólice": "DEMO-1002",
        "Produto": "Residencial",
        "Parcela": "02/12",
        "Vencimento": "10/11/2026",
        "Valor": 285.90,
        "Status": "Inadimplente"
    },
    {
        "Seguradora": "Tokio Marine",
        "Cliente": "Cliente Demonstração 03",
        "Documento": "***.***.***-03",
        "Telefone": "(51) 90000-0003",
        "Apólice": "DEMO-1003",
        "Produto": "Empresarial",
        "Parcela": "07/12",
        "Vencimento": "15/11/2026",
        "Valor": 610.00,
        "Status": "Em aberto"
    },
    {
        "Seguradora": "Tokio Marine",
        "Cliente": "Cliente Demonstração 04",
        "Documento": "***.***.***-04",
        "Telefone": "(51) 90000-0004",
        "Apólice": "DEMO-1004",
        "Produto": "Automóvel",
        "Parcela": "01/10",
        "Vencimento": "20/11/2026",
        "Valor": 198.75,
        "Status": "PAGO"
    },
    {
        "Seguradora": "Tokio Marine",
        "Cliente": "Cliente Demonstração 05",
        "Documento": "***.***.***-05",
        "Telefone": "(51) 90000-0005",
        "Apólice": "DEMO-1005",
        "Produto": "Vida",
        "Parcela": "04/12",
        "Vencimento": "02/11/2026",
        "Valor": 155.00,
        "Status": "Inadimplente"
    }
])


def moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def cartao(titulo, valor):
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">{titulo}</div>
            <div class="metric-value">{valor}</div>
        </div>
    """, unsafe_allow_html=True)


# =====================================================
# NAVEGAÇÃO
# =====================================================

st.sidebar.markdown("## 💙 Central Vanielle")
st.sidebar.caption("Versão demonstrativa 2.5")

pagina = st.sidebar.radio(
    "Navegação",
    [
        "Dashboard",
        "Inadimplentes",
        "Clientes",
        "Apólices",
        "Parcelas",
        "Histórico",
        "Relatórios",
        "Integração Tokio"
    ]
)

st.sidebar.divider()
st.sidebar.success("Ambiente de demonstração")

if st.sidebar.button("Sair"):
    st.session_state.authenticated = False
    st.rerun()


# =====================================================
# CABEÇALHO DAS TELAS
# =====================================================

st.title(pagina)
st.caption(
    "Dados inteiramente fictícios • Demonstração técnica • "
    "Não representa consulta em produção"
)


# =====================================================
# DASHBOARD
# =====================================================

if pagina == "Dashboard":

    inadimplentes = data[data["Status"] == "Inadimplente"]

    a, b, c, d = st.columns(4)

    with a:
        cartao("Clientes", str(len(data)))

    with b:
        cartao("Apólices", str(data["Apólice"].nunique()))

    with c:
        cartao("Parcelas inadimplentes", str(len(inadimplentes)))

    with d:
        cartao("Valor em aberto", moeda(inadimplentes["Valor"].sum()))

    st.markdown("### Resumo demonstrativo por produto")

    resumo = data.groupby("Produto")["Valor"].sum()
    st.bar_chart(resumo)

    st.markdown("### Últimos registros demonstrativos")
    st.dataframe(data, use_container_width=True, hide_index=True)


# =====================================================
# INADIMPLENTES
# =====================================================

elif pagina == "Inadimplentes":

    st.subheader("Parcelas em situação de inadimplência")

    resultado = data[data["Status"] == "Inadimplente"]

    x, y = st.columns(2)
    x.metric("Quantidade de parcelas", len(resultado))
    y.metric("Total em aberto", moeda(resultado["Valor"].sum()))

    st.dataframe(resultado, use_container_width=True, hide_index=True)


# =====================================================
# CLIENTES
# =====================================================

elif pagina == "Clientes":

    st.subheader("Base demonstrativa de clientes")

    st.dataframe(
        data[["Cliente", "Documento", "Telefone", "Seguradora"]],
        use_container_width=True,
        hide_index=True
    )


# =====================================================
# APÓLICES
# =====================================================

elif pagina == "Apólices":

    st.subheader("Apólices demonstrativas")

    st.dataframe(
        data[["Cliente", "Apólice", "Produto", "Seguradora"]],
        use_container_width=True,
        hide_index=True
    )


# =====================================================
# PARCELAS
# =====================================================

elif pagina == "Parcelas":

    st.subheader("Parcelas demonstrativas")

    st.dataframe(
        data[["Apólice", "Parcela", "Vencimento", "Valor", "Status"]],
        use_container_width=True,
        hide_index=True
    )


# =====================================================
# HISTÓRICO
# =====================================================

elif pagina == "Histórico":

    st.subheader("Histórico de consultas")

    st.info(
        "Histórico demonstrativo: consulta simulada em 18/11/2026."
    )

    historico = pd.DataFrame([
        {
            "Data": "18/11/2026 11:00",
            "Origem": "Demonstração web",
            "Registros": 5,
            "Resultado": "Concluído"
        }
    ])

    st.dataframe(historico, use_container_width=True, hide_index=True)


# =====================================================
# RELATÓRIOS
# =====================================================

elif pagina == "Relatórios":

    st.subheader("Relatório demonstrativo")

    csv = data.to_csv(index=False).encode("utf-8-sig")

    st.download_button(
        "📥 Baixar relatório CSV",
        data=csv,
        file_name="relatorio_demonstracao.csv",
        mime="text/csv"
    )

    resumo = data.groupby("Status", as_index=False)["Valor"].sum()

    st.dataframe(resumo, use_container_width=True, hide_index=True)


# =====================================================
# INTEGRAÇÃO TOKIO
# =====================================================

elif pagina == "Integração Tokio":

    st.subheader("Status da integração")

    st.warning(
        "Ambiente demonstrativo: conexão com a API desativada. "
        "Aguardando credenciais e URL oficiais de produção."
    )

    x, y = st.columns(2)

    x.metric("Autenticação", "Não executada")
    y.metric("Consulta API", "Não executada")

    st.info(
        "Esta tela demonstra onde os resultados da integração "
        "serão apresentados. Nenhuma chamada externa é realizada."
    )


# =====================================================
# RODAPÉ
# =====================================================

st.divider()

st.caption(
    "Central Vanielle 2.5 • Demonstração para avaliação técnica • "
    "Dados fictícios"
)
