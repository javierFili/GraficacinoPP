import math

class Transformaciones:


    def __init__(self):
        pass

    def traslacionP(self,px, py, sumax, sumay):
        return (px +sumax, py + sumay)


    def escalacionP(self,px, py, escalaX, escalaY, fijoX, fijoY):
        return (round(px*escalaX+(1-escalaX)*fijoX), round(py*escalaY+(1-escalaY)*fijoY))


    def rotacionP(self,px, py, angulo, fijoX, fijoY):
        # return (round(px*math.cos(angulo)-py*math.sin(angulo)), round(px*math.sin(angulo)-py*math.cos(angulo)))
        return (round(fijoX + (px - fijoX)*math.cos(angulo) - (py -fijoY)*math.sin(angulo)),
                round(fijoX + (px - fijoX)*math.sin(angulo) - (py -fijoY)*math.cos(angulo)))

    def traslacion(self, listaP, sumax, sumay):
        if len(listaP) == 2:
            listaP[0] = (listaP[0][0]+sumax, listaP[0][1]+sumay)
        else:
            for i in range(len(listaP)):
                px, py = listaP[i]
                listaP[i] = self.traslacionP(px, py, sumax, sumay)


    def escalacion(self,listaP, escalaX, escalaY, fijoX, fijoY):
        if len(listaP) == 2:
            listaP[1] = (round(listaP[1][0]*escalaX), 0)
        else:
            for i in range(len(listaP)):
                px, py = listaP[i]
                listaP[i] = self.escalacionP(px, py, escalaX, escalaY, fijoX, fijoY)


    def rotacion(self,listaP, angulo, fijoX, fijoY):
        if len(listaP) == 2:
            px, py = listaP[0]
            listaP[0] = self.rotacionP(px, py, angulo, fijoX, fijoY)
        for i in range(len(listaP)):
            px, py = listaP[i]
            # r = math.dist([px,py],[fijoX, fijoY])
            listaP[i] = self.rotacionP(px, py, angulo, fijoX, fijoY)