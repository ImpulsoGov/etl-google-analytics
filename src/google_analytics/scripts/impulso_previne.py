from sqlalchemy.orm import Session

from google_analytics.bd import Sessao, tabelas
from google_analytics.google_analytics_4.quickstart.principal import (
    obter_relatorio_quickstart,
)

agendamentos = tabelas["configuracoes.capturas_operacoes"]


def listar_registros_agendamentos(sessao: Session, operacao_id: str):

    return sessao.query(agendamentos).filter(agendamentos.c.id == operacao_id).all()


def listar_variaveis_agendamentos(agendamento_operacao):

    for agendamento in agendamento_operacao:
        return agendamento.parametros


def extrair_tabela_destino(agendamento_operacao):

    for agendamento in agendamento_operacao:
        return agendamento.tabela_destino


def relatorio_ga4_quickstart(sessao: Session, teste: bool = False) -> None:

    operacao_id = "063aaf29-4b06-7b27-beb8-7be99f22b396"
    agendamento_operacao = listar_registros_agendamentos(sessao=sessao, operacao_id=operacao_id)
    tabela_destino = extrair_tabela_destino(agendamento_operacao)
    variaveis = listar_variaveis_agendamentos(agendamento_operacao=agendamento_operacao)

    obter_relatorio_quickstart(sessao=sessao, tabela_destino=tabela_destino, variaveis=variaveis)

    if teste:
        sessao.rollback()

    sessao.commit()


def principal(sessao: Session, teste: bool = False) -> None:

    # Lista de relatórios do GA4 para operação de ETL
    relatorio_ga4_quickstart(sessao=sessao, teste=teste)




