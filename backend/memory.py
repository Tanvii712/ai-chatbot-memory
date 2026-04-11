class ChatMemory:
    def __init__(self):
        self.history = []

    def add(self, user, bot):
        self.history.append({"user": user, "bot": bot})

    def get_context(self):
        context = ""
        for msg in self.history[-5:]:   # last 5 messages only
            context += f"User: {msg['user']}\nBot: {msg['bot']}\n"
        return context