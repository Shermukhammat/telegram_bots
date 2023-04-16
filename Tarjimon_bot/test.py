RAM_admes = {}

class RAM:
    def __init__(self):
        self.user_mes = dict()
        self.names = dict()
        self.langs = dict()

    def user_message(self, message, user_id = None):
        keys = list(self.user_mes.keys())

        if user_id in keys:
            self.user_mes[user_id].append(message)
        else:
            self.user_mes[user_id] = [message]

        return self.user_mes

    def get_user_message(self, user_id = None):
        keys = list(self.user_mes.keys())

        if user_id in keys:
            return self.user_mes[user_id]
        else:
            return []

    def delet_usmes(self, message, user_id = None):
        keys = list(self.user_mes.keys())

        if user_id in keys:
            array = self.user_mes[user_id]
            if message in array:
                array.remove(message)
                self.user_mes[user_id] = array

    def clear_usmes(self, user_id = None):
        keys = list(self.user_mes.keys())

        if user_id in keys:
            self.user_mes[user_id] = []
        keys = list(self.user_mes.keys())

        if user_id in keys:
            self.user_mes[user_id] = []



    def save_name(self, name, user_id = None):
        self.names[user_id] = name

    def get_name(self, user_id = None):
        keys = list(self.names.keys())

        if user_id in keys:
            return self.names[user_id]

    def save_lang(self, lang, user_id = None):
        self.langs[user_id] = lang

    def get_lang(self, user_id = None):
        keys = list(self.langs.keys())
        if user_id in keys:
            return self.langs[user_id]




if __name__ == "__main__":
    ram = RAM()
    ram.user_message("122", user_id = 12)
    ram.user_message("ola", user_id = 12)
    ram.delet_usmes("ola", user_id = 12)
    print(ram.user_message("salom", user_id = 12))