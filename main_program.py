# -*- coding: utf-8 -*-
# Authors: Nurdan Karapınar
"""
Created on Thu Sep  3 09:25:37 2015

"""
import os
import shutil
import time
from tkinter.filedialog import askopenfilenames,askopenfilename
from tkinter.messagebox import askquestion,showwarning
from configparser import ConfigParser

try:
    # Python3 için
    import tkinter as tk
    
except ImportError:
    # Python2 için
    import Tkinter as tk

# Çalışmaların kaydedileceği klasör
if not os.path.isdir("A-Track"):
    os.makedirs("A-Track")
timestr = time.strftime("%Y%m%d-%H%M%S")
os.makedirs("A-Track/"+ timestr)

Dir= "A-Track/"+timestr+"/"+timestr
image_file = open(Dir+".txt","w")

config = ConfigParser()

if os.path.exists('./atrack.config'):
    config.read('./atrack.config')

else:
    print('Python cannot open the configuration file. Make sure atrack.config',
          'is in the same folder as atrack.py.')
    raise SystemExit
    
#==============================================================================
# FONKSİYONLAR
#==============================================================================
# 1.sayfa fonksiyonları
    
Image_list=[]

def import_file():
    Formats = [
    ('text files', '.txt'),
    ('All files ','*')
    ]
    Image_list = askopenfilename(parent = root_window,filetypes=Formats)
    list_box = tk.Listbox(first_frame,selectmode = "SINGLE")
    list_box.place(relx = 0.05,rely = 0.07,width=600, height=350)
    
    Image_list = open(Image_list)
    Image_list = Image_list.read()
    Image_list = Image_list.split()
    for i in Image_list:
        list_box.insert(tk.END,i)


def load_file():
    #dosya yükleme
    global list_box,Image_list,Images
    Formats = [
    ('Flexible Image Transport System','*.fits'),
    ('All files ','*')
    ]
    Image_list = askopenfilenames(parent = root_window, filetypes=Formats)
    Images = len(Image_list)
    
    if Images >= 3:
        Images = Image_list
        list_box = tk.Listbox(first_frame,selectmode = "SINGLE")
        list_box.place(relx = 0.05,rely = 0.07,width=600, height=350)
        for i in Images:
            list_box.insert(tk.END, str(i)+"\n")
    elif Images <3:
      showwarning( "Open file",\
        "Please,select 3-15 ımage")

def delete_file():
    items = list_box.curselection()
    pos = 0
    for i in items :
        idx = int(i) - pos
        list_box.delete( idx,idx )
        pos = pos + 1

        # 2.sayfa fonksiyonları

