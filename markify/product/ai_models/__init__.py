import openai
import key




def get_response(message):
    openai.api_key=key.api_key
    messages = [ {"role": "system", "content": "Make an Advertisement Title. Only give the title without any other text.The input will be the product"} ]
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="davinci-002", messages=messages
        )
      
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")

get_response('Dell Latitude E7440 is a Windows 8 laptop with a 14.00-inch display. It is powered by a Core i5 processor and it comes with 4GB of RAM. The Dell Latitude E7440 packs 256GB of SSD storage.')    