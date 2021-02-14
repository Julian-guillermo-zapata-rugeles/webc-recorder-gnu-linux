import os
import time

"""
Este script es Desarollado por Julián Guillermo Zapata Rugeles
su objetivo es dotar una simple estructura de control mediante clases
para la gestión de diferentes interfaces de aplicación de la línea de comandos
se empleará para uso del CRONTAB.




Puedes crear tus copias y distribuirlas bajo software libre.
    Algunos módulos como ffmpeg son independientes del este proyecto
    por ende merecen el crédito por ello.



"""


VIDEOS_SESSION = 1


class Capturador(object):
    """ El objetivo de este script es generar grabaciones de Vídeo Empleando ffmpeg .
        Este módulo se encuentra disponible a través de la líne a de comandos en
        distrubuciones GNU/LINUX , WINDOWS .

        sudo apt-get install ffmpeg
            ffmpeg es un módulo que permite el procesamiento de audio y vídeo así
            como diferentes operaciones de modificación de estos mismos.

            para más documentación busque FFMPEG

    """

    PATH=""
    OUTPUT = "videos"


    def __init__(self):

        # Método constructor del script
        super(Capturador, self).__init__()
        self.obtenerRuta()
        self.crearDirectorio()


    def obtenerRuta(self):
        tmp_path=os.popen("pwd").read()
        self.PATH  = tmp_path[:-1]

    def crearDirectorio(self):
        os.system("mkdir "+self.OUTPUT+" > /dev/null 2>&1")

    def grabarVideo(self, segundos ):
        tmp_file_name = "/"+time.asctime().replace(" ","-")+".avi"
        tmp_command = "ffmpeg  -f video4linux2 -i /dev/video0 -f alsa -i hw:0 -acodec mp2 -qscale 0 -t "+str(segundos)+" "+self.PATH+"/"+self.OUTPUT+tmp_file_name
        print("-----------------------------------------------------")
        print("              Grabando {} segundos".format(segundos))
        print("-----------------------------------------------------")
        os.system(tmp_command)

gestor=Capturador()
while VIDEOS_SESSION > 0:
    gestor.grabarVideo(55)
    time.sleep(5)
    VIDEOS_SESSION-=1
    print(" --------------- Reiniciando ----------------------")
