# coding: utf-8


def get_tk(widget):
    """
    Percorrer por todos os widgets até encontrar um que seja a instancia da classe tkinter.Tk
    """
    from tkinter import Tk


    master = widget.master
    if isinstance(master, Tk):
        return master
    
    elif master is not None:
        master=get_tk(master)
    
    return master
    