def default_get_parameter():
    config = ConfigParser()
    if os.path.exists('./default.config'):
        config.read('./default.config')
    else:
        print('Python cannot open the configuration file.' +
              ' Make sure default.config',
              'is in the same folder as atrack.py.')
        raise SystemExit
        
    ent1.delete(0,tk.END)
    ent2.delete(0,tk.END)
    ent3.delete(0,tk.END)
    ent4.delete(0,tk.END)
    ent5.delete(0,tk.END)
    ent6.delete(0,tk.END)
    ent7.delete(0,tk.END)
    ent8.delete(0,tk.END)
    ent9.delete(0,tk.END)
    ent10.delete(0,tk.END)
    ent11.delete(0,tk.END)
    ent12.delete(0,tk.END)
    ent13.delete(0,tk.END)
    ent14.delete(0,tk.END)
    ent15.delete(0,tk.END)
    ent16.delete(0,tk.END)
    ent17.delete(0,tk.END)
    ent18.delete(0,tk.END)
    ent19.delete(0,tk.END)
    ent20.delete(0,tk.END)
    ent21.delete(0,tk.END)
    ent22.delete(0,tk.END)
    ent23.delete(0,tk.END)
    ent24.delete(0,tk.END)
    ent25.delete(0,tk.END)
    ent1.insert(0,config.get("sources", "DETECT_THRESH"))
    ent2.insert(0,config.get("sources", "ANALYSIS_THRESH"))
    ent3.insert(0,config.get("sources", "DETECT_MINAREA"))
    ent4.insert(0,config.get("sources", "PIXEL_SCALE"))
    ent5.insert(0,config.get("sources", "SEEING_FWHM"))
    ent6.insert(0,config.get("sources", "PHOT_AUTOPARAMS"))
    ent7.insert(0,config.get("sources", "BACK_SIZE"))
    ent8.insert(0,config.get("sources", "BACK_FILTERSIZE"))
    ent9.insert(0,config.get("sources", "DEBLEND_NTHRESH"))
    ent10.insert(0,config.get("sources", "SATUR_LEVEL"))
    ent11.insert(0,config.get("sources", "DEBLEND_MINCONT"))
    ent12.insert(0,config.get("sources", "GAIN"))
    ent13.insert(0,config.get("sources", "rerun"))
    ent14.insert(0,config.get("sources", "keepcat"))
    ent15.insert(0,config.get("sources", "verbose"))
    ent16.insert(0,config.get("asteroids", "FWHM_MIN"))
    ent17.insert(0,config.get("asteroids", "FLUX_MAX"))
    ent18.insert(0,config.get("asteroids", "ELONGATION_MAX"))
    ent19.insert(0,config.get("asteroids", "SNR_MIN"))
    ent20.insert(0,config.get("asteroids", "TRAVEL_MIN"))
    ent21.insert(0,config.get("asteroids", "HEIGHT_MAX"))
    ent22.insert(0,config.get("asteroids", "SCALE"))
    ent23.insert(0,config.get("asteroids", "V_MAX"))
    ent24.insert(0,config.get("asteroids", "TOLERANCE"))
    ent25.insert(0,config.get("asteroids", "SPEED_MIN"))

# 3.sayfa fonksiyonları

command= "python3 atrack.py"

def align_function():
    global command
# skip alignment if alignment is already done
    command += " --skip-align"
    
    
def cats_function():
    global command
# skip creating catalog files if they are already created
    command += " --skip-cats"
    
    
def PNGs_function():
    global command
# skip creating PNGs
    command += " --skip-pngs"
    
    
def Gif_function():
    global command
# skip creating animation file
    command += " --skip-gif"
    
    
def third_help_function():
    help_frame_label_answer = tk.Label(help_frame,text = "")
    
    help_frame_label_answer.place(relx = 0.25,rely = 0.10)
    
    first_frame.place_forget()
    second_frame.place_forget()
    third_frame.place_forget()
    help_frame.place(relx = 0.0,rely = 0.0,width=500, height=500)
    
    help_frame_back_button = tk.Button(help_frame, text = "Back",
                                          command = call_third_frame_on_top)
    help_frame_back_button.place(relx =0.75,rely=0.95)     

# 4.sayfa fonksiyonları

def fourth_help_function():
    help_frame_label_answer = tk.Label(help_frame,text = "")
    
    help_frame_label_answer.place(relx = 0.25,rely = 0.10)
    
    first_frame.place_forget()
    second_frame.place_forget()
    third_frame.place_forget()
    help_frame.place(relx = 0.0,rely = 0.0,width=500, height=500)
    
    help_frame_back_button = tk.Button(help_frame, text = "Back",
                                       command = call_fourth_frame_on_top)
    help_frame_back_button.place(relx =0.75,rely=0.95)     

def result_function():
    dirname, filename = os.path.split(os.path.abspath(__file__))
    os.system("gedit " + dirname + "/A-Track/" + timestr + "/atrack"+"/results.txt")
    SystemExit

# Her sayfada olan fonksiyonlar

def quit_function():
    # quit butonu işlevi
    answer = askquestion(title= ' Really quit? ' , 
                         message= ' Are you sure quit? ' )
    if answer== 'yes':
        root_window.destroy()

