from data import constantes
import random
import sys

sys.path.append('../')


class Persona():

    def __init__(self):

        self._HP = random.randint(
            constantes.MIN_HP_PERSONA, constantes.MAX_HP_PERSONA)

    @property
    def HP(self):
        return self._HP

    @HP.setter
    def HP(self, value):
        self._HP = value


class Trabajador(Persona):

    def __init__(self):

        super().__init__(self)
        self._current = None

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        if value == None:
            self._current = value
        else:
            if self._current == None:
                self._current = value
            else:
                raise ValueError(
                    "Can't assign task: currently {}".format(self._current))

    def recolectar(self):
        return random.randint(constantes.MIN_CANTIDAD_RECURSO, constantes.MAX_CANTIDAD_RECURSO)

    def construir(self):
        pass


class Soldado(Persona):

    def __init__(self):
        super().__init__(self)
        self._poder = random.randint(
            constantes.MIN_ATAQUE_SOLDADO, constantes.MAX_ATAQUE_SOLDADO)

    @property
    def poder(self):
        return self._poder

    @poder.setter
    def poder(self, value):
        self._poder = value

    def atacar(self):
        pass


class Ayudante(Persona):

    def __init__(self):
        super().__init__(self)
        self._IQ = random.randint(
            constantes.MIN_IQ_AYUDANTE, constantes.MAX_IQ_AYUDANTE)

    @property
    def IQ(self):
        return self._IQ

    @IQ.setter
    def IQ(self, value):
        self._IQ = value

    def investigar(self):
        pass
