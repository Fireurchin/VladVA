# Paul Dou
# 10/05/23

# TTS file, handles voice assistant functionality

# import python libraries
import elevenlabs # import elevenlabs text-to-speech library
import ffmpeg # I hate you so much
import time

# initialize TTS functionality
elevenlabs.set_api_key("") # insert ElevenLabs API key

# convert GPT response to TTS
def tts(verbalGarbage):
    audio = ""
    try: # if too many chars
        audio = elevenlabs.generate(text=verbalGarbage[:2499],voice="Bella",model="eleven_monolingual_v1") # generate elevenlabs audio
    except Exception as e:
        print("Error: "+str(e)) # display error code
    
    try: # if audio cannot be played
        elevenlabs.play(audio) # play elevenlabs audio
    except Exception as e:
        print("Error: "+str(e)) # display error code