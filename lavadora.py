class Lavadora:

    def __init__(self):
        pass

    def lavar(self,temperatura='Hot'):
        self._llenar_tanque(temperatura)
        self._anadir_jabon() #Llama a los diferentes métodos
        self._lavar()
        self._centrifugar()

    def _llenar_tanque(self, temperatura):
        print(f'Llenando tanque con agua {temperatura}')

    def _anadir_jabon(self):
        print('Añadiendo jabon')

    def _lavar(self):
        print('Lavando...')

    def _centrifugar(self):
        print('Centrifugando...')

if __name__=='__main__':
    lavadora=Lavadora()
    lavadora.lavar()