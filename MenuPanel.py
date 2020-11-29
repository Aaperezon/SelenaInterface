#Esta clase crea paneles  o pantallas que se visualizan con botones, graficas, imagenes, etc...
import wx
import requests
import json
import ast

class MenuPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        self.SetBackgroundColour(wx.Colour(255,255,255,1))
        font = wx.Font(40, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)

        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.bg = wx.Bitmap('./src/menuBack.jpg')
        self._width, self._height  = self.bg.GetSize()
        hSizer = wx.BoxSizer(wx.VERTICAL)

        hSizer.Add((1,1), 1, wx.EXPAND)
        hSizer.Add((1,1), 0, wx.ALL, 75)
        self.SetSizer(hSizer)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        categoria = ['reino','filo','clase' ,'orden' ,'familia' ,'genero','especie','nombreComunESP' ,'nombreComunING','sexo' ,'categoriaDeEdad' ,'numeroDeIndividuos' ,'identificadoPor']
        self.cboxCategoria = wx.ComboBox(self,-1,choices=categoria,size=(120,25))
        self.cboxSeleccion = wx.ComboBox(self,-1,choices=[],size=(120,25))

    def FillComboBox(self, s):
        X = 760
        Y = 90
        separacion = 125
        font = wx.Font(10.5, wx.SCRIPT, wx.NORMAL, wx.NORMAL, 0, "")

        txtCategoria = wx.StaticText(self, -1, "Categoria", pos=(X, Y-17))
        self.cboxCategoria.SetPosition(wx.Point(X,Y))
        self.cboxCategoria.Bind(wx.EVT_TEXT, self.OnSelect)

        print(s)
        if(s == 'reino'):
            self.catego = requests.get('http://localhost:3000/selena/reino')
        elif(s == 'filo'):
            self.catego = requests.get('http://localhost:3000/selena/filo')
        elif(s == 'clase'):
            self.catego = requests.get('http://localhost:3000/selena/clase')
        elif(s == 'orden'):
            self.catego = requests.get('http://localhost:3000/selena/orden')
        elif(s == 'familia'):
            self.catego = requests.get('http://localhost:3000/selena/familia')
        elif(s == 'genero'):
            self.catego = requests.get('http://localhost:3000/selena/genero')
        elif(s == 'especie'):
            self.catego = requests.get('http://localhost:3000/selena/especie')
        elif(s == 'nombreComunESP'):
            self.catego = requests.get('http://localhost:3000/selena/nombreComunESP')
        elif(s == 'nombreComunING'):
            self.catego = requests.get('http://localhost:3000/selena/nombreComunING')
        elif(s == 'sexo'):
            self.catego = requests.get('http://localhost:3000/selena/sexo')
        elif(s == 'categoriaDeEdad'):
            self.catego = requests.get('http://localhost:3000/selena/categoriaDeEdad')
        elif(s == 'numeroDeIndividuos'):
            self.catego = requests.get('http://localhost:3000/selena/numeroDeIndividuos')
        elif(s == 'identificadoPor'):
            self.catego = requests.get('http://localhost:3000/selena/identificadoPor')
       
        if(s != ''):
            self.catego = self.catego.json()
            aux = self.catego
            self.catego = []
            for i in aux:
                self.catego.append(i[s])
            self.cboxSeleccion.Clear()
            self.cboxSeleccion.Append(self.catego)
            X+=separacion
            txtSeleccion = wx.StaticText(self, -1, "Seleccion", pos=(X, Y-17))
            self.cboxSeleccion.SetPosition(wx.Point(X,Y))
            txtSeleccion.SetFont(font)
            self.cboxSeleccion.Bind(wx.EVT_TEXT, self.OnSelectS)
            

    def OnSelect(self,event):
        self.categoria = self.cboxCategoria.GetValue()
        self.FillComboBox(self.categoria)

    def OnSelectS(self,event):
        self.seleccion = self.cboxSeleccion.GetValue()
    def GetCategoria(self):
        return self.categoria
    def GetSeleccion(self):
        return self.seleccion
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
        X = 700
        Y = 0
        self.abrirButton = wx.Button(self, label='Abrir',size=(150, 37))
        self.filtrarButton = wx.Button(self, label='Filtrar',size=(150, 37))
        self.abrirButton.SetPosition(wx.Point(X,Y))
        self.filtrarButton.SetPosition(wx.Point(X+200,Y))

        font = wx.Font(10.5, wx.SCRIPT, wx.NORMAL, wx.NORMAL, 0, "")
        self.abrirButton.SetFont(font)
        self.filtrarButton.SetFont(font)
        #sizer = wx.BoxSizer(wx.VERTICAL)
        sizer = wx.GridSizer(1, 13, 5, 5) 

        
       
       
       

    

    def AbrirButton(self):
        return self.abrirButton
    def FiltrarButton(self):
        return self.filtrarButton


    def UpdateMenu(self):
        X,Y = self.GetSize()
        Y = Y-100
        if(X>=0):
            abrirX = (X/2)-50
            textX = (X/2)-300
            self.abrirButton.SetPosition(wx.Point(abrirX,Y))
           