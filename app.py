import random
import gi
import logging
from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import (ActivityToolbarButton, StopButton)

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
logger = logging.getLogger(__name__)


class faunaflora(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        self.agregar_toolbar()
        self.agregar_contenedor()
        self.PrimeraVentanaPlanta()
        

    def agregar_toolbar(self):
        toolbar_box = ToolbarBox()
        aplicacion_toolbar_boton = ActivityToolbarButton(self)
        aplicacion_stop_boton = StopButton(self)
        toolbar_box.toolbar.insert(aplicacion_toolbar_boton, 0)
        aplicacion_toolbar_boton.show()
        toolbar_box.toolbar.insert(aplicacion_stop_boton, -1)
        aplicacion_stop_boton.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

    def agregar_contenedor(self):
        self.canvas = Gtk.Grid()
        self.add(self.canvas)

    def PrimeraVentanaPlanta(self):
        self.planta = Gtk.Button('Clasificacion de las plantas')
        self.animales = Gtk.Button('Clasificacion de los animales')
        self.canvas.attach(self.planta, 0, 0, 1, 1)
        self.canvas.attach_next_to(
            self.animales,
            self.planta,
            Gtk.PositionType.RIGHT,
            1,
            1
        )
        self.planta.connect('clicked',self.SegundaVentanaPlanta)
        self.animales.connect('clicked',self.SegundaVentanaAnimal)
        self.canvas.show_all()

    def SegundaVentanaPlanta(self,btn):

        for widget in self.canvas:
            self.canvas.remove(widget)

        self.label_conflor_planta = Gtk.Label('Con Flor')
        self.label_sinflor_planta = Gtk.Label('sin Flor')

        self.boton_siguiente_planta = Gtk.Button('Siguinte')
        self.canvas.attach(self.label_conflor_planta,0,0,1,1)
        self.canvas.attach_next_to(self.label_sinflor_planta,self.label_conflor_planta,Gtk.PositionType.BOTTOM,1,1)
        self.canvas.attach(self.boton_siguiente_planta,0,2,1,1)

        self.canvas.show_all()
        self.boton_siguiente_planta.connect('clicked',self.TerceraVentanaPlanta)
        


    def TerceraVentanaPlanta(self,b):
        
        for widget in self.canvas:
            self.canvas.remove(widget)
        
    
        self.boton_inicio_planta = Gtk.Button('Inicio')
        self.label_numero_planta = Gtk.Label('Numero de veces')
        self.numero_de_entrada_planta = Gtk.Entry() 
        self.canvas.attach(self.label_numero_planta,0,0,1,1)
        self.canvas.attach_next_to(self.numero_de_entrada_planta,self.label_numero_planta,Gtk.PositionType.RIGHT,1,1)
        self.canvas.attach_next_to(self.boton_inicio_planta,self.label_numero_planta,Gtk.PositionType.BOTTOM,1,1)
        self.canvas.show_all()
        self.boton_inicio_planta.connect('clicked',self.CuartaVentanaPlanta)


    def CuartaVentanaPlanta(self,btn):

        for widget in self.canvas:
            self.canvas.remove(widget)

        self.label_planta = Gtk.Label('las plantas de mi pais')
        self.canvas.attach(self.label_planta,0,0,1,1)
        self.canvas.show_all()


    def SegundaVentanaAnimal(self,btn):

        for widget in self.canvas:
            self.canvas.remove(widget)

        self.label_dondeviven_animal = Gtk.Label('Donde Viven')
        self.label_alimentacion_animal = Gtk.Label('Su alimentacion')

        self.boton_siguiente_animal = Gtk.Button('Siguiente')

        self.canvas.attach(self.label_dondeviven_animal,0,0,1,1)
        self.canvas.attach_next_to(self.label_alimentacion_animal,self.label_dondeviven_animal,Gtk.PositionType.BOTTOM,1,1)
        self.canvas.attach(self.boton_siguiente_animal,0,2,1,1)

        self.canvas.show_all()
        self.boton_siguiente_animal.connect('clicked',self.TerceraVentanaAnimal)
        


    def TerceraVentanaAnimal(self,b):
        
        for widget in self.canvas:
            self.canvas.remove(widget)
        
        
        self.boton_inicio_animal = Gtk.Button('Inicio')
        self.label_numero_animal = Gtk.Label('Numero de veces')
        self.numero_de_entrada_animal = Gtk.Entry() 
        self.canvas.attach(self.label_numero_animal,0,0,1,1)
        self.canvas.attach_next_to(self.numero_de_entrada_animal,self.label_numero_animal,Gtk.PositionType.RIGHT,1,1)
        self.canvas.attach_next_to(self.boton_inicio_animal,self.label_numero_animal,Gtk.PositionType.BOTTOM,1,1)
        self.canvas.show_all()
        self.boton_inicio_animal.connect('clicked',self.CuartaVentanaAnimal)


    def CuartaVentanaAnimal(self,btn):
        for widget in self.canvas:
            self.canvas.remove(widget)

        self.label_animal = Gtk.Label('Los animales de mi pais')
        self.canvas.attach(self.label_animal,0,0,1,1)
        self.canvas.show_all()


