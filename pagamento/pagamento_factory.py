from pagamento.pagamento_cartao import PagamentoCartao
from pagamento.pagamento_pix import PagamentoPIX

class PagamentoFactory:
    @staticmethod
    def criar_pagamento(tipo):
        if tipo == "cartao":
            return PagamentoCartao()
        elif tipo == "pix":
            return PagamentoPIX()
        else:
            raise ValueError(f"Tipo de pagamento '{tipo}' não suportado.")