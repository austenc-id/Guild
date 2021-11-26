from tkinter import *
from tkinter import ttk as gui
import functools as ft
from PIL import ImageTk, Image
from assets.build import Version


class UI:
    def root():
        root = Tk()
        root.title('MysteonDex')
        UI.rootframe = gui.Frame(root, padding="3 3 12 12")
        UI.rootframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        return root
    def versions():
        col = 1
        row = 1
        gui.Label(UI.rootframe, text='available versions: ').grid(column=col, row=row, sticky=E)
        available = ['RescueTeamDX']
        for version in available:
            col += 1
            gui.Button(UI.rootframe, text=version, command=ft.partial(UI.pokedex, version)).grid(column=col, row=row)
    def pokedex(name):
        col = 1
        row = 2
        version = Version(name)
        version.getpokemon()
        gui.Label(UI.rootframe, text=name).grid(column=col, row=row)
        col += 1
        gui.Button(UI.rootframe, text='launch', command=ft.partial(UI.pokedexframe, version.pokedex)).grid(column=col, row=row)
    def pokedexframe(pokedex):
        UI.dexframe = Toplevel(UI.rootframe)
        col = 1
        row = 1
        for pokemon in pokedex:
            gui.Button(UI.dexframe, text=pokemon.species, command=ft.partial(UI.pokemonframe, pokemon)).grid(column=col, row=row)
            col += 1
            if col >= 25:
                col = 1
                row += 1
    def pokemonframe(pokemon):
        col = 1
        row = 1
        row += 1
        UI.dexidframe = Toplevel(UI.dexframe)
        pokemonframe = UI.dexidframe
        pokemonframe.title(pokemon.dexid)
        gui.Label(pokemonframe, text='species: ').grid(column=col, row=row)
        col += 1
        gui.Label(pokemonframe, text=pokemon.species).grid(column=col, row=row)
        col -= 1
        row += 1
        gui.Label(pokemonframe, text='typing: ').grid(column=col, row=row)
        col += 1
        gui.Label(pokemonframe, text=pokemon.typing).grid(column=col, row=row)
        col -= 1
        row += 1
        gui.Label(pokemonframe, text='abilities: ').grid(column=col, row=row)
        col += 1
        gui.Label(pokemonframe, text=pokemon.abilities).grid(column=col, row=row)
        col -= 1
        row += 1
        gui.Label(pokemonframe, text='moveset: ').grid(column=col, row=row)
        col += 1
        gui.Label(pokemonframe, text=len(pokemon.moveset)).grid(column=col, row=row)
        row += 1
        gui.Button(pokemonframe, text='details').grid(column=col, row=row)
        
    
ui = UI.root()
versions = UI.versions()
ui.mainloop()