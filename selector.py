import wx
import zipfile

#with zipfile.ZipFile('data.zip', 'r') as zipobj:

file_location_Input = ""

def OnOpen(self):
    global file_location_Input
    with wx.DirDialog(self, "Choose a directory", style=wx.DD_DEFAULT_STYLE) as dlg:
        if dlg.ShowModal() == wx.ID_OK:
            file_location_Input = dlg.GetPath()
    
def PathFile():
    global file_location_Input
    return file_location_Input