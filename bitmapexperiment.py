import wx

def OnFrameClicked(e):
    print("Frame received click event")
    print(e.GetPosition())
    e.Skip()

def OnImageClicked(e):
    print("Image received click event")
    print(e.GetPosition())

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "wxStaticBitmap Experiment")
frame.Bind(wx.EVT_LEFT_DOWN, OnFrameClicked)
bmp = wx.Image('100x100.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
image = wx.StaticBitmap(frame, bitmap=bmp)
image.Bind(wx.EVT_LEFT_DOWN, OnImageClicked)
frame.Show(True)
# uncomment the next 2 lines to enable detailed inspection
#import wx.lib.inspection
#wx.lib.inspection.InspectionTool().Show()
print(wx.version())
app.MainLoop()
