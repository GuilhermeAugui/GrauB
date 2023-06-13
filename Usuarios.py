class Ususario:
    def __init__(self, nome,senha,tipoAsinatura):
        self._nome= nome
        self._senha= senha
        self._tipoAsinatura= tipoAsinatura
    def adicionaPerfil(self,nome,idade):
        perfil=[]
        if self._tipoAsinatura == 'SIMPLES' and len(perfil) < 3:
            nome.append    