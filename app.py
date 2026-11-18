import os
import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title='Central Vanielle 2.5 | Demonstração', page_icon='💙', layout='wide')

# Acesso protegido: configure DEMO_USER e DEMO_PASSWORD nas variáveis de ambiente do host.
def login():
    st.markdown('<h1 style="color:#eaf2ff">💙 Central Vanielle 2.5</h1><p style="color:#9db2ce">Ambiente demonstrativo • Tokio Marine</p>', unsafe_allow_html=True)
    with st.form('login'):
        user = st.text_input('Usuário')
        password = st.text_input('Senha', type='password')
        ok = st.form_submit_button('Entrar', use_container_width=True)
    if ok:
        if user == os.getenv('DEMO_USER', 'tokio') and password == os.getenv('DEMO_PASSWORD', 'TROQUE-ESTA-SENHA'):
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error('Usuário ou senha inválidos.')

if not st.session_state.get('authenticated'):
    st.markdown('''<style>.stApp{background:linear-gradient(135deg,#061a33,#0b2c52)} [data-testid="stForm"]{background:#0b2c52;padding:24px;border:1px solid #17416e;border-radius:14px}</style>''', unsafe_allow_html=True)
    login(); st.stop()

st.markdown('''<style>
.stApp{background:#061a33;color:#f1f6ff}.block-container{padding-top:1.5rem}
[data-testid="stSidebar"]{background:#04152b}.stMetric{background:#0b2c52;padding:16px;border:1px solid #17416e;border-radius:12px}
[data-testid="stDataFrame"]{border:1px solid #17416e;border-radius:10px}
h1,h2,h3{color:#f1f6ff}
</style>''', unsafe_allow_html=True)

# Massa fictícia exclusiva para demonstração. Nenhum dado é importado do SQLite original.
data = pd.DataFrame([
 {'Seguradora':'Tokio Marine','Cliente':'Cliente Demonstração 01','Documento':'***.***.***-01','Telefone':'(51) 90000-0001','Apólice':'DEMO-1001','Produto':'Automóvel','Parcela':'03/10','Vencimento':'05/11/2026','Valor':420.50,'Status':'Inadimplente'},
 {'Seguradora':'Tokio Marine','Cliente':'Cliente Demonstração 02','Documento':'***.***.***-02','Telefone':'(51) 90000-0002','Apólice':'DEMO-1002','Produto':'Residencial','Parcela':'02/12','Vencimento':'10/11/2026','Valor':285.90,'Status':'Inadimplente'},
 {'Seguradora':'Tokio Marine','Cliente':'Cliente Demonstração 03','Documento':'***.***.***-03','Telefone':'(51) 90000-0003','Apólice':'DEMO-1003','Produto':'Empresarial','Parcela':'07/12','Vencimento':'15/11/2026','Valor':610.00,'Status':'Em aberto'},
 {'Seguradora':'Tokio Marine','Cliente':'Cliente Demonstração 04','Documento':'***.***.***-04','Telefone':'(51) 90000-0004','Apólice':'DEMO-1004','Produto':'Automóvel','Parcela':'01/10','Vencimento':'20/11/2026','Valor':198.75,'Status':'PAGO'},
 {'Seguradora':'Tokio Marine','Cliente':'Cliente Demonstração 05','Documento':'***.***.***-05','Telefone':'(51) 90000-0005','Apólice':'DEMO-1005','Produto':'Vida','Parcela':'04/12','Vencimento':'02/11/2026','Valor':155.00,'Status':'Inadimplente'},
])

st.sidebar.markdown('## 💙 Central Vanielle')
st.sidebar.caption('Versão demonstrativa 2.5')
page = st.sidebar.radio('Navegação', ['Dashboard','Inadimplentes','Clientes','Apólices','Parcelas','Histórico','Relatórios','Integração Tokio'])
st.sidebar.divider()
st.sidebar.success('Ambiente de demonstração')
if st.sidebar.button('Sair'):
    st.session_state.authenticated = False; st.rerun()

st.title(page)
st.caption('Dados inteiramente fictícios • Demonstração técnica • Não representa consulta em produção')

if page == 'Dashboard':
    overdue = data[data.Status == 'Inadimplente']
    a,b,c,d = st.columns(4)
    a.metric('Clientes', len(data)); b.metric('Apólices', data.Apólice.nunique()); c.metric('Parcelas inadimplentes', len(overdue)); d.metric('Valor em aberto', f"R$ {overdue.Valor.sum():,.2f}".replace(',','X').replace('.',',').replace('X','.'))
    st.subheader('Resumo demonstrativo por produto')
    st.bar_chart(data.groupby('Produto').Valor.sum())
    st.subheader('Últimos registros demonstrativos')
    st.dataframe(data, use_container_width=True, hide_index=True)
elif page == 'Inadimplentes':
    st.subheader('Parcelas em situação de inadimplência')
    st.dataframe(data[data.Status == 'Inadimplente'], use_container_width=True, hide_index=True)
elif page == 'Clientes':
    st.subheader('Base demonstrativa de clientes')
    st.dataframe(data[['Cliente','Documento','Telefone','Seguradora']], use_container_width=True, hide_index=True)
elif page == 'Apólices':
    st.subheader('Apólices demonstrativas')
    st.dataframe(data[['Cliente','Apólice','Produto','Seguradora']], use_container_width=True, hide_index=True)
elif page == 'Parcelas':
    st.subheader('Parcelas demonstrativas')
    st.dataframe(data[['Apólice','Parcela','Vencimento','Valor','Status']], use_container_width=True, hide_index=True)
elif page == 'Histórico':
    st.info('Histórico de demonstração: consulta simulada em 18/11/2026 • 5 registros fictícios apresentados.')
    st.dataframe(pd.DataFrame([{'Data':'18/11/2026 11:00','Origem':'Demonstração web','Registros':5,'Resultado':'Concluído'}]), use_container_width=True, hide_index=True)
elif page == 'Relatórios':
    st.subheader('Relatório demonstrativo')
    st.download_button('Baixar relatório CSV', data.to_csv(index=False).encode('utf-8-sig'), 'relatorio_demonstracao.csv', 'text/csv')
    st.dataframe(data.groupby('Status', as_index=False).Valor.sum(), use_container_width=True, hide_index=True)
elif page == 'Integração Tokio':
    st.subheader('Status da integração')
    st.warning('Ambiente demonstrativo: conexão com a API desativada. Aguardando credenciais e URL oficiais de produção.')
    x,y = st.columns(2); x.metric('Autenticação', 'Não executada'); y.metric('Consulta API', 'Não executada')
    st.info('A tela demonstra onde os resultados da integração serão apresentados. Nenhuma chamada externa é realizada nesta versão.')

st.divider()
st.caption('Central Vanielle 2.5 • Demonstração para avaliação técnica • Dados fictícios')
