import glob
import os
import wx
from DeepLearning import *
import requests

class ImagePanel(wx.Panel):
   
    def __init__(self,parent):
        super().__init__(parent)
        self.SetBackgroundColour(wx.Colour(154, 171, 145))

        self.max_size = 800
        self.photos = []
        self.current_photo = 0
        self.total_photos = 0
        self.layout()

        self.slideshow_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_next, self.slideshow_timer)

    def layout(self):
        """
        Layout the widgets on the panel
        """

        self.main_sizer = wx.BoxSizer(4)
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)

        img = wx.Image(self.max_size, self.max_size)
        self.image_ctrl = wx.StaticBitmap(self, wx.ID_ANY,wx.Bitmap(img))
        self.main_sizer.Add(self.image_ctrl, 0, wx.ALL|wx.CENTER, 5)
        self.image_label = wx.StaticText(self, label="")
        self.main_sizer.Add(self.image_label, 0, wx.ALL|wx.CENTER, 5)

        btn_data = [("Previous", btn_sizer, self.on_previous),
                    ("Slide Show", btn_sizer, self.on_slideshow),
                    ("Next", btn_sizer, self.on_next)]
        for data in btn_data:
            label, sizer, handler = data
            self.btn_builder(label, sizer, handler)

        self.main_sizer.Add(btn_sizer, 0, wx.CENTER)
        self.SetSizer(self.main_sizer)

    def btn_builder(self, label, sizer, handler):
        """
        Builds a button, binds it to an event handler and adds it to a sizer
        """
        btn = wx.Button(self, label=label)
        btn.Bind(wx.EVT_BUTTON, handler)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)

    def on_next(self, event):
        """
        Loads the next picture in the directory
        """
        if not self.photos:
            return

        if self.current_photo == self.total_photos - 1:
            self.current_photo = 0
        else:
            self.current_photo += 1
        self.update_photo(self.photos[self.current_photo])

    def on_previous(self, event):
        """
        Displays the previous picture in the directory
        """
        if not self.photos:
            return

        if self.current_photo == 0:
            self.current_photo = self.total_photos - 1
        else:
            self.current_photo -= 1
        self.update_photo(self.photos[self.current_photo])

    def on_slideshow(self, event):
        """
        Starts and stops the slideshow
        """
        btn = event.GetEventObject()
        label = btn.GetLabel()
        if label == "Slide Show":
            self.slideshow_timer.Start(3000)
            btn.SetLabel("Stop")
        else:
            self.slideshow_timer.Stop()
            btn.SetLabel("Slide Show")
    def GetCurrentPhoto(self):
        return self.photos[self.current_photo]
    def update_photo(self, image):
        """
        Update the currently shown photo
        """
        contador = wx.StaticText(self, -1, str(self.current_photo+1)+"/"+str(len(self.photos)), pos=(910,180))
        font = wx.Font(40, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        contador.SetFont(font)
        self.MachineLearning()

        img = wx.Image(image, wx.BITMAP_TYPE_ANY)
        # scale the image, preserving the aspect ratio
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.max_size
            NewH = self.max_size * H / W
        else:
            NewH = self.max_size
            NewW = self.max_size * W / H
        img = img.Scale(NewW, NewH)

        self.image_ctrl.SetBitmap(wx.Bitmap(img))
        self.Refresh()
    def SetLateralPanel(self, l):
        self.lateralPanel = l
    def MachineLearning(self):
        a = self.GetCurrentPhoto()
        a = Work(a)
        request = requests.get('http://localhost:3000/selena/animalVistaActual/'+a)
        request = request.json()
        aux = request
        request = []
        for i in aux:
            print(i['especie'])
            self.lateralPanel.Reino(i['reino'])
            self.lateralPanel.Filo(i['filo'])
            self.lateralPanel.Clase(i['clase'])
            self.lateralPanel.Orden(i['orden'])
            self.lateralPanel.Familia(i['familia'])
            self.lateralPanel.Genero(i['genero'])
            self.lateralPanel.Especie(i['especie'])
            self.lateralPanel.NombreComunESP(i['nombreComunESP'])
            self.lateralPanel.NombreComunING(i['nombreComunING'])
            self.lateralPanel.Sexo(i['sexo'])
            self.lateralPanel.CategoriaDeEdad(i['categoriaDeEdad'])
            self.lateralPanel.NumeroDeIndividuos(i['numeroDeIndividuos'])
            self.lateralPanel.IdentificadoPor(i['identificadoPor'])
        self.lateralPanel.ShowMenuPanel()
        
    def Reino(self):
        return self.reino
    def Reino(self,it):
        self.reino = it
    def Filo(self):
        return self.filo
    def Filo(self,it):
        self.filo = it
    def Clase(self):
        return self.clase
    def Clase(self,it):
        self.clase = it
    def Orden(self):
        return self.orden
    def Orden(self,it):
        self.orden = it
    def Familia(self):
        return self.familia
    def Familia(self,it):
        self.familia = it
    def Genero(self):
        return self.genero
    def Genero(self,it):
        self.genero = it
    def Especie(self):
        return self.especie
    def Especie(self,it):
        self.especie = it
    def NombreComunESP(self):
        return self.nombreComunESP
    def NombreComunESP(self,it):
        self.nombreComunESP = it
    def NombreComunING(self):
        return self.nombreComunING
    def NombreComunING(self,it):
        self.nombreComunING = it
    def Sexo(self):
        return self.sexo
    def Sexo(self,it):
        self.sexo = it
    def CategoriaDeEdad(self):
        return self.categoriaDeEdad
    def CategoriaDeEdad(self,it):
        self.categoriaDeEdad = it
    def NumeroDeIndividuos(self):
        return self.numeroDeIndividuos
    def NumeroDeIndividuos(self,it):
        self.numeroDeIndividuos = it
    def IdentificadoPor(self):
        return self.identificadoPor
    def IdentificadoPor(self,it):
        self.identificadoPor = it
        """
        self.lateralPanel.Especie(a)
        self.lateralPanel.ShowMenuPanel()
        """

    def reset(self):
        img = wx.Image(self.max_size, self.max_size)
        bmp = wx.Bitmap(img)
        self.image_ctrl.SetBitmap(bmp)
        self.current_photo = 0
        self.photos = []
