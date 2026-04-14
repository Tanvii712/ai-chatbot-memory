class ChatMemory:

    #creates class store chat history
    def __init__(self):
        self.short_term = []
#everytime user asks something
    def add(self, user, bot):
        self.short_term.append({"user": user, "bot": bot})
#core logic
#takes last 5 msgs
#converts into text
#send it to ai as context
    def get_context(self):
        context = ""
        for msg in self.short_term[-5:]:   # last 5 messages only
            context += f"User: {msg['user']}\nBot: {msg['bot']}\n"
        return context