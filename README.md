# Central Vanielle 2.5 — demonstração web

Versão web demonstrativa independente da aplicação Windows. Usa exclusivamente dados fictícios em memória; não lê o SQLite original e não chama a API Tokio.

## Publicação rápida no Streamlit Community Cloud
1. Crie um repositório GitHub privado ou público e envie `app.py` e `requirements.txt`.
2. Em https://share.streamlit.io/ conecte o GitHub e selecione o repositório, branch e `app.py`.
3. Em App settings / Secrets, configure:

```toml
DEMO_USER = "tokio"
DEMO_PASSWORD = "defina-uma-senha-forte-aqui"
```

4. Publique e compartilhe a URL somente com o avaliador.

## Segurança obrigatória antes de compartilhar
- Troque a senha padrão; não use `TROQUE-ESTA-SENHA`.
- Restrinja o acesso ao avaliador e não publique dados reais.
- Esta versão é demonstrativa, não é a versão operacional da Vanielle.
