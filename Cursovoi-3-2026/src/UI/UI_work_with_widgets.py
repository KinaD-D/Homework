from UI.UI_inner_logic import UIInnerLogic

import tkinter as tk
from tkinter import ttk
from typing import Callable


class UIWorkWithWidgets(UIInnerLogic):
    def __init__(self, title: str = "Электросила", size: tuple[int, int] = (800, 800)):
        super().__init__(title, size)

    def make_button(
        self,
        coord: tuple[float, float] = (0.5, 0.5),
        text: str = "Button",
        func: Callable = None,
        *args
    ) -> int:
        """Создаёт кнопку и возвращает её идентификатор."""
        if func:
            command = lambda: func(*args)
        else:
            command = None

        element = ttk.Button(self.root, text=text, command=command)
        element.place(relx=coord[0], rely=coord[1], anchor=tk.CENTER)
        return self._add_element_to_dict(element)

    def make_label(
            self, coord: tuple[float, float] = (0.5, 0.5), text: str = "Label"
    ) -> int:
        element = ttk.Label(self.root, text=text)
        element.place(relx=coord[0], rely=coord[1], anchor=tk.CENTER)
        return self._add_element_to_dict(element)