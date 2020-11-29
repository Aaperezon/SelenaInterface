#Esta clase crea paneles  o pantallas que se visualizan con botones, graficas, imagenes, etc...
import wx


class LateralPanel(wx.Panel):
   
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        self.SetBackgroundColour(wx.Colour(255,255,255,0))
        self.reino = ""
        self.filo = ""
        self.clase = ""
        self.orden = ""
        self.familia = ""
        self.genero = ""
        self.especie = ""
        self.nombreComunESP = ""
        self.nombreComunING = ""
        self.sexo = ""
        self.categoriaDeEdad = ""
        self.numeroDeIndividuos = ""
        self.identificadoPor = "Selena"
        
        self.font = wx.Font(14, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        

        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.bg = wx.Bitmap('./src/lateralBack.jpg')
        self._width, self._height  = self.bg.GetSize()
        hSizer = wx.BoxSizer(wx.VERTICAL)

        hSizer.Add((1,1), 1, wx.EXPAND)
        hSizer.Add((1,1), 0, wx.ALL, 100)
        self.SetSizer(hSizer)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

    def OnSize(self, size):
        self.Layout()
        self.Refresh()

    def OnEraseBackground(self, evt):
        pass

    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        self.Draw(dc)

    def Draw(self, dc):
        cliWidth, cliHeight = self.GetClientSize()
        if not cliWidth or not cliHeight:
            return
        dc.Clear()
        xPos = (cliWidth - self._width)/2
        yPos = (cliHeight - self._height)/2
        dc.DrawBitmap(self.bg, 0, 0)



    def ShowMenuPanel(self):
        self.Layout()
        self.Refresh()
        self.Update()
        X = 20
        Y = 30
        XW = 300
        YW = 20
        txtReino = wx.StaticText(self, -1, "Reino:     "+str(self.reino), pos=(X, Y), size=(XW,YW))
        Y+=50
        txtFilo = wx.StaticText(self, -1, "Filo:     "+str(self.filo), pos=(X, Y), size=(XW,YW))
        Y+=50
        txtClase = wx.StaticText(self, -1, "Clase:     "+str(self.clase), pos=(X, Y), size=(XW,YW))
        Y+=50
        txtOrden = wx.StaticText(self, -1, "Orden:     "+str(self.orden), pos=(X, Y), size=(XW,YW))
        Y+=50
        txtFamilia = wx.StaticText(self, -1, "Familia:     "+str(self.familia), pos=(X, Y), size=(XW,YW))
        Y+=50
        txtGenero = wx.StaticText(self, -1, "Genero:     "+str(self.genero), pos=(X, Y), size=(XW,YW))
        Y+=50
        txtEspecie = wx.StaticText(self, -1, "Especie:     "+str(self.especie), pos=(X, Y), size=(XW,YW))
        Y+=50
        txtNombreComunESP = wx.StaticText(self, -1, "NombreComunESP:     "+str(self.nombreComunESP), pos=(X, Y), size=(XW,YW))
        Y+=50
        txtNombreComunING = wx.StaticText(self, -1, "NombreComunING:     "+str(self.nombreComunING), pos=(X, Y), size=(XW,YW))
        Y+=50
        txtSexo = wx.StaticText(self, -1, "Sexo:     "+str(self.sexo), pos=(X, Y), size=(XW,YW))
        Y+=50
        txtCategoriaDeEdad = wx.StaticText(self, -1, "CategoriaDeEdad:     "+str(self.categoriaDeEdad), pos=(X, Y), size=(XW,YW))
        Y+=50
        txtNumeroDeIndividuos = wx.StaticText(self, -1, "NumeroDeIndividuos:     "+str(self.numeroDeIndividuos), pos=(X, Y), size=(XW,YW))
        Y+=50
        txtIdentificadoPor = wx.StaticText(self, -1, "IdentificadoPor:     "+str(self.identificadoPor), pos=(X, Y), size=(XW,YW))
        txtReino.SetFont(self.font)
        txtFilo.SetFont(self.font)
        txtClase.SetFont(self.font)
        txtOrden.SetFont(self.font)
        txtFamilia.SetFont(self.font)
        txtGenero.SetFont(self.font)
        txtEspecie.SetFont(self.font)
        txtNombreComunESP.SetFont(self.font)
        txtNombreComunING.SetFont(self.font)
        txtSexo.SetFont(self.font)
        txtCategoriaDeEdad.SetFont(self.font)
        txtNumeroDeIndividuos.SetFont(self.font)
        txtIdentificadoPor.SetFont(self.font)

   
        
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
