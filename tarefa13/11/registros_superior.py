import registros_medio

class registro_superior(registros_medio.registro_medio):
    """ensino superior de registro"""

    def __init__(self,nome,id,escola,escola_medio,faculdade,cargo):
        super().__init__(nome,id,escola,escola_medio,cargo)
        self._faculdade = faculdade
        self._saldo *= 2
        if cargo == 'gerente':
            self._saldo += 1500.0
        elif cargo == 'supervisor':
            self._saldo += 600.0
        elif cargo == 'vendedor':
            self._saldo += 250.0
    def show(self):
        print(self._nome)
        print(self._saldo)
    def toString(self,cargo):
        if cargo == 'gerente':
            return f'nome: {self._nome} saldo: {self._saldo} cargo: 1500.00'
        elif cargo == 'supervisor':
            return f'nome: {self._nome} saldo: {self._saldo} cargo: 600.00'
        elif cargo == 'vendedor':
            return f'nome: {self._nome} saldo: {self._saldo} cargo: 250.00'