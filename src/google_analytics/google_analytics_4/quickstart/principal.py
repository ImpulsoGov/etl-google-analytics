from __future__ import annotations

import os

from sqlalchemy.orm import Session

from google_analytics.google_analytics_4.quickstart.carregamento import carregar_dados
from google_analytics.google_analytics_4.quickstart.extracao import extrair_relatorio
from google_analytics.google_analytics_4.quickstart.tratamento import transformar_dados


def obter_relatorio_quickstart(sessao: Session, tabela_destino: str, variaveis: dict):
    df_extraido = extrair_relatorio(variaveis=variaveis)
    # df_extraido.to_parquet('IMPULSO_PREVINE_GA4_QUICKSTART.parquet',engine='pyarrow')
    df_tratado = transformar_dados(df_extraido=df_extraido)
    carregar_dados(sessao=sessao, df_tratado=df_tratado, tabela_destino=tabela_destino)
    os.remove("GA4-ImpulsoGov-Credenciais.json")
