# Paul Dou
# 10/05/23

# Main file, handles GPT and voice assistant compatibility

# import python libraries
import vladGPT # import OpenAI GPT functionality
import vladTTS # import elevenlabs text-to-speech functions
import vladInput # import input handling
import vladInMsg # import prompt message handling
import time

# main func
def main():
    while True:
        # implement prompt functions
        vladInMsg.promptAudio()

        # implement input and GPT functions
        audioText = vladInput.enterInput()
        if audioText:
            aiGarbage = vladGPT.remoteGPT(audioText)
            print(f"VladVA: {aiGarbage}\n") # generate GPT response
            vladTTS.tts(aiGarbage) # narrate GPT response using elevenlabs


if __name__ == "__main__":
    main()