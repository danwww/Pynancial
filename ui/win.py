import wx
import handlers

class WinUI(wx.Frame):
    """docstring for WinUI"""
    def __init__(self, *args, **kwargs):
        super(WinUI, self).__init__(*args, **kwargs)
        
        self.start_ui()

    def start_ui(self):

        # Create menubar
        menu_bar = wx.MenuBar()
        self.SetMenuBar(menu_bar)

        # Add File menu
        file_menu = wx.Menu()
        menu_bar.Append(file_menu, '&File')
        quit_button = file_menu.Append(wx.ID_EXIT, 'Quit', 'Quit Pynancial')

        # Add Calcs Menu
        calcs_menu = wx.Menu()
        menu_bar.Append(calcs_menu, '&Calculations')

        # Add events
        self.Bind(wx.EVT_MENU, self.OnQuit, quit_button)

        # Create sizer skeleton
        main_box = wx.BoxSizer(wx.VERTICAL)

        # Create calculator display
        calc_display = wx.BoxSizer(wx.HORIZONTAL)
        main_box.Add(calc_display, flag=wx.ALIGN_BOTTOM|wx.ALL)

        #
        # TODO: Finish bond calculator UI
        #

        self.Show(True)

    def OnQuit(self, e):
        self.Close()
        