#==============================================================================
# Penceler ve özellikleri
#==============================================================================

def create_widgets_in_first_frame():
    global add_file,remove_file,list_box,import_file
    # Giriş penceresi
    first_window_label = tk.Label(first_frame, 
                                      text='STEP1 : IMAGE SELECTION',
                                      font=("Helvetica", 8))
    first_window_label.place(relx = 0.05,rely = 0.0)
    # Girişteki butonlar
    first_window_quit_button = tk.Button(first_frame, text = "Quit",
                                         command = quit_function)
    first_window_quit_button.place(relx = 0.10,rely = 0.95)
    first_window_next_button = tk.Button(first_frame, text = "Next",
                                         command = call_second_frame_on_top)
    first_window_next_button.place(relx = 0.88,rely = 0.95)
    remove_file = tk.Button(first_frame,text = "REMOVE FILE",
                            command = delete_file,font=("Helvetica", 8))
    remove_file.place(relx = 0.54,rely = 0.82)
    add_file = tk.Button(first_frame,text = "ADD FILE",
                         command = load_file,font=("Helvetica", 8))
    add_file.place(relx = 0.80,rely = 0.82)
    import_file = tk.Button(first_frame,
                            text = "IMPORT FILE",
                            command = import_file,font=("Helvetica", 8))
    import_file.place(relx = 0.30,rely = 0.82)
    
    list_box = tk.Listbox(first_frame)
    list_box.place(relx = 0.05,rely = 0.07,width=600, height=350)


def create_widgets_in_second_frame():
    global ent1,ent2,ent3,ent4,ent5,ent6,ent7,ent8,ent9,ent10,ent11,\
           ent12,ent13,ent14,ent15,ent16,ent17,ent18,ent19,ent20,ent21,ent22,\
           ent23,ent24,ent25
    
    # Parametreler Penceresi
    second_window_label = tk.Label(second_frame, text='STEP 2 : PARAMETERS ',
                                   font=("Helvetica", 8))
    second_window_label.place(relx = 0.05,rely = 0.0)

    second_window_back_button = tk.Button(second_frame, text = "Back", 
                                          command = call_first_frame_on_top)
    second_window_back_button.place(relx =0.75,rely=0.960)
    second_window_next_button = tk.Button(second_frame, text = "Next",
                                          command = call_third_frame_on_top)
    second_window_next_button.place(relx =0.88,rely=0.960)
    second_window_cancel_button = tk.Button(second_frame, text = "Quit",
                                            command = quit_function)
    second_window_cancel_button.place(relx = 0.05,rely = 0.960)
     
    default_button = tk.Button(second_frame, text = "DEFAULT", 
                               command = default_get_parameter,
                               font=("Helvetica", 8))
    default_button.place(relx =0.4,rely=0.960)
