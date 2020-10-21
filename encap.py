#Encapsulacion
 
class CasillaDeVotacion:
    def __init__(self, id, pais):
        self.id = id
        self._pais = pais
        self.__region = None

    @property   #Indica que es una función encapsulada y a su vez getter
    def region(self):
        return self.__region
    
    @region.setter  #Decorador de modificación setter
    def region(self, region):#Función decorada para cambiar o agregar la región note que es la misma función region
        if region in self._pais: #Función de verificación
            self.__region = region   #Modificación del atributo      
        else:
            raise ValueError(f'La region {region} no es una opcion valida en {self._pais}') 
    
    @region.deleter
    def region(self):
        print('Borrando region...')
        del self.__region

if __name__ == "__main__":
    casilla = CasillaDeVotacion(123, ['Cali', 'Medellin'])
    print(casilla.region)
    casilla.region = 'Cali'    
    print(casilla.region)
    del casilla.region
    casilla.region = 'Medellin'
    print(casilla.region)