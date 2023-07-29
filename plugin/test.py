import openai
def getChat():
    openai.api_key = "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"
    openai.api_base = "https://openaiapicn.top/v1"
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                   messages=[{"role": "user", "content": "我应该如何追求梦想"}])
    text=chat_completion
    print(text["choices"][0]["message"]['content'])
if __name__=="__main__":
    getChat()