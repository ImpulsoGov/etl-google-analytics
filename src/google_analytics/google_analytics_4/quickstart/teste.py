# from google_analytics.google_analytics_4.quickstart.credenciais_ga4 import CREDENCIAIS_IP_GA4
import json
import os
from typing import Final

import jsonio
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    MetricType,
    RunReportRequest,
)


def credenciais_api_ga42(variaveis: dict):
    for credenciais_dicionario in variaveis["credenciais_api"]:
        with open("GA4-ImpulsoGov-Credenciais.json", "w") as jsonfile:
            jsonio.dump(credenciais_dicionario, jsonfile)
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "GA4-ImpulsoGov-Credenciais.json"
            credentials = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
