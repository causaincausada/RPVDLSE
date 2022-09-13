from tkinter import ttk
from ttkthemes import ThemedTk
from ctypes import windll
from Code.views.main_frames.GuiGallery import GuiGallery
from Code.views.others.GuiMenuBar import GuiMenuBar
from Code.views.others.Language import Language
from Code.views.others.Messages import Messages


DEFAULT_THEME = 'adapta'
DEFAULT_WINDOW_TITLE = 'RPVDLSE'
GEOMETRY = '700x600+0+0'
MINSIZE_WINDOW_X = 700
MINSIZE_WINDOW_Y = 600
#TEXT_TAB_GALLERY = 'Galería' #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Texto Ingles/Español


class Gui(ThemedTk):
    def __init__(self):
        super().__init__()
        #Language pack
        self.numlanguage = 0
        self.language = Language()
        self.messages = Messages(self.numlanguage)
        self.language.languageChange(self.numlanguage)

        #Set window parameters
        self.set_theme(DEFAULT_THEME)
        self.geometry(GEOMETRY)
        self.minsize(MINSIZE_WINDOW_X, MINSIZE_WINDOW_Y)
        self.title(DEFAULT_WINDOW_TITLE)
        self.state('zoomed')

        #Menu bar
        self.menubar= GuiMenuBar(self)
        self.config(menu=self.menubar)
        #Tabs GUI: i.e. Gallery and Results
        self.tab_control = ttk.Notebook(self)
        self.frame_tab_gallery = GuiGallery(self) #Frame gallery
        #Poner aqui #Frame Results
        self.tab_control.add(self.frame_tab_gallery, text = self.language.galery)
        #tab_control.add(frame_tab_gallery, text ='Tab 1')
        self.tab_control.pack(expand = 1, fill ="both") #!!!!!!!!!!!!!!!!!!!!!! Ver si pack, grid o place
        
        try:
            #Configuration to Windows OS
            windll.shcore.SetProcessDpiAwareness(1)
        finally:
            pass;
    #fuction to change language
    def change_language(self, numlanguage):
        self.numlanguage = numlanguage
        self.messages = Messages(self.numlanguage)
        self.language.languageChange(self.numlanguage)
        self.menubar = GuiMenuBar(self)
        self.config(menu=self.menubar)
        self.tab_control.destroy()
        self.tab_control = ttk.Notebook(self)
        self.frame_tab_gallery= GuiGallery(self)
        self.tab_control.add(self.frame_tab_gallery, text=self.language.galery)
        self.tab_control.pack(expand = 1, fill ="both")
        
