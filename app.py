import random
import gi
import logging
from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import (ActivityToolbarButton, StopButton)

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
logger = logging.getLogger(__name__)


class FaunaFlora(activity.Activity):

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
        self.contenedor = Gtk.Grid()
        self.contenedor.set_row_homogeneous(False)

        self.contenedor.set_column_homogeneous(True)
        self.add(self.contenedor)

    def PrimeraVentanaPlanta(self):
        self.planta = Gtk.Button('Clasificacion de las plantas')
        self.animales = Gtk.Button('Clasificacion de los animales')
        self.contenedor.attach(self.planta, 0, 0, 1, 1)
        self.contenedor.attach_next_to(
            self.animales,
            self.planta,
            Gtk.PositionType.RIGHT,
            1,
            1
        )
        #self.planta.connect('clicked', self.SegundaVentanaPlanta)
        #self.animales.connect('clicked', self.SegundaVentanaAnimal)
