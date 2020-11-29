#Este es el main del proyecto
import wx
import wx.lib.agw.fourwaysplitter as fws
from selector import *
from DeepLearning import *

from PIL import Image
from MenuPanel import MenuPanel
from ImagePanel import ImagePanel
from LateralPanel import LateralPanel

import requests

import glob
import os
import wx
import os
import shutil
class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title = "Selena",size = (1700,1000))
        topSplitter = wx.SplitterWindow(self)
        vSplitter = wx.SplitterWindow(topSplitter)
        
        self.lateralPanel = LateralPanel(vSplitter)
        self.imagePanel = ImagePanel(vSplitter)
        vSplitter.SplitVertically(self.lateralPanel, self.imagePanel)
        vSplitter.SetMinimumPaneSize(400)
        self.menuPanel = MenuPanel(topSplitter)
        topSplitter.SplitHorizontally(self.menuPanel,vSplitter)
        topSplitter.SetMinimumPaneSize(120)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(topSplitter, 1, wx.EXPAND)
        self.SetSizer(sizer)

        self.menuPanel.ShowMenuPanel()
        self.lateralPanel.ShowMenuPanel()
        """
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.TimeInterval, self.timer)
        self.timer.Start(1000)
        """    

        self.Bind(wx.EVT_BUTTON, self.OnButtonClickAbrir, self.menuPanel.AbrirButton()) 
        self.Bind(wx.EVT_BUTTON, self.OnButtonClickFiltrar, self.menuPanel.FiltrarButton()) 


    def OnButtonClickAbrir(self, event):
        requests.get('http://localhost:3000/selena/localTable/')
        OnOpen(self)
        self.Refresh()
        self.Run()
    def OnButtonClickFiltrar(self, event):
        print("FILTRANDO")
        print(self.menuPanel.GetCategoria())
        print(self.menuPanel.GetSeleccion())
        request = requests.get('http://localhost:3000/selena/filtro/'+self.menuPanel.GetCategoria()+"/"+self.menuPanel.GetSeleccion())
        request = request.json()
        aux = request
        request = []
        for i in aux:
            request.append(i['id'])
        print(request)
        path = './'+self.menuPanel.GetCategoria()+"_"+self.menuPanel.GetSeleccion()
        if not os.path.exists(path):
            os.makedirs(path)
        newPhoto = self.imagePanel.photos
        filtro = []
        for i in request:
            for j in range(0,len(newPhoto)):
                if((i-1) == j):
                    filtro.append(self.imagePanel.photos[j])
        for i in filtro :
            shutil.copy(i, path)


    def Run(self):
        self.imagePanel.SetLateralPanel(self.lateralPanel)
        photos = glob.glob(os.path.join(PathFile(), '*.jpg'))
        self.imagePanel.photos = photos
        if photos:
            self.imagePanel.update_photo(photos[0])
            self.imagePanel.total_photos = len(photos)
        else:
            self.imagePanel.reset()
        
        for i in photos:
            text = Work(i)
            self.genero = requests.get('http://localhost:3000/selena/revisarCoincidencia/'+text)
        self.menuPanel.FillComboBox('')
           


    
if __name__ == "__main__":
    app = wx.App()
    frame = Main()
    frame.Show()
    app.MainLoop()

