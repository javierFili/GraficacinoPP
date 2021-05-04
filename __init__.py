import math

import  pygame
from figuras import Figuras
# from Figuras import Figuras
from Boton import Boton
from Cursor import Cursor
from Transformaciones import Transformaciones
puntoFIjoX = 500
puntoFIjoY = 300

cuadrado = False
triangulo = False
circulo = False

cuadradoPredeterminadoAx = 234
cuadradoPredeterminadoAy = 234

cuadradoPredeterminadoBx = 500
cuadradoPredeterminadoBy = 234

cuadradoPredeterminadoCx = 234
cuadradoPredeterminadoCy = 500

cuadradoPredeterminadoDx = 500
cuadradoPredeterminadoDy = 500

cuadradoPredeterminado = [(cuadradoPredeterminadoAx, cuadradoPredeterminadoAy),(cuadradoPredeterminadoBx, cuadradoPredeterminadoBy),(cuadradoPredeterminadoCx,cuadradoPredeterminadoCy),
                          (cuadradoPredeterminadoDx, cuadradoPredeterminadoDy)]

trianguloPredeterminado = [(100,100),(300,300),(450,150)]

circuloPredeterminado = [(500,300),(150, 0)]

transf = Transformaciones()

# def limpiar():


def main1():

    pygame.init()
    pantalla = pygame.display.set_mode((1360,680))

    pygame.display.set_caption("Graficacion")
    reloj1 = pygame.time.Clock()
    # .Colores En RGB
    blanco = (255, 255, 255)
    rojo = (200, 0, 0)
    navajowhite=(255, 222, 173)# s1 es asi.
    negro=(0,0,0)



    #Rect secundario
    s1=pygame.surface.Surface((280,680))
    color= (255, 222, 173)
    s1.fill(color)
    gros=pygame.Rect(1280,150,20,20)
    espa=pygame.Rect(1280,200,20,20)
    segm=pygame.Rect(1280,250,20,20)
    trasx=pygame.Rect(1130, 395, 20, 20)
    trasy=pygame.Rect(1250, 395, 20, 20)
    escx = pygame.Rect(1130, 485, 20, 20)
    escy = pygame.Rect(1250, 485, 20, 20)
    rotGr = pygame.Rect(1130, 575, 20, 20)


    #Texto
    fuente1=pygame.font.Font(None,25)
    texGros="Grosor"
    grosTex=fuente1.render(texGros,0,(0,0,0))

    texEspa="Segmentacion"
    espaTex=fuente1.render(texEspa,0,(0,0,0))

    texSegm="Espacio"
    segmTex=fuente1.render(texSegm,0,(0,0,0))

    texTrans1 = "Transformaciones"
    fuente=pygame.font.Font(None, 34)
    trans1Text=fuente.render(texTrans1,0,(0,0,0))

    texEsca = "Escalacion"
    escaTex =fuente1.render(texEsca,0,(0,0,0))

    texRota = "Rotacion"
    rotaTex =fuente1.render(texRota,0,(0,0,0))

    texTras = "Traslacion"
    tranTex =fuente1.render(texTras,0,(0,0,0))

    texCam1=".jpg"
    texCam2=".png"
    texCam3=".bmp"
    texCam4=".tga"
    texCam=[texCam1,texCam2,texCam3,texCam4]
    n=0

    #botones importantes
    imaTrian = pygame.image.load("triangle.png")
    imaTrian1 = pygame.image.load("triangulo.png")
    bttriangulo = Boton(imaTrian,imaTrian1,1220,20)

    imaCuadr=pygame.image.load("square.png")
    imaCuadr1=pygame.image.load("square1.png")
    btcuadrado=Boton(imaCuadr1,imaCuadr,1155,20)

    imaCir=pygame.image.load("circle.png")
    imaCir1=pygame.image.load("circle1.png")
    btcirculo=Boton(imaCir,imaCir1,1299,20)

    imades=pygame.image.load("descar1.png")
    imades1=pygame.image.load("descar.png")
    btdescargar=Boton(imades,imades1,1260,630)

    imaInterCam=pygame.image.load("interCam1.png")
    imaInterCam1=pygame.image.load("inteCam.png")
    btInterCamb=Boton(imaInterCam,imaInterCam1,1140,630)#text 160 ..

    #botones segundarios
    imaMas=pygame.image.load("mas1.png")
    imaMen=pygame.image.load("menos.png")
    imaMen1=pygame.image.load("menos1.png")
    imaMas1=pygame.image.load("mas.png")
    imaPlay = pygame.image.load("play.png")
    imaPlay1 = pygame.image.load("play1.png")
    btGrosMas=Boton(imaMas,imaMas1,1250,140)
    btGrosMen=Boton(imaMen,imaMen1,1250,160)
    btSegmMas=Boton(imaMas,imaMas1,1250,190)
    btSegmMen=Boton(imaMen,imaMen1,1250,210)
    btEspaMas=Boton(imaMas,imaMas1,1250,240)
    btEspaMen=Boton(imaMen,imaMen1,1250,260)
    btTraslacionXmas = Boton(imaMas, imaMas1, 1160, 385)
    btTraslacionXmenos = Boton(imaMen, imaMen1, 1160, 405)
    btTraslacionYmas = Boton(imaMas, imaMas1, 1280, 385)
    btTraslacionYmenos = Boton(imaMen, imaMen1, 1280, 405)
    btTraslacionPlay = Boton(imaPlay, imaPlay1, 1230, 345)

    btEscalacionXmas = Boton(imaMas, imaMas1, 1160, 475)
    btEscalacionXmenos = Boton(imaMen, imaMen1, 1160, 495)
    btEscalacionYmas = Boton(imaMas, imaMas1, 1280, 475)
    btEscalacionYmenos = Boton(imaMen, imaMen1, 1280, 495)
    btEscalacionPlay = Boton(imaPlay, imaPlay1, 1230, 435)

    btRotacionMas = Boton(imaMas, imaMas1, 1160, 565)
    btRotacionMenos = Boton(imaMen, imaMen1, 1160, 585)
    btRotacionPlay = Boton(imaPlay, imaPlay1, 1230, 525)


    #figuras
    fig= Figuras()
    salir=False
    cursor1 = Cursor()
    # contadores
    grosor=0
    segmentacion=0
    espacio=0
    traslacionx = 0
    traslaciony = 0
    escalacionx = 0
    escalaciony = 0
    rotacionGrados = 90
    versionDescarga = 1
    pantalla.fill(blanco)
    while salir !=True:
        # pa_ = pygame.PixelArray(pantalla)
        # fig.pintar(puntoFIjoX, puntoFIjoY, pa_, rojo)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(btcuadrado.rect):
                    pantalla.fill(blanco)
                    listaPuntosActual = cuadradoPredeterminado.copy()
                    fig.cuadrilatero(cuadradoPredeterminado, pantalla,
                                negro, segmentacion, espacio, grosor)
                    triangulo = False
                    circulo = False
                    cuadrado = True
                if cursor1.colliderect(bttriangulo.rect):
                    pantalla.fill(blanco)
                    listaPuntosActual = trianguloPredeterminado.copy()
                    fig.triangulo(trianguloPredeterminado,pantalla,
                                  negro,segmentacion,espacio,grosor)
                    triangulo = True
                    circulo = False
                    cuadrado = False
                if cursor1.colliderect(btcirculo.rect):
                    pantalla.fill(blanco)
                    listaPuntosActual = circuloPredeterminado.copy()
                    fig.circulo(circuloPredeterminado,negro,pantalla)
                    triangulo = False
                    circulo = True
                    cuadrado = False

                if cursor1.colliderect(btSegmMas.rect):
                    segmentacion= segmentacion + 1
                if cursor1.colliderect(btSegmMen.rect):
                    segmentacion= segmentacion - 1
                if cursor1.colliderect(btEspaMas.rect):
                    espacio= espacio + 1
                if cursor1.colliderect(btEspaMen.rect):
                    espacio= espacio - 1
                if cursor1.colliderect(btGrosMas.rect):
                    grosor= grosor + 1
                if cursor1.colliderect(btGrosMen.rect):
                    grosor= grosor - 1
                if cursor1.colliderect(btTraslacionXmas.rect):
                    traslacionx = traslacionx + 10
                if cursor1.colliderect(btTraslacionXmenos.rect):
                    traslacionx = traslacionx - 10
                if cursor1.colliderect(btTraslacionYmas.rect):
                    traslaciony = traslaciony + 10
                if cursor1.colliderect(btTraslacionYmenos.rect):
                    traslaciony = traslaciony - 10
                if cursor1.colliderect(btEscalacionXmas.rect):
                    escalacionx += 0.25
                if cursor1.colliderect(btEscalacionXmenos.rect):
                    escalacionx -= 0.25
                if cursor1.colliderect(btEscalacionYmas.rect):
                    escalaciony += 0.25
                if cursor1.colliderect(btEscalacionYmenos.rect):
                    escalaciony -= 0.25
                if cursor1.colliderect(btRotacionMas.rect):
                    rotacionGrados += 5
                if cursor1.colliderect(btRotacionMenos.rect):
                    rotacionGrados -= 5
                if cursor1.colliderect(btTraslacionPlay.rect):
                    # s1.fill(blanco)
                    pantalla.fill(blanco)
                    transf.traslacion(listaPuntosActual, traslacionx, traslaciony)
                    if cuadrado:
                        fig.cuadrilatero(listaPuntosActual, pantalla, negro, segmentacion, espacio, grosor)
                    else:
                        if triangulo:
                            fig.triangulo(listaPuntosActual,pantalla, negro, segmentacion, espacio, grosor)
                        else:
                            fig.circulo(listaPuntosActual, negro, pantalla)
                if cursor1.colliderect(btEscalacionPlay.rect):
                    pantalla.fill(blanco)
                    transf.escalacion(listaPuntosActual, escalacionx, escalaciony, puntoFIjoX, puntoFIjoY)
                    if cuadrado:
                        fig.cuadrilatero(listaPuntosActual, pantalla, negro, segmentacion, espacio, grosor)
                    else:
                        if triangulo:
                            fig.triangulo(listaPuntosActual,pantalla, negro, segmentacion, espacio, grosor)
                        else:
                            fig.circulo(listaPuntosActual, negro, pantalla)
                if cursor1.colliderect(btRotacionPlay.rect):
                    pantalla.fill(blanco)
                    rad = rotacionGrados*math.pi/180
                    transf.rotacion(listaPuntosActual, rad, puntoFIjoX, puntoFIjoY)
                    if cuadrado:
                        fig.cuadrilatero(listaPuntosActual, pantalla, negro, segmentacion, espacio, grosor)
                    else:
                        if triangulo:
                            fig.triangulo(listaPuntosActual,pantalla, negro, segmentacion, espacio, grosor)
                        else:
                            fig.circulo(listaPuntosActual, negro, pantalla)
                if cursor1.colliderect(btdescargar.rect):
                    zonaDeTrabajo = pygame.Rect(0, 0, 1000, 600)
                    superficie = pantalla.subsurface(zonaDeTrabajo)
                    nombreArchivo = "imagen"+str(versionDescarga)
                    if n != 0:
                        pygame.image.save(superficie, "descargas/"+ nombreArchivo + texCam[n-1])
                    else:
                        pygame.image.save(superficie, "descargas/" + nombreArchivo + texCam[n])
                    versionDescarga += 1

                if cursor1.colliderect(btInterCamb.rect):
                    if n<=3:
                        rect=pygame.Rect(1060,630,40,20)
                        pygame.draw.rect(pantalla,blanco,rect)
                        actu=str(texCam[n])
                        super=fuente1.render(actu, 0, negro)
                        pantalla.blit(super,(1060,630))
                        n = n + 1
                    else:
                        n=0


        reloj1.tick(20)

        #actualizamos cursor

        cursor1.update()
        #inio de las surfaces
        pantalla.blit(s1,[1100,0])

        # iniciamos cuadros
        pygame.draw.rect(pantalla, (blanco), gros)
        pygame.draw.rect(pantalla, (blanco), espa)
        pygame.draw.rect(pantalla, (blanco), segm)
        pygame.draw.rect(pantalla, (blanco), trasx)
        pygame.draw.rect(pantalla, (blanco), trasy)
        pygame.draw.rect(pantalla, blanco, escx)
        pygame.draw.rect(pantalla, blanco, escy)
        pygame.draw.rect(pantalla, blanco, rotGr)


        #textos
        pantalla.blit(grosTex,(1130,150))# 1140 145 155 botones
        pantalla.blit(espaTex,(1130,200))#1140  195 205 botones
        pantalla.blit(segmTex,(1130,250))#1140  245 255 botones

        pantalla.blit(trans1Text, (1100,300))
        pantalla.blit(tranTex,(1130,350))
        pantalla.blit(escaTex,(1130,440))
        pantalla.blit(rotaTex,(1130,530))

        # los botones acualiza
        btdescargar.update(pantalla, cursor1)
        btcirculo.update(pantalla, cursor1)
        btcuadrado.update(pantalla, cursor1)
        bttriangulo.update(pantalla, cursor1)
        btGrosMas.update(pantalla,cursor1)
        btGrosMen.update(pantalla,cursor1)
        btEspaMas.update(pantalla,cursor1)
        btEspaMen.update(pantalla,cursor1)
        btSegmMas.update(pantalla,cursor1)
        btSegmMen.update(pantalla,cursor1)
        btTraslacionXmas.update(pantalla, cursor1)
        btTraslacionXmenos.update(pantalla, cursor1)
        btTraslacionYmas.update(pantalla, cursor1)
        btTraslacionYmenos.update(pantalla, cursor1)
        btTraslacionPlay.update(pantalla, cursor1)
        btEscalacionXmas.update(pantalla,cursor1)
        btEscalacionXmenos.update(pantalla, cursor1)
        btEscalacionYmas.update(pantalla, cursor1)
        btEscalacionYmenos.update(pantalla, cursor1)
        btEscalacionPlay.update(pantalla, cursor1)
        btInterCamb.update(pantalla, cursor1)
        btRotacionMas.update(pantalla, cursor1)
        btRotacionMenos.update(pantalla, cursor1)
        btRotacionPlay.update(pantalla, cursor1)
        #corremos contadores

        conSegm1 = str(segmentacion)
        conGros1 = str(grosor)
        conEspa1 = str(espacio)
        conTraslx = str(traslacionx)
        conTrasly = str(traslaciony)
        conEscalx = str(escalacionx)
        conEscaly = str(escalaciony)
        conRotG = str(rotacionGrados)
        segCont = fuente1.render(conSegm1, 0, negro)
        grosCon = fuente1.render(conGros1, 0, negro)
        espaCon = fuente1.render(conEspa1, 0, negro)
        traslxCon = fuente1.render(conTraslx, 0, negro)
        traslyCon = fuente1.render(conTrasly, 0, negro)
        escalxCon = fuente1.render(conEscalx, 0, negro)
        escalyCon = fuente1.render(conEscaly, 0, negro)
        rotGCon = fuente1.render(conRotG, 0, negro)
        pantalla.blit(segCont,(1280,200))
        pantalla.blit(grosCon,(1280,150))
        pantalla.blit(espaCon,(1280,250))
        pantalla.blit(traslxCon, (1130, 395))
        pantalla.blit(traslyCon, (1250, 395))
        pantalla.blit(escalxCon, (1130, 485))
        pantalla.blit(escalyCon, (1250, 485))
        pantalla.blit(rotGCon, (1130, 575))
        # hasta ahi
        pygame.display.update()

    pygame.quit()


if __name__=='__main__':
    main1()