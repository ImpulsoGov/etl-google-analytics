from __future__ import annotations

import os

import jsonio
import pandas as pd
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)


def credenciais_api_ga4(variaveis: dict):
    " Credenciais do Google Analytics"
    for credenciais_dicionario in variaveis["credenciais_api"]:
        with open("GA4-ImpulsoGov-Credenciais.json", "w") as jsonfile:
            jsonio.dump(credenciais_dicionario, jsonfile)
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "GA4-ImpulsoGov-Credenciais.json"
            # credentials = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]


def extrair_dicionario_dimensoes(variaveis: dict) -> dict:
    for dimensoes_dicionario in variaveis["dimensoes"]:
        return dimensoes_dicionario


def extrair_dicionario_metricas(variaveis: dict) -> dict:
    for metricas_dicionario in variaveis["metricas"]:
        return metricas_dicionario


def solicitar_relatorio(variaveis: dict):

    propriedade_id = variaveis["propriedade_id"]
    data_inicio_relatorio = variaveis["data_inicio_relatorio"]
    data_fim_relatorio = variaveis["data_fim_relatorio"]
    dimensoes_dicionario = extrair_dicionario_dimensoes(variaveis=variaveis)
    metricas_dicionario = extrair_dicionario_metricas(variaveis=variaveis)
    credenciais_api_ga4(variaveis=variaveis)

    client = BetaAnalyticsDataClient()
    requisicao = RunReportRequest(
        property=f"properties/{propriedade_id}",
        dimensions=[
            Dimension(name=dimensoes_dicionario["dimensao_nome_a"]),
            Dimension(name=dimensoes_dicionario["dimensao_nome_b"]),
            Dimension(name=dimensoes_dicionario["dimensao_nome_c"]),
            Dimension(name=dimensoes_dicionario["dimensao_nome_d"]),
            Dimension(name=dimensoes_dicionario["dimensao_nome_e"]),
            Dimension(name=dimensoes_dicionario["dimensao_nome_f"]),
            Dimension(name=dimensoes_dicionario["dimensao_nome_g"]),
            Dimension(name=dimensoes_dicionario["dimensao_nome_h"]),
        ],
        metrics=[
            Metric(name=metricas_dicionario["metrica_nome_a"]),
            Metric(name=metricas_dicionario["metrica_nome_b"]),
            Metric(name=metricas_dicionario["metrica_nome_c"]),
            Metric(name=metricas_dicionario["metrica_nome_d"]),
            Metric(name=metricas_dicionario["metrica_nome_e"]),
            Metric(name=metricas_dicionario["metrica_nome_f"]),
            Metric(name=metricas_dicionario["metrica_nome_g"]),
            Metric(name=metricas_dicionario["metrica_nome_h"]),
            Metric(name=metricas_dicionario["metrica_nome_i"]),
            Metric(name=metricas_dicionario["metrica_nome_j"]),
        ],
        date_ranges=[DateRange(start_date=data_inicio_relatorio, end_date=data_fim_relatorio)],
    )
    return client.run_report(requisicao)


def extrair_relatorio(variaveis: dict):

    resposta = solicitar_relatorio(variaveis=variaveis)

    dicionario = []
    for linhaIdx, linha in enumerate(resposta.rows):
        colunas = []
        chaves = []
        valores = []

        for i, dimensao_valores in enumerate(linha.dimension_values):
            dimensao_nome = resposta.dimension_headers[i].name
            colunas.append(dimensao_nome)
            chaves.append(dimensao_nome)
            valores.append(dimensao_valores.value)

        for i, metrica_valores in enumerate(linha.metric_values):
            metrica_nome = resposta.metric_headers[i].name
            colunas.append(metrica_nome)
            chaves.append(metrica_nome)
            valores.append(metrica_valores.value)
        dados = dict(zip(chaves, valores))
        dicionario.append(dados)

    return pd.DataFrame(dicionario, columns=colunas)