# SExtractor ve A-Track parametreleri
    
    lbl1 = tk.Label(second_frame,text="DETECT_THRESH",font=("Helvetica", 8))
    lbl1.place(relx=0.0,rely=0.0368)
    ent1 = tk.Entry(second_frame)
    ent1.place(relx=0.4,rely=0.0368,width=100)
    ent1.insert(0,config.get("sources","DETECT_THRESH"))
    main_1 = tk.Label(second_frame,text = "1-3 (sigma)")
    main_1.place(relx=0.7,rely=0.0368)

    lbl2 = tk.Label(second_frame,text ="ANALYSIS_THRESH",font=("Helvetica", 8))
    lbl2.place(relx =0.0,rely=0.0736)
    ent2 = tk.Entry(second_frame)
    ent2.place(relx =0.4,rely=0.0736,width=100)
    ent2.insert(0,config.get("sources","ANALYSIS_THRESH"))
    main_2 = tk.Label(second_frame,text = "integer (n ≤ 32)")
    main_2.place(relx =0.7,rely=0.0736)

    lbl3 = tk.Label(second_frame,text="DETECT_MINAREA",font=("Helvetica", 8))
    lbl3.place(relx =0.0,rely=0.1104)
    ent3 = tk.Entry(second_frame)
    ent3.place(relx =0.4,rely=0.1104,width=100)
    ent3.insert(0,config.get("sources","DETECT_MINAREA"))
    main_3 = tk.Label(second_frame,text = "3-50")
    main_3.place(relx =0.7,rely=0.1104)

    lbl4 = tk.Label(second_frame,text="PIXEL_SCALE",font=("Helvetica", 8))
    lbl4.place(relx =0.0,rely=0.1472)
    ent4 = tk.Entry(second_frame)
    ent4.place(relx =0.4,rely=0.1472,width=100)
    ent4.insert(0,config.get("sources","PIXEL_SCALE"))
    main_4 = tk.Label(second_frame,text = "arcsec")
    main_4.place(relx =0.7,rely=0.1472)

    lbl5 = tk.Label(second_frame,text="SEEING_FWHM",font=("Helvetica", 8))
    lbl5.place(relx =0.0,rely=0.184)
    ent5 = tk.Entry(second_frame)
    ent5.place(relx =0.4,rely=0.184,width=100)
    ent5.insert(0,config.get("sources","SEEING_FWHM"))
    main_5 = tk.Label(second_frame,text = "arcsec")
    main_5.place(relx =0.7,rely=0.184)

    lbl6 = tk.Label(second_frame,text="PHOT_AUTOPARAMS",font=("Helvetica", 8))
    lbl6.place(relx =0.0,rely=0.2208)
    ent6 = tk.Entry(second_frame)
    ent6.place(relx =0.4,rely=0.2208,width=100)
    ent6.insert(0,config.get("sources","PHOT_AUTOPARAMS"))
    main_6 = tk.Label(second_frame,text = "min_radius")
    main_6.place(relx =0.7,rely=0.2208)

    lbl7 = tk.Label(second_frame,text="BACK_SIZE",font=("Helvetica", 8))
    lbl7.place(relx =0.0,rely=0.2576)
    ent7 = tk.Entry(second_frame)
    ent7.place(relx =0.4,rely=0.2576,width=100)
    ent7.insert(0,config.get("sources","BACK_SIZE"))
    main_7 = tk.Label(second_frame,text = "<width>,<height>")
    main_7.place(relx =0.7,rely=0.2576)

    lbl8 = tk.Label(second_frame,text="BACK_FILTERSIZE",
                    font=("Helvetica", 8))
    lbl8.place(relx =0.0,rely=0.2944)
    ent8 = tk.Entry(second_frame)
    ent8.place(relx =0.4,rely=0.2944,width=100)
    ent8.insert(0,config.get("sources","BACK_FILTERSIZE"))
    main_8 = tk.Label(second_frame,text = "<width>,<height>")
    main_8.place(relx =0.7,rely=0.2944)

    lbl9 = tk.Label(second_frame,text="DEBLEND_NTHRESH",
                    font=("Helvetica", 8))
    lbl9.place(relx =0.0,rely=0.3312)
    ent9 = tk.Entry(second_frame)
    ent9.place(relx =0.4,rely=0.3312,width=100)
    ent9.insert(0,config.get("sources","DEBLEND_NTHRESH"))
    main_9 = tk.Label(second_frame,text = "arcsec")
    main_9.place(relx =0.7,rely=0.3312)

    lbl10 = tk.Label(second_frame,text="SATUR_LEVEL",
                     font=("Helvetica", 8))
    lbl10.place(relx =0.0,rely=0.368)
    ent10 = tk.Entry(second_frame)
    ent10.place(relx =0.4,rely=0.368,width=100)
    ent10.insert(0,config.get("sources","SATUR_LEVEL"))
    main_10 = tk.Label(second_frame,text = "ADU")
    main_10.place(relx =0.7,rely=0.368)

    lbl11 = tk.Label(second_frame,text="DEBLEND_MINCONT",
                     font=("Helvetica", 8))
    lbl11.place(relx =0.0,rely=0.4048)
    ent11 = tk.Entry(second_frame)
    ent11.place(relx =0.4,rely=0.4048,width=100)
    ent11.insert(0,config.get("sources","DEBLEND_MINCONT"))
    main_11 = tk.Label(second_frame,text = "arcsec")
    main_11.place(relx =0.7,rely=0.4048)

    lbl12 = tk.Label(second_frame,text="GAIN",
                     font=("Helvetica", 8))
    lbl12.place(relx =0.0,rely=0.4416)
    ent12 = tk.Entry(second_frame)
    ent12.place(relx =0.4,rely=0.4416,width=100)
    ent12.insert(0,config.get("sources","GAIN"))
    main_12 = tk.Label(second_frame,text = "e-/ADU")
    main_12.place(relx =0.7,rely=0.4416)
    
    lbl13 = tk.Label(second_frame,text="rerun",
                     font=("Helvetica", 8))
    lbl13.place(relx =0.0,rely=0.4784)
    ent13 = tk.Entry(second_frame)
    ent13.place(relx =0.4,rely=0.4784,width=100)
    ent13.insert(0,config.get("sources","rerun"))
    main_13 = tk.Label(second_frame,text = "True or False")
    main_13.place(relx =0.7,rely=0.4784)
    
    lbl14 = tk.Label(second_frame,text="keepcat",
                     font=("Helvetica", 8))
    lbl14.place(relx =0.0,rely=0.5152)
    ent14 = tk.Entry(second_frame)
    ent14.place(relx =0.4,rely=0.5152,width=100)
    ent14.insert(0,config.get("sources","keepcat"))
    main_14 = tk.Label(second_frame,text = "True or False")
    main_14.place(relx =0.7,rely=0.5152)
    
    lbl15 = tk.Label(second_frame,text="verbose",
                     font=("Helvetica", 8))
    lbl15.place(relx =0.0,rely=0.552)
    ent15 = tk.Entry(second_frame)
    ent15.place(relx =0.4,rely=0.552,width=100)
    ent15.insert(0,config.get("sources","verbose"))
    main_15 = tk.Label(second_frame,text = "True or False")
    main_15.place(relx =0.7,rely=0.552)
    
    lbl16 = tk.Label(second_frame,text="FWHM_MIN",
                     font=("Helvetica", 8))
    lbl16.place(relx =0.0,rely=0.5888)
    ent16 = tk.Entry(second_frame)
    ent16.place(relx =0.4,rely=0.5888,width=100)
    ent16.insert(0,config.get("asteroids","FWHM_MIN"))
    main_16 = tk.Label(second_frame,text = "float")
    main_16.place(relx =0.7,rely=0.5888)

    lbl17 = tk.Label(second_frame,text="FLUX_MAX",
                     font=("Helvetica", 8))
    lbl17.place(relx =0.0,rely=0.6256)
    ent17 = tk.Entry(second_frame)
    ent17.place(relx =0.4,rely=0.6256,width=100)
    ent17.insert(0,config.get("asteroids","FLUX_MAX"))
    main_17 = tk.Label(second_frame,text = "integer")
    main_17.place(relx =0.7,rely=0.6256)

    lbl18 = tk.Label(second_frame,text="ELONGATION_MAX",
                     font=("Helvetica", 8))
    lbl18.place(relx =0.0,rely=0.6624)
    ent18 = tk.Entry(second_frame)
    ent18.place(relx =0.4,rely=0.6624,width=100)
    ent18.insert(0,config.get("asteroids","ELONGATION_MAX"))
    main_18 = tk.Label(second_frame,text = "integer")
    main_18.place(relx =0.7,rely=0.6624)

    lbl19 = tk.Label(second_frame,text="SNR_MIN",
                     font=("Helvetica", 8))
    lbl19.place(relx =0.0,rely=0.6993)
    ent19 = tk.Entry(second_frame)
    ent19.place(relx =0.4,rely=0.6993,width=100)
    ent19.insert(0,config.get("asteroids","SNR_MIN"))
    main_19 = tk.Label(second_frame,text = "integer")
    main_19.place(relx =0.7,rely=0.6993)

    lbl20 = tk.Label(second_frame,text="TRAVEL_MIN",
                     font=("Helvetica", 8))
    lbl20.place(relx =0.0,rely=0.736)
    ent20 = tk.Entry(second_frame)
    ent20.place(relx =0.4,rely=0.736,width=100)
    ent20.insert(0,config.get("asteroids","TRAVEL_MIN"))
    main_20 = tk.Label(second_frame,text = "pixelscale")
    main_20.place(relx =0.7,rely=0.736)

    lbl21 = tk.Label(second_frame,text="HEIGHT_MAX")
    lbl21.place(relx =0.0,rely=0.7728)
    ent21 = tk.Entry(second_frame)
    ent21.place(relx =0.4,rely=0.7728,width=100)
    ent21.insert(0,config.get("asteroids","HEIGHT_MAX"))
    main_21 = tk.Label(second_frame,text = "floats")
    main_21.place(relx =0.7,rely=0.7728)

    lbl22 = tk.Label(second_frame,text="SCALE",
                     font=("Helvetica", 8))
    lbl22.place(relx =0.0,rely=0.8096)
    ent22 = tk.Entry(second_frame)
    ent22.place(relx =0.4,rely=0.8096,width=100)
    ent22.insert(0,config.get("asteroids","SCALE"))
    main_22 = tk.Label(second_frame,text = "ﬂoats")
    main_22.place(relx =0.7,rely=0.8096)

    lbl23 = tk.Label(second_frame,text="V_MAX",
                     font=("Helvetica", 8))
    lbl23.place(relx =0.0,rely=0.8464)
    ent23 = tk.Entry(second_frame)
    ent23.place(relx =0.4,rely=0.8464,width=100)
    ent23.insert(0,config.get("asteroids","V_MAX"))
    main_23 = tk.Label(second_frame,text = "px/min")
    main_23.place(relx =0.7,rely=0.8464)

    lbl24 = tk.Label(second_frame,text="TOLERANCE",
                     font=("Helvetica", 8))
    lbl24.place(relx =0.0,rely=0.8832)
    ent24 = tk.Entry(second_frame)
    ent24.place(relx =0.4,rely=0.8832,width=100)
    ent24.insert(0,config.get("asteroids","TOLERANCE"))
    main_24 = tk.Label(second_frame,text = "ﬂoats")
    main_24.place(relx =0.7,rely=0.8832)

    lbl25 = tk.Label(second_frame,text="SPEED_MIN",
                     font=("Helvetica", 8))
    lbl25.place(relx =0.0,rely=0.92)
    ent25 = tk.Entry(second_frame)
    ent25.place(relx =0.4,rely=0.92,width=100)
    ent25.insert(0,config.get("asteroids","SPEED_MIN"))
    main_25 = tk.Label(second_frame,text = "px/min")
    main_25.place(relx =0.7,rely=0.92)
     
