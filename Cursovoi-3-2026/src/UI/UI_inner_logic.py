import tkinter as tk
from tkinter import ttk
from typing import Any


class UIInnerLogic:
    """Здесь находится начинка (сырая реализация) для интерфейся

    Расположены следующие функции:

    Создание кнопки:
    make_button(self, coord: tuple(int, int)=(0.5, 0,5), text: str = "unk", func: Callable = None):
        По входным параметрам понятно, что создаёт кнопку на определённом месте и записывает туда текст с функцией
        Помимо прочего эта функция и нижеописанные сами управляют своим обновлением и прочим

    """
    def __init__(self, title: str, size: tuple[int, int]):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{size[0]}x{size[1]}")

        # Сюда записываются удалённые номера элементов, чтобы их использовали в первую очередь
        # Порядка нет, номера не по возрастанию/убыванию
        self._empty_nums: list[int] = []
        # Сюда под определённым номером записывают элемент
        self._elements: dict[int: Any] = {}
        self._counter = self._counter_for_id()


    @staticmethod
    def _counter_for_id():
        i = 0
        while True:
            yield i := i + 1

    def _add_element_to_dict(self, element: Any) -> int:
        """Добавляет элемент в словарь и возвращает его номер"""
        if self._empty_nums:
            num = self._empty_nums.pop(0)
        else:
            num = next(self._counter)
        self._elements[num] = element
        return num

    def _delete_element_from_dict(self, num: int):
        """Удаляет элемент из словаря и освобождает идентификатор"""
        if num in self._elements:
            self._elements[num].destroy()  # удаляем виджет из интерфейса
            del self._elements[num]
            self._empty_nums.append(num)

    def run(self):
        """Запуск интерфейса Tkinter."""
        self.root.mainloop()

    def destroy_all(self):
        """Удаляет все элементы из интерфейса."""
        for num in list(self._elements.keys()):
            self._delete_element_from_dict(num)
