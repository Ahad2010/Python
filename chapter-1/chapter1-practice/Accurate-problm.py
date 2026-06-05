import edge_tts
import asyncio
import os

async def speak(text):
    communicate = edge_tts.Communicate(text, voice="en-US-JennyNeural")
    await communicate.save("output.mp3")
    os.system("start output.mp3")

asyncio.run(speak("Once upon a time, a clever fox lived near a large, green forest. One sunny morning, he was walking through the woods looking for something to eat, when a wonderful smell caught his attention. High up in the branches of an old oak tree, a black crow sat with a large, delicious piece of cheese in her beak."))


# asyncio.run(speak("Hello! I am speaking with a natural voice My name is Comatoze and i am from porn hub."))