def create_widgets_in_third_frame():
    # Create the label for the frame
    third_window_label = tk.Label(third_frame, text='STEP 3 : SECTİON STEPS',
                                  font=("Helvetica", 8))
    third_window_label.place(relx = 0.05,rely = 0.0)
    # Create the button for the frame
    third_window_back_button = tk.Button(third_frame, text = "Back",
                                         command = call_second_frame_on_top)
    third_window_back_button.place(relx =0.73,rely=0.95)
 
    third_window_cancel_button = tk.Button(third_frame, text = "Quit",
                                           command = quit_function)
    third_window_cancel_button.place(relx = 0.05,rely = 0.95)
    third_window_help_button = tk.Button(third_frame,text = "Help",
                                         command = third_help_function)
    third_window_help_button.place(relx = 0.18,rely = 0.95)
    third_window_run_button = tk.Button(third_frame,text = "RUN",
                                            command = call_fourth_frame_on_top)
                                            
    third_window_run_button.place(relx = 0.88,rely = 0.95)    
    Align = tk.Checkbutton(third_frame,text = "Skip Align ",
                           command = align_function)
    Align.place(relx =0.2,rely=0.22)

    Cats = tk.Checkbutton(third_frame,text= "Skip Cats ",
                          command = cats_function)
    Cats.place(relx =0.2,rely=0.32)
    
    PNGs = tk.Checkbutton(third_frame,text= "Skip PNGs ",
                          command = PNGs_function)
    PNGs.place(relx =0.2,rely=0.42)

    Gif = tk.Checkbutton(third_frame,text= "Skip Animated ",
                         command = Gif_function)
    Gif.place(relx =0.2,rely=0.52)


