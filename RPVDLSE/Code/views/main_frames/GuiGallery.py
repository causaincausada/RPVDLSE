from ctypes import sizeof
import os
import sys
import tkinter as tk 
from tkinter import DISABLED, NORMAL, ttk
from typing import List
from Code.views.others.Language import Language
from Code.views.others.Messages import Messages
from Code.views.others.GuiCamera import GuiCamera
from Code.props.Img import Img

DEFAULT_SIZE_RADIO_BUTTON = 15

class GuiGallery(ttk.Frame):
    def __init__(self, root):
        super().__init__(root.tab_control)
        #radio_button select var 
        self.selected_radio_button = tk.StringVar()
        #gui elements list
        self.btns_imgs = []
        self.l_imgs = []
        #Language and Messages
        self.root = root
        self.language = Language()
        self.messages = Messages(root.numlanguage)
        self.language.languageChange(root.numlanguage)

        #Style
        style = ttk.Style()
        style.configure('Big.TRadiobutton', 
                        font=(None, DEFAULT_SIZE_RADIO_BUTTON))

        #Layout Management: Grid
        #Configure the grid
        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 9)
        self.rowconfigure(2, weight = 1)


        #Frame Up
        #Layout Management: Place
        frame_up = ttk.Frame(self)
        frame_up.grid(column=0, row=0, sticky='NEWS')

        #Buttons Frame Up: Control of Gallery
        path = os.path.dirname(__file__)
        filename = os.path.join(path, '../../../media/back.png')
        #icons
        self.back_icon = tk.PhotoImage(file=filename)
        filename = os.path.join(path, '../../../media/next.png')
        self.next_icon = tk.PhotoImage(file=filename)
        filename = os.path.join(path, '../../../media/update.png')
        self.update_icon = tk.PhotoImage(file=filename)
        filename = os.path.join(path, '../../../media/camera.png')
        self.camera_icon = tk.PhotoImage(file=filename)

        self.btn_back = ttk.Button(frame_up, image=self.back_icon, 
                                   command = self.click_btn_back)
        self.btn_next = ttk.Button(frame_up, image=self.next_icon, 
                                   command = self.click_btn_next)
        self.btn_update = ttk.Button(frame_up, image=self.update_icon, 
                                     command = self.click_btn_update)
        self.btn_camera = ttk.Button(frame_up, image=self.camera_icon, 
                                     command = self.click_btn_camera)

        #Frame RadioButton in Frame Up
        #Layout Management: Place
        frame_radio_button_ie = ttk.Frame(frame_up)
        frame_radio_button_ie.place(relx=0.75, 
                                    rely=0.0, 
                                    relheight=1, 
                                    relwidth=0.20)
        
        rb_internals = ttk.Radiobutton(frame_radio_button_ie, 
                                      text=self.language.internals,
                                      value='internal', 
                                      variable=self.selected_radio_button,
                                      command = self.click_rb_internal,
                                      style = "Big.TRadiobutton")
        rb_externals = ttk.Radiobutton(frame_radio_button_ie, 
                                      text=self.language.externals,
                                      value='external',
                                      command = self.click_rb_external,
                                      variable=self.selected_radio_button,
                                      style = "Big.TRadiobutton")
        self.selected_radio_button.set("internal") #Default option 

        #Lacation elements(Buttons and Radiobutton in Frame Up and Frame Radio)
        self.btn_back.place(relx=0.05, rely=0.0, relheight=1, relwidth=0.10)
        self.btn_next.place(relx=0.15, rely=0.0, relheight=1, relwidth=0.10)
        self.btn_update.place(relx=0.25, rely=0.0, relheight=1, relwidth=0.10)
        self.btn_camera.place(relx=0.65, rely=0.0, relheight=1, relwidth=0.10)
        rb_internals.place(relx=0.15, rely=0.00, relheight=0.5, relwidth=0.85)
        rb_externals.place(relx=0.15, rely=0.5, relheight=0.5, relwidth=0.85)

        
        #Frame Center
        #Layout Management: Place
        frame_center = ttk.Frame(self)
        frame_center.grid(column=0, row=1, sticky='NEWS')
        #Frame Middle
        #Layout Management: Grid
        frame_middle = ttk.Frame(frame_center)
        frame_middle.place(relx=0.05, rely=0.01, relheight=0.98, relwidth=0.9)
        frame_middle.config(relief="groove") #Frame outline
        frame_middle.config(padding=10)

        #Configure the grid
        frame_middle.columnconfigure(0, weight=1)
        frame_middle.columnconfigure(1, weight=1)
        frame_middle.columnconfigure(2, weight=1)
        frame_middle.columnconfigure(3, weight=1)

        frame_middle.rowconfigure(0, weight = 4)
        frame_middle.rowconfigure(1, weight = 1)
        frame_middle.rowconfigure(2, weight = 4)
        frame_middle.rowconfigure(3, weight = 1)
        frame_middle.rowconfigure(4, weight = 4)
        frame_middle.rowconfigure(5, weight = 1)

        #gallery images in buttons
        btn_img_1 = ttk.Button(frame_middle, command = self.click_btn_img_1)
        self.btns_imgs.append(btn_img_1)
        btn_img_2 = ttk.Button(frame_middle, command = self.click_btn_img_2)
        self.btns_imgs.append(btn_img_2)
        btn_img_3 = ttk.Button(frame_middle, command = self.click_btn_img_3)
        self.btns_imgs.append(btn_img_3)
        btn_img_4 = ttk.Button(frame_middle, command = self.click_btn_img_4)
        self.btns_imgs.append(btn_img_4)
        btn_img_5 = ttk.Button(frame_middle, command = self.click_btn_img_5)
        self.btns_imgs.append(btn_img_5)
        btn_img_6 = ttk.Button(frame_middle, command = self.click_btn_img_6)
        self.btns_imgs.append(btn_img_6)
        btn_img_7 = ttk.Button(frame_middle, command = self.click_btn_img_7)
        self.btns_imgs.append(btn_img_7)
        btn_img_8 = ttk.Button(frame_middle, command = self.click_btn_img_8)
        self.btns_imgs.append(btn_img_8)
        btn_img_9 = ttk.Button(frame_middle, command = self.click_btn_img_9)
        self.btns_imgs.append(btn_img_9)
        btn_img_10 = ttk.Button(frame_middle, command = self.click_btn_img_10)
        self.btns_imgs.append(btn_img_10)
        btn_img_11 = ttk.Button(frame_middle, command = self.click_btn_img_11)
        self.btns_imgs.append(btn_img_11)
        btn_img_12 = ttk.Button(frame_middle, command = self.click_btn_img_12)
        self.btns_imgs.append(btn_img_12)
        l_img_1 = ttk.Label(frame_middle, text = "Img 1")
        self.l_imgs.append(l_img_1)
        l_img_2 = ttk.Label(frame_middle, text = "Img 2")
        self.l_imgs.append(l_img_2)
        l_img_3 = ttk.Label(frame_middle, text = "Img 3")
        self.l_imgs.append(l_img_3)
        l_img_4 = ttk.Label(frame_middle, text = "Img 4")
        self.l_imgs.append(l_img_4)
        l_img_5 = ttk.Label(frame_middle, text = "Img 5")
        self.l_imgs.append(l_img_5)
        l_img_6 = ttk.Label(frame_middle, text = "Img 6")
        self.l_imgs.append(l_img_6)
        l_img_7 = ttk.Label(frame_middle, text = "Img 7")
        self.l_imgs.append(l_img_7)
        l_img_8 = ttk.Label(frame_middle, text = "Img 8")
        self.l_imgs.append(l_img_8)
        l_img_9 = ttk.Label(frame_middle, text = "Img 9")
        self.l_imgs.append(l_img_9)
        l_img_10 = ttk.Label(frame_middle, text = "Img 10")
        self.l_imgs.append(l_img_10)
        l_img_11 = ttk.Label(frame_middle, text = "Img 11")
        self.l_imgs.append(l_img_11)
        l_img_12 = ttk.Label(frame_middle, text = "Img 12")
        self.l_imgs.append(l_img_12)
        
        #Lacation elements (Buttons (images) and in Frame middle)
        btn_img_1.grid(column = 0, row = 0, sticky='NEWS')
        btn_img_2.grid(column = 1, row = 0, sticky='NEWS')
        btn_img_3.grid(column = 2, row = 0, sticky='NEWS')
        btn_img_4.grid(column = 3, row = 0, sticky='NEWS')
        btn_img_5.grid(column = 0, row = 2, sticky='NEWS')
        btn_img_6.grid(column = 1, row = 2, sticky='NEWS')
        btn_img_7.grid(column = 2, row = 2, sticky='NEWS')
        btn_img_8.grid(column = 3, row = 2, sticky='NEWS')
        btn_img_9.grid(column = 0, row = 4, sticky='NEWS')
        btn_img_10.grid(column = 1, row = 4, sticky='NEWS')
        btn_img_11.grid(column = 2, row = 4, sticky='NEWS')
        btn_img_12.grid(column = 3, row = 4, sticky='NEWS')
        l_img_1.grid(column = 0, row = 1)
        l_img_2.grid(column = 1, row = 1)
        l_img_3.grid(column = 2, row = 1)
        l_img_4.grid(column = 3, row = 1)
        l_img_5.grid(column = 0, row = 3)
        l_img_6.grid(column = 1, row = 3)
        l_img_7.grid(column = 2, row = 3)
        l_img_8.grid(column = 3, row = 3)
        l_img_9.grid(column = 0, row = 5)
        l_img_10.grid(column = 1, row = 5)
        l_img_11.grid(column = 2, row = 5)
        l_img_12.grid(column = 3, row = 5)

        #Frame Down
        #Layout Management: Place
        frame_down = ttk.Frame(self)
        #Location (Frame Down in Gallery Frame)
        frame_down.grid(column=0, row=2, sticky='NEWS')

        #Buttons Frame Down: Gallery Images Options
        btn_open = ttk.Button(frame_down, text=self.language.open, 
                              command = self.click_btn_open)
        btn_delete = ttk.Button(frame_down, text=self.language.delet,
                                command = self.click_btn_delete)
        btn_rename = ttk.Button(frame_down, text=self.language.rename,
                                command = self.click_btn_rename)
        btn_recognize = ttk.Button(frame_down, text=self.language.recognize,
                                   command = self.click_btn_recognize)

        #Lacation elements (Buttons in Frame Down)
        btn_open.place(relx=0.05, rely=0.0, relheight=1, 
                       relwidth=0.1875)
        btn_delete.place(relx=0.2875, rely=0.0, relheight=1, 
                         relwidth=0.1875)
        btn_rename.place(relx=0.525, rely=0.0, relheight=1, 
                         relwidth=0.1875)
        btn_recognize.place(relx=0.7625, rely=0.0, relheight=1, 
                            relwidth=0.1875)

    def set_images(self, images: List[Img]):
        i = 0
        for btn_img in self.btns_imgs:
            if(i < len(images)):
                btn_img.config(image = images[i].python_image)
                btn_img.config(state = NORMAL)
            else:
                btn_img.config(image = '')
                btn_img.config(state = DISABLED)
            i += 1

        i = 0
        for l_img in self.l_imgs:
            if(i < len(images)):
                l_img.config(text = images[i].name)
            else:
                l_img.config(text = "")
            i += 1

    def disabled_btn_back(self):
        self.btn_back.config(state = DISABLED)

    def enable_btn_back(self):
        self.btn_back.config(state = NORMAL)

    def disabled_btn_next(self):
        self.btn_next.config(state = DISABLED)

    def enable_btn_next(self):
        self.btn_next.config(state = NORMAL)

    def click_btn_back(self):
        self.root.appLogic.select_image(-1)
        self.root.appLogic.return_page()

    def click_btn_next(self):
        self.root.appLogic.select_image(-1)
        self.root.appLogic.turn_page()
    
    def click_btn_update(self):
        self.root.appLogic.select_image(-1)
        self.root.appLogic.update_gallery()

    def click_btn_camera(self):
        self.root.appLogic.select_image(-1)
        self.btn_camera.config(state=DISABLED)
        self.camera = GuiCamera(self)
        self.camera.initialize()
        self.camera.mainloop()
        

    def click_rb_internal(self):
        self.root.appLogic.select_image(-1)
        self.root.appLogic.set_int_mode()
        self.root.appLogic.update_gallery()


    def click_rb_external(self):
        self.root.appLogic.select_image(-1)
        self.root.appLogic.set_ext_mode()
        self.root.appLogic.update_gallery()

    def click_btn_open(self):
        print("open")

    def click_btn_delete(self):
        self.root.appLogic.select_image(-1)

    def click_btn_rename(self):
        print("rename")

    def click_btn_recognize(self):
        print("recognize")
    
    def click_btn_img_1(self):
        self.root.appLogic.select_image(1)
    
    def click_btn_img_2(self):
        self.root.appLogic.select_image(2)

    def click_btn_img_3(self):
        self.root.appLogic.select_image(3)

    def click_btn_img_4(self):
        self.root.appLogic.select_image(4)
    
    def click_btn_img_5(self):
        self.root.appLogic.select_image(5)

    def click_btn_img_6(self):
        self.root.appLogic.select_image(6)

    def click_btn_img_7(self):
        self.root.appLogic.select_image(7)
    
    def click_btn_img_8(self):
        self.root.appLogic.select_image(8)

    def click_btn_img_9(self):
        self.root.appLogic.select_image(9)

    def click_btn_img_10(self):
        self.root.appLogic.select_image(10)
    
    def click_btn_img_11(self):
        self.root.appLogic.select_image(11)

    def click_btn_img_12(self):
        self.root.appLogic.select_image(12)