from __future__ import annotations

from datetime import datetime
from typing import Final

import pandas as pd
from frozendict import frozendict

IPGA4_COLUNAS: Final[dict[str, str]] = {
    "dateHour": "periodo_data_hora",
    "firstSessionDate": "periodo_data_primeira_sessao",
    "customUser:usuario_id_dimensao": "usuario_id",
    "customUser:usuario_mun_dimensao": "usuario_municipio",
    "customUser:usuario_equipe_dimensao": "usuario_equipe_ine",
    "customUser:usuario_cargo_dimensao": "usuario_cargo",
    "city": "cidade_acesso",
    "pagePath": "pagina_path",
    "activeUsers": "usuarios_ativos",
    "newUsers": "novos_usuarios",
    "eventCount": "eventos",
    "engagedSessions": "sessoes_engajadas",
    "engagementRate": "taxa_engajamento",
    "screenPageViews": "visualizacoes",
    "userEngagementDuration": "sessao_duracao",
    "averageSessionDuration": "sessao_duracao_media",
    "dauPerMau": "dau_per_mau",
    "dauPerWau": "dau_per_wau",
}

IPGA4_TIPOS: Final[frozendict] = frozendict(
    {
        "periodo_data_hora": str,
        "periodo_data_primeira_sessao": str,
        "usuario_id": str,
        "usuario_municipio": str,
        "usuario_equipe_ine": str,
        "usuario_cargo": str,
        "cidade_acesso": str,
        "pagina_path": str,
        "usuarios_ativos": int,
        "novos_usuarios": int,
        "eventos": int,
        "sessoes_engajadas": int,
        "taxa_engajamento": float,
        "visualizacoes": int,
        "sessao_duracao": int,
        "sessao_duracao_media": float,
        "dau_per_mau": float,
        "dau_per_mau": float,
    }
)


def transformar_dados(df_extraido: pd.DataFrame) -> pd.DataFrame:

    df_extraido["criacao_data"] = datetime.now()
    df_extraido["atualizacao_data"] = datetime.now()

    df_tratado = df_extraido.rename(columns=IPGA4_COLUNAS)
    df_tratado = df_tratado.astype(IPGA4_TIPOS)

    return df_tratado
