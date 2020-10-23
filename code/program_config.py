# coding: utf-8

# imports
import copy
from tkinter import (Frame, LabelFrame, Toplevel,
                     Button, messagebox)
from tkinter.ttk import Notebook

from widgets import SliderInput


class Tab(Frame):
    def __init__(self, master, program, data, *args, **kwargs):
        super(Tab, self).__init__(master, *args, **kwargs)
        self.program = program
        self.data = copy.deepcopy(data)
        # ---main container
        self.main_container = Frame(self)
        self.main_container.pack(fill="both", expand=True)
        # ---buttons aply and cancel
        buttons_container = Frame(self)
        self.button_aply = Button(buttons_container, text="Aplicar")
        self.button_cancel = Button(buttons_container, text="Cancelar")
        
        buttons_container.pack(fill="x", padx=5, pady=5)
        self.button_aply.pack(side="left", fill="x", expand=True, padx=1, pady=1)
        self.button_cancel.pack(side="left", fill="x", expand=True, padx=1, pady=1)
        # ---button save
        self.button_save = Button(self, text="Salvar")
        self.button_save.pack(fill="x", padx=5, pady=5)

        # ---setting buttons
        self.button_aply["command"] = self.aply
        self.button_cancel["command"] = self.cancel
        self.button_save["command"] = self.save
        
    def aply(self):
        print("Não implementado.")
    
    def cancel(self):
        print("Não implementado.")
    
    def save(self):
        if self.program.get_style_conection().save():
            messagebox.showinfo("Aviso", "Alterações salvas. Reinicie a aplicação.")
            
        else:
            messagebox.showwarning("Aviso", "Sem permissão.")
        

class WindowTab(Tab):
    pass


class CommonFontTab(Tab):
    def __init__(self, *args, **kwargs):
        super(CommonFontTab, self).__init__(*args, **kwargs)
        # ---font size
        self.font_size = SliderInput(self.main_container, "Tamanho da fonte", 
                                     minimo=8, maximo=32)
        self.font_size.pack(fill="x", padx=5, pady=5)


class LabelTab(CommonFontTab):
    def __init__(self, *args, **kwargs):
        super(LabelTab, self).__init__(*args, **kwargs)
        # ---setting current font size
        current_font_size = self.data["label"]["font"][1]
        self.font_size.set_valor(current_font_size)

    def aply(self):
        self.data["label"]["font"][1] = self.font_size.get_valor()
        self.program.get_style_conection().set_data(self.data)
        self.program.carregar_estilo(self.program, "label")
   

class ButtonTab(CommonFontTab):
    def __init__(self, *args, **kwargs):
        super(ButtonTab, self).__init__(*args, **kwargs)
        # ---setting current font size
        current_font_size = self.data["button"]["font"][1]
        self.font_size.set_valor(current_font_size)

    def aply(self):
        self.data["button"]["font"][1] = self.font_size.get_valor()
        self.program.get_style_conection().set_data(self.data)
        self.program.carregar_estilo(self.program, "button")


class EntryTab(CommonFontTab):
    def __init__(self, *args, **kwargs):
        super(EntryTab, self).__init__(*args, **kwargs)
        # ---setting current_font_size
        current_font_size = self.data["entry"]["font"][1]
        self.font_size.set_valor(current_font_size)
    
    def aply(self):
        self.data["entry"]["font"][1] = self.font_size.get_valor()
        self.program.get_style_conection().set_data(self.data)
        self.program.carregar_estilo(self.program, "entry")


class ProgramConfig(Toplevel):
    def __init__(self, master, program, *args, **kwargs):
        super(ProgramConfig, self).__init__(master, *args, **kwargs)
        self.program = program
        self.backup = program.get_style_conection().get_data()
        # ---default window config
        self.title("Configurações")
        self.geometry("900x400")
        # ---creating tabs navegations 
        tab_navegation =  Notebook(self)
        tab_navegation.pack(fill="both", expand=True)
        
        self.window_tab = WindowTab(tab_navegation, self.program, self.backup)
        self.label_tab = LabelTab(tab_navegation, self.program, self.backup)
        self.button_tab = ButtonTab(tab_navegation, self.program, self.backup)
        self.entry_tab = EntryTab(tab_navegation, self.program, self.backup)
        
        tab_navegation.add(self.window_tab, text="Janela")
        tab_navegation.add(self.label_tab, text="Label")
        tab_navegation.add(self.button_tab, text="Botão")
        tab_navegation.add(self.entry_tab, text="Campo de texto")


if __name__ == "__main__":
    from main import Programa
    
    program = Programa()
    program.mainloop()