def create_widgets_in_fourth_frame():
    # Create the label for the frame
    fourth_window_label = tk.Label(fourth_frame, text='STEP 4 : RESULT FILE ',
                                   font=("Helvetica", 8))
    fourth_window_label.place(relx = 0.05,rely = 0.0)
    fourth_window_cancel_button = tk.Button(fourth_frame, text = "Quit",
                                            command = quit_function)
    fourth_window_cancel_button.place(relx = 0.05,rely = 0.95)
    fourth_window_help_button = tk.Button(fourth_frame, text = "Help",
                                            command = fourth_help_function)
    fourth_window_help_button.place(relx = 0.18,rely = 0.95)         
    fourth_window_result_button = tk.Button(fourth_frame,text = "Go To Result",
                                            command = result_function,
                                            font=("Helvetica", 8))
    fourth_window_result_button.place(relx = 0.75,rely = 0.95)


def create_widgets_in_help_frame():
     help_frame_label = tk.Label(help_frame, text='HELP')
     help_frame_label.place(relx = 0.15,rely = 0.05)
     help_frame_cancel_button = tk.Button(help_frame, text = "Quit",
                                            command = quit_function)
     help_frame_cancel_button.place(relx = 0.05,rely = 0.95)
#==============================================================================    
# Pencere çağırma fonksiyonları
#==============================================================================


