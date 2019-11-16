import vk_api, json, logging, datetime
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard
from vk_api.keyboard import VkKeyboardColor
from utils import Vk_tools, vk_run
from keybord import keyboard
from config import start_message

logging.basicConfig(format='%(message)s', level=logging.INFO, filename='vkbotlog.log')

longpoll = vk_run()[1]
vk = vk_run()[0]
now = datetime.datetime.now().strftime("%H:%M:%S %d.%B.%Y")

vk_utils = Vk_tools()

keybord = keyboard()

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.from_user:
                    if event.obj.text in start_message:
                        vk.messages.send(peer_id=event.object.peer_id, message="Меню", keyboard=keybord.keyboard_menu(), random_id=0)
                    elif event.obj.text == "⏪ Назад":
                        if event.obj.payload == "90":
                            vk.messages.send(peer_id=event.object.peer_id, message="Классы", keyboard=keybord.keyboard_classes(), random_id=0)
                        elif event.obj.payload == "91":
                            vk.messages.send(peer_id=event.object.peer_id, message="11 Класс", keyboard=keybord.keyboard_classes_11(), random_id=0)
                        elif event.obj.payload == "92":
                            vk.messages.send(peer_id=event.object.peer_id, message="10 Класс", keyboard=keybord.keyboard_classes_10(), random_id=0)
                    elif event.obj.payload == "1":
                        vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes(), message="Классы")
                    elif event.obj.payload == "11":
                        vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes_11(), message="11 Класс")
                    elif event.obj.payload == "10":
                        vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes_10(), message="10 Класс")
                    elif event.obj.payload == "111":
                        attachment = vk_utils.create_attachment('Обложки', 'photo', name="алгебра11")
                        vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes_11_predmet(), message="Решебник по алгебру 11 класс — Кузнецова, Шнеперман.\nУкажите номер задания.\nПример:1.55", attachment=attachment)
                        try:
                            payloadd = vk_utils.check_payload(event, payloadd)
                        except:
                            payloadd = vk_utils.check_payload(event)
                        payloadd.append(f"{event.obj.payload}|{event.obj.from_id}")
                    elif event.obj.payload == "211":
                        attachment = vk_utils.create_attachment('Обложки', 'photo', name="геометрия11")
                        vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes_11_predmet(), message="Решебник по геометрии за 11 класс — Шлыков.\nУкажите номер задания.\nПример:223", attachment=attachment)
                        try:
                            payloadd = vk_utils.check_payload(event, payloadd)
                        except:
                            payloadd = vk_utils.check_payload(event)
                        payloadd.append(f"{event.obj.payload}|{event.obj.from_id}")
                    elif event.obj.payload == "311":
                        attachment = vk_utils.create_attachment('Обложки', 'photo', name="русскяз11")
                        vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes_11_predmet(), message="Решебник по русскому языку за 11 класс — Мурина.\nУкажите номер задания.\nПример:155", attachment=attachment)
                        try:
                            payloadd = vk_utils.check_payload(event, payloadd)
                        except:
                            payloadd = vk_utils.check_payload(event)
                        payloadd.append(f"{event.obj.payload}|{event.obj.from_id}")
                    elif event.obj.payload == "411":
                        attachment = vk_utils.create_attachment('Обложки', 'photo', name="физика11")
                        vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes_11_predmet(), message="Решебник по физике 11 класс — Жилко В.В, Маркович Л.Г.\nУкажите номер задания.\nПример:5.5", attachment=attachment)
                        try:
                            payloadd = vk_utils.check_payload(event, payloadd)
                        except:
                            payloadd = vk_utils.check_payload(event)
                        payloadd.append(f"{event.obj.payload}|{event.obj.from_id}")
                    elif event.obj.payload == "211":
                        pass
                    elif event.obj.payload == "110":
                        attachment = vk_utils.create_attachment('Обложки', 'photo', name="алгебра10")
                        vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes_10_predmet(), message="Решебник по алгебрe 10 класс — Кузнецова.\nУкажите номер задания.\nПример:1.15", attachment=attachment)
                        try:
                            payloadd = vk_utils.check_payload(event, payloadd)
                        except:
                            payloadd = vk_utils.check_payload(event)
                        payloadd.append(f"{event.obj.payload}|{event.obj.from_id}")
                    elif event.obj.text.replace(".","").isdigit():
                        logging.info(f'\nPayload list{payloadd} {now}\n')
                        if int(event.obj.text[:1]) in range(10):
                            if f"111|{event.obj.from_id}" in payloadd:
                                try:
                                    nomer_id = event.obj.text[2:]
                                    section = event.obj.text[:1]
                                    attachment = vk_utils.create_attachment('Алгебра11', 'photo', section=section, nomer_id=nomer_id)
                                    vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes_11_predmet(), attachment=attachment)
                                except:
                                    vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes_11_predmet(), message='Укажите правильно номер')
                            elif f"311|{event.obj.from_id}" in payloadd:
                                try:
                                    nomer_id = event.obj.text
                                    attachment = vk_utils.create_attachment('Русскийязык11', 'photo', nomer_id=nomer_id)
                                    vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes_11_predmet(), attachment=attachment)
                                except:
                                    vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes_11_predmet(), message='Укажите правильно номер')
                            elif f"411|{event.obj.from_id}" in payloadd:
                                try:
                                    nomer_id = event.obj.text[2:]
                                    section = event.obj.text[:1]
                                    attachment = vk_utils.create_attachment('Физика11', 'photo', nomer_id=nomer_id, section=section)
                                    vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes_11_predmet(), attachment=attachment)
                                except:
                                    vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes_11_predmet(), message='Укажите правильно номер')
                            elif f"110|{event.obj.from_id}" in payloadd:
                                try:
                                    nomer_id = event.obj.text[2:]
                                    section = event.obj.text[:1]
                                    attachment = vk_utils.create_attachment('Алгебра10', 'photo', section=section, nomer_id=nomer_id)
                                    vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes_10_predmet(), attachment=attachment)
                                except:
                                    vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes_10_predmet(), message='Укажите правильно номер')
                            elif f"211|{event.obj.from_id}" in payloadd:
                                try:
                                    nomer_id = event.obj.text
                                    attachment = vk_utils.create_attachment('Геометрия11', 'photo', nomer_id=nomer_id)
                                    vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes_11_predmet(), attachment=attachment)
                                except:
                                    vk.messages.send(peer_id=event.object.peer_id, random_id=0, keyboard=keybord.keyboard_classes_11_predmet(), message='Укажите правильно номер')
    except Exception as e:
        logging.exception(f"\nException {now}")
        print(e)
        continue