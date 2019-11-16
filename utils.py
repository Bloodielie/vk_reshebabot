import vk_api, json
from vk_api.bot_longpoll import VkBotLongPoll
from keybord import keyboard
from config import token, group_id

def vk_run(recovery = None):
    vk_session = vk_api.VkApi(token = token)
    longpoll = VkBotLongPoll(vk_session, group_id)
    vk = vk_session.get_api()
    if recovery is not None:
        return vk
    else:
        return [vk, longpoll]

vk = vk_run("return")

class Vk_tools:
    def __init__(self):
        self.upload = vk_api.VkUpload(vk)

    def create_attachment(self, folder, type_, section=None, nomer_id=None, name=None):
        if section is not None:
            photo = self.upload.photo_messages(f'{folder}/{section}.{nomer_id}.jpg')
        elif name is not None:
            photo = self.upload.photo_messages(f'{folder}/{name}.jpg')
        else:
            photo = self.upload.photo_messages(f'{folder}/{nomer_id}.jpg')

        owner_id = photo[0]['owner_id']
        photo_id = photo[0]['id']
        access_key = photo[0]['access_key']
        return f'{type_}{owner_id}_{photo_id}_{access_key}'

    def check_payload(self, event, payloadd:list=None):
        if payloadd is not None:
            ferst_payload = []
            for payload in payloadd:
                pay = payload
                p = payload.split("|")
                if p[1] == str(event.obj.from_id):
                    payloadd.remove(pay)
                else:
                    ferst_payload.append(payload)
            return ferst_payload
        else:
            return []