def call_first_frame_on_top():
    second_frame.place_forget()
    first_frame.place(relx = 0.0,rely = 0.0,width=500, height=500)
    

def call_second_frame_on_top():
    #Daha önce çalışılmış dosyayı kullanmak için
    for img in Image_list:
        image_file.write(img+"\n")
    image_file.close()
    
    first_frame.place_forget()
    third_frame.place_forget()
    second_frame.place(relx = 0.0,rely = 0.0,width=500, height=500)
    

           
def call_third_frame_on_top():
    global ent1,ent2,ent3,ent4,ent5,ent6,ent7,ent8,ent9,ent10,ent11,\
           ent12,ent13,ent14,ent15,ent16,ent17,ent18,ent19,ent20,ent21,ent22,\
           ent23,ent24,ent25
    second_frame.place_forget()
    fourth_frame.place_forget()
    help_frame.place_forget()
    third_frame.place(relx = 0.0,rely = 0.0,width=500, height=500)
    
    config.set("sources","DETECT_THRESH",ent1.get())
    config.set("sources","ANALYSIS_THRESH",ent2.get())
    config.set("sources","DETECT_MINAREA",ent3.get())
    config.set("sources","PIXEL_SCALE",ent4.get())
    config.set("sources","SEEING_FWHM",ent5.get())
    config.set("sources","PHOT_AUTOPARAMS",ent6.get())
    config.set("sources","BACK_SIZE",ent7.get())
    config.set("sources","BACK_FILTERSIZE",ent8.get())
    config.set("sources","DEBLEND_NTHRESH",ent9.get())
    config.set("sources","SATUR_LEVEL",ent10.get())
    config.set("sources","DEBLEND_MINCONT",ent11.get())
    config.set("sources","GAIN",ent12.get())
    config.set("sources","rerun",ent13.get())
    config.set("sources","keepcat",ent14.get())
    config.set("sources","verbose",ent15.get())
    config.set("asteroids","FWHM_MIN",ent16.get())
    config.set("asteroids","FLUX_MAX",ent17.get())
    config.set("asteroids","ELONGATION_MAX",ent18.get())
    config.set("asteroids","SNR_MIN",ent19.get())
    config.set("asteroids","TRAVEL_MIN",ent20.get())
    config.set("asteroids","HEIGHT_MAX",ent21.get())
    config.set("asteroids","SCALE",ent22.get())
    config.set("asteroids","V_MAX",ent23.get())
    config.set("asteroids","TOLERANCE",ent24.get())
    config.set("asteroids","SPEED_MIN",ent25.get())
    
    with open('atrack.config', 'w') as getting:
        config.write(getting)
        
