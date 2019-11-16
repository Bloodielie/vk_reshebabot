import vk_api
from vk_api.keyboard import VkKeyboard
from vk_api.keyboard import VkKeyboardColor

class keyboard:
#payload Пример 111
#первое число номер предмета: 1)математика 2)геометрия 3)русск.яз 4)физика 5)нем.яз 6)бел.яз
#второе число номер класса

    #Клавиатура меню
    def keyboard_menu(self):
        keyboard = VkKeyboard()
        keyboard.add_button('📂 Классы', color=VkKeyboardColor.PRIMARY, payload="1")
        #keyboard.add_button('📒 Избранные', color=VkKeyboardColor.PRIMARY, payload="2")
        return keyboard.get_keyboard()

    #Клавиатура классов
    def keyboard_classes(self):
        keyboard = VkKeyboard()
        keyboard.add_button('11 Класс', color=VkKeyboardColor.DEFAULT, payload="11")
        keyboard.add_button('10 Класс', color=VkKeyboardColor.DEFAULT, payload="10")
        keyboard.add_line()
        keyboard.add_button('Меню', color=VkKeyboardColor.NEGATIVE)
        return keyboard.get_keyboard()

    #Клавиатура 11 класса
    def keyboard_classes_11(self):
        keyboard = VkKeyboard()
        keyboard.add_button('Алгебра', color=VkKeyboardColor.DEFAULT, payload="111")
        keyboard.add_button('Русский язык', color=VkKeyboardColor.DEFAULT, payload="311")
        keyboard.add_line()
        keyboard.add_button('Геометрия', color=VkKeyboardColor.DEFAULT, payload="211")
        keyboard.add_button('Физика', color=VkKeyboardColor.DEFAULT, payload="411")
        keyboard.add_line()
        keyboard.add_button('⏪ Назад', color=VkKeyboardColor.POSITIVE, payload="90")
        keyboard.add_button('Меню', color=VkKeyboardColor.NEGATIVE)
        return keyboard.get_keyboard()

    #Клавиатура 10 класса
    def keyboard_classes_10(self):
        keyboard = VkKeyboard()
        keyboard.add_button('Алгебра', color=VkKeyboardColor.DEFAULT, payload="110")
        keyboard.add_line()
        keyboard.add_button('⏪ Назад', color=VkKeyboardColor.POSITIVE, payload="90")
        keyboard.add_button('Меню', color=VkKeyboardColor.NEGATIVE)
        return keyboard.get_keyboard()

    #Клавиатура 11 класса по предметам
    def keyboard_classes_11_predmet(self):
        keyboard = VkKeyboard()
        keyboard.add_button('⏪ Назад', color=VkKeyboardColor.POSITIVE, payload="91")
        keyboard.add_button('Меню', color=VkKeyboardColor.NEGATIVE)
        return keyboard.get_keyboard()

    #Клавиатура 10 класса по предметам
    def keyboard_classes_10_predmet(self):
        keyboard = VkKeyboard()
        keyboard.add_button('⏪ Назад', color=VkKeyboardColor.POSITIVE, payload="92")
        keyboard.add_button('Меню', color=VkKeyboardColor.NEGATIVE)
        return keyboard.get_keyboard()