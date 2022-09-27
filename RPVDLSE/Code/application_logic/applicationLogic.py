from Code.props.props import Props
from Code.props.img import Img
import re


INTERNAL = 0
EXTERNAL = 1
NUM_IMGS_GALLERY = 12

class ApplicationLogic():
    def __init__(self, props:Props, gui):
        self.props = props
        self.gui = gui

        #image data
        self.imgs_tk = [] #Display images
        self.select_img:Img = None #Select image status

        #vars of control for gallery 
        self.lists_imgs = None #List of list // Each list is a page of gallery
        self.page = 0 #Page of gallery
        self.status_int_ext = INTERNAL #Default option: intenal imgs

        #init gallery
        self.calculate_lists_imgs()#Calculate lists_imgs
        self.set_images_gui()
        self.status_next_back_btn()
        self.disabled_bottom_btns()
    
    #Gallery methods
    def select_image(self, img_num: int):
        if(img_num == -1):
            self.select_img = None
            self.disabled_bottom_btns()
        elif(len(self.imgs_tk) >= img_num):
            self.select_img = self.imgs_tk[img_num-1]
            self.enable_bottom_btns()
        else:
            self.select_img = None
            self.disabled_bottom_btns()
            print("Error") #catch error / no deberia pasar

    def turn_page(self):
        self.page += 1
        self.calculate_lists_imgs()
        self.repaint()

    def return_page(self):
        self.page -= 1
        self.calculate_lists_imgs()
        self.repaint()

    def set_images_gui(self):
        self.list_tk()
        self.gui.frame_tab_gallery.set_images(self.imgs_tk)
    
    def calculate_lists_imgs (self):
        if(self.status_int_ext == 0):
            self.lists_imgs = self.partition(self.props.get_imgs_internal(),
                                             NUM_IMGS_GALLERY)
        else:
            self.lists_imgs = self.partition(self.props.get_imgs_external(),
                                             NUM_IMGS_GALLERY)
    
    def list_tk(self):
        self.imgs_tk.clear()
        if(self.page > (len(self.lists_imgs) - 1)):#Delete last image in page
                self.page = len(self.lists_imgs) - 1

        if(len(self.lists_imgs) > 0):
            for img in self.lists_imgs[self.page]:
                self.imgs_tk.append(Img(img, self.status_int_ext))

    def status_next_back_btn(self):
        if(self.page == 0):
            self.gui.frame_tab_gallery.disabled_btn_back()
        else:
            self.gui.frame_tab_gallery.enable_btn_back()

        if((self.page == (len(self.lists_imgs) - 1)) or 
           (len(self.lists_imgs) == 0)):
            self.gui.frame_tab_gallery.disabled_btn_next()
        else:
            self.gui.frame_tab_gallery.enable_btn_next()

    def set_ext_mode(self):
        self.status_int_ext = EXTERNAL

    def set_int_mode(self):
        self.status_int_ext = INTERNAL

    def update_gallery(self):
        self.lists_imgs = None #List of list // Each list is a page of gallery
        self.page = 0 #Page of gallery
        self.calculate_lists_imgs()#Calculate lists_imgs
        self.repaint()

    def repaint(self):
        self.set_images_gui()
        self.status_next_back_btn()

    def get_empty_img(self):
        return self.props.get_empty(self.status_int_ext)

    def open_select_img(self):
        successfull = self.select_img.open_image()
        return successfull

    def disabled_bottom_btns(self):
        self.gui.frame_tab_gallery.disabled_btn_open()
        self.gui.frame_tab_gallery.disabled_btn_delete()
        self.gui.frame_tab_gallery.disabled_btn_rename()
        self.gui.frame_tab_gallery.disabled_btn_recognize()

    def enable_bottom_btns(self):
        self.gui.frame_tab_gallery.enable_btn_open()
        self.gui.frame_tab_gallery.enable_btn_delete()
        self.gui.frame_tab_gallery.enable_btn_rename()
        self.gui.frame_tab_gallery.enable_btn_recognize()

    def delete_img_select(self):
        successfull = self.select_img.delete_image()
        return successfull

    def update_gallery_page(self, page):
        self.lists_imgs = None #List of list // Each list is a page of gallery
        self.page = page #Page of gallery
        self.calculate_lists_imgs()#Calculate lists_imgs
        self.repaint()

    def get_name_select_img(self):
        return self.select_img.name

    def change_name_select_img(self, new_name):
        successfull = self.select_img.rename_image(new_name)
        return successfull

    def is_raname_valid(self, new_name):
        if(re.match("^[A-Za-z0-9_-]+$", new_name)):
            return True
        else:
            return False

    #Results methods

    #other methods
    def partition(self, lst, size):
        list_of_lists = []
        for i in range(0, len(lst), size):
            list = lst[i : i+size]
            list_of_lists.append(list)
        return list_of_lists