def call_fourth_frame_on_top():
    # görüntüleri kopyalama
    cmd = "A-Track/"+ timestr
    for img in Image_list:
        print(img)
        shutil.copy2(img,cmd)
    # terminalden çalıştırma
    os.system(command + " " + cmd)
    # ekranda gösterilecek sonuçlar
    list_box2 = tk.Listbox(fourth_frame,selectmode = "SINGLE")
    list_box2.place(relx = 0.05,rely = 0.07,width=600, height=350)
    dirname, filename = os.path.split(os.path.abspath(__file__))
    result = open(dirname + "/" + cmd + "/atrack"+"/results.txt")
    result = result.readlines()
    for i in result:
        list_box2.insert(tk.END,i)
    # Kullanılan görüntülerin silinmesi
    # shutil.rmtree(dirname + "/" + cmd + "/atrack")

    
    second_frame.place_forget()
    third_frame.place_forget()
    help_frame.place_forget()
    fourth_frame.place(relx = 0.0,rely = 0.0,width=500, height=500)
        

###############################
# Main program starts here #
###############################

root_window = tk.Tk()
root_window.title("   *** A-Track *** Asteroid Track ***   ")

root_w = 550
root_h = 530

root_winw = root_window.winfo_screenwidth()
root_winh = root_window.winfo_screenheight()
x = (root_winw - root_w) / 2
y = (root_winh - root_h) / 2
root_window.geometry("%dx%d+%d+%d"%(root_w, root_h, x, y))

first_frame=tk.Frame(root_window, width=500,height=500)
first_frame['borderwidth'] = 5
first_frame['relief'] = 'flat'
first_frame.place(relx =0.0,rely =0.0,width=500, height=500)

second_frame=tk.Frame(root_window, width=500, height=500)
second_frame['borderwidth'] = 5
second_frame['relief'] = 'flat'
second_frame.place(relx =0.0,rely =0.0,width=500, height=500)

third_frame=tk.Frame(root_window, width=500, height=500)
third_frame['borderwidth'] = 5
third_frame['relief'] = 'flat'
third_frame.place(relx =0.0,rely =0.0,width=500, height=500)

fourth_frame=tk.Frame(root_window, width=500, height=500)
fourth_frame['borderwidth'] = 5
fourth_frame['relief'] = 'flat'
fourth_frame.place(relx =0.0,rely =0.0,width=500, height=500)

help_frame=tk.Frame(root_window, width=500,height=500)
help_frame['borderwidth'] = 5
help_frame['relief'] = 'flat'
help_frame.place(relx =0.0,rely =0.0,width=500, height=500)

# Create all widgets to all frames
create_widgets_in_first_frame()
create_widgets_in_second_frame()
create_widgets_in_third_frame()
create_widgets_in_fourth_frame()
create_widgets_in_help_frame()


# Hide all frames in reverse order, but leave first frame visible (unhidden).
fourth_frame.place_forget()
third_frame.place_forget()
second_frame.place_forget()
help_frame.place_forget()

# Start tkinter event - loop
root_window.mainloop()
