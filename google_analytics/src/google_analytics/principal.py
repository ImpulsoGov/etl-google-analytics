from google_analytics.bd import Sessao
from google_analytics.scripts.impulso_previne import (
    principal as capturas_impulso_previne,
)


def principal(teste: bool = False) -> None:
    with Sessao() as sessao:
        capturas_impulso_previne(sessao=sessao, teste=teste)


if __name__ == "__main__":
    principal()
