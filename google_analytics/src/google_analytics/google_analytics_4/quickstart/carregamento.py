from __future__ import annotations

import pandas as pd
from sqlalchemy import delete
from sqlalchemy.orm import Session

from google_analytics.bd import tabelas
from google_analytics.loggers import logger
from google_analytics.utilitarios.bd import carregar_dataframe


def deletar_dados(sessao: Session, tabela_destino: str) -> int:

    tabela_usuarios_acessos_ga4 = tabelas[tabela_destino]
    limpar = delete(tabela_usuarios_acessos_ga4)
    logger.debug(limpar)
    sessao.execute(limpar)

    return 0


def carregar_dados(sessao: Session, df_tratado: pd.DataFrame, tabela_destino: str) -> int:

    logger.info("Carregando dados em tabela...")

    deletar_dados(sessao=sessao, tabela_destino=tabela_destino)

    carregar_dataframe(sessao=sessao, df=df_tratado, tabela_destino=tabela_destino)

    logger.info(
        "Carregamento concluído para a tabela `{tabela_nome}`: " + "adicionadas {linhas_adicionadas} novas linhas.",
        tabela_nome=tabela_destino,
        linhas_adicionadas=len(df_tratado),
    )

    return 0
