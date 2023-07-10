import openai
def getChat():
    openai.api_key = "sk-f2KkLJ1DF9dR2PUWoMknNU7KHOL2VW9EY6vQ6SYdHBa93pKk"
    openai.api_base = "https://oa.f2api.com/v1"
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "我应该如何追求梦想"}])
    text=chat_completion.to_dict()
    text=text['choices'][0].to_dict()
    print(text)
if __name__=="__main__":
    getChat()