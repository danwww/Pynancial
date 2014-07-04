#!/usr/bin/env python

import platform, wx
from ui import __version__ as ui_version
from library import __version__ as lib_version

VERSION = 'Pynancial v{0}/{1}'.format(lib_version, ui_version)

def main():

    def windows():
        from ui import win
        pynancial = wx.App()
        win.WinUI(None, title='Pynancial')
        pynancial.MainLoop()

    def linux():
        pass

    def osx():
        pass

    if platform.system() is 'Windows':
        windows()

    elif platform.system() is 'Linux':
        linux()

    elif platform.system() is 'Darwin':
        osx()

    else:
        print 'OS not recognized or supported'

if __name__ == '__main__':
    main()
