from pytest import fixture, mark

from src.google_analytics.bd import Sessao
from src.google_analytics.scripts.impulso_previne import listar_registros_agendamentos


def test_listar_registros_agendamentos():

    operacao_id = "063aaf29-4b06-7b27-beb8-7be99f22b396"
    with Sessao() as sessao:
        listar_registros_agendamentos(sessao=sessao, operacao_id=operacao_id)


def listar_variaveis_agendamentos():

    operacao_id = "063aaf29-4b06-7b27-beb8-7be99f22b39g"
    with Sessao() as sessao:
        listar_registros_agendamentos(sessao=sessao, operacao_id=operacao_id)
