import edge_tts
import asyncio
import os

async def speak(text):
    communicate = edge_tts.Communicate(text, voice="en-US-JennyNeural")
    await communicate.save("output.mp3")
    os.system("start output.mp3")

asyncio.run(speak("Hello! I am speaking with a natural voice My name is Comatoze and i am from porn hub."))