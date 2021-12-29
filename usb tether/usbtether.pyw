# -*- coding: utf-8 -*
import os
from tkinter import *
from time import sleep
def and4():
    import com
    com.command(1)
def and5():
    import com
    com.command(2)
def and6():
    import com
    com.command(3)
def and7():
    import com
    com.command(4)
def install():
    import com
    com.command(5)
def installl():
    import com
    com.command(6)
def cik():
    import com
    com.command(7)
pencere = Tk()
pencere.title("Usb Tether")
pencere.geometry("300x300")
pencere.resizable(width=FALSE, height=FALSE)
#pencere.wm_attributes("-alpha","0.5")
uyari=Label(pencere,text="Bu yazılım sadece rootlu telefonlarda çalışır\nCihazın usb hata ayıklamasını açın",
            fg="red").place(relx=0.15,rely=0.05)
çikti=Label(pencere, text="Çıktı=").place(relx=0.1,rely=0.9)
sonuc=Label(pencere, text="", fg="green").place(relx=0.3,rely=0.9)

button = Button(pencere, 
                text="---> Android 4 <---",
                command=and4).place(relx="0.06",rely="0.23")
andro4 = Button(pencere, 
                text="---> Android 5 <---",
                command=and5).place(relx="0.06",rely="0.36")
andro5 = Button(pencere, 
                text="---> Android 6 <---",
                command=and6).place(relx="0.6",rely="0.23")
andro6 = Button(pencere, 
                text="---> Android 7 <---",
                command=and7).place(relx="0.6",rely="0.36")
andro7 = Button(pencere, 
                text="------> Adb Kill <------",
                fg="red",
                command=install).place(relx="0.3",rely="0.6")
install = Button(pencere, 
                text="-> Adb Fastboot Kur <-",
                fg="green",
                command=installl).place(relx="0.3",rely="0.69")
cikk = Button(pencere, 
                text="-> Kapat <-",
                fg="red",
                command=cik).place(relx="0.4",rely="0.78")

pencere.mainloop()
