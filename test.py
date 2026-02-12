import pyautogui
import pyaudio
import time
import os
from pocketsphinx import Decoder, get_model_path

def hotword():
    # PocketSphinx setup
    decoder = None
    paud = None
    audio_stream = None

    # --- Configuration ---
    keyphrase = "hey deva"
    
    # 1. PATH TO YOUR CUSTOM DICTIONARY
    # Assumes 'custom.dict' is in the same folder as your Python script
    dict_path = "custom.dict" 
    
    # 2. THIS IS THE "TRAINING" PART
    # You MUST tune this value.
    # Start with 1e-20.
    # - If it NEVER detects "hey deva", make it smaller (e.g., 1e-30).
    # - If it triggers on EVERYTHING, make it bigger (e.g., 1e-10).
    kws_threshold = 1e-20 
    
    # --- Get model paths ---
    try:
        model_path = get_model_path()
        hmm_path = os.path.join(model_path, 'en-us')

        # --- Initialize Decoder ---
        config = Decoder.default_config()
        config.set_string('-hmm', hmm_path)
        
        # 3. USE YOUR CUSTOM DICTIONARY
        config.set_string('-dict', dict_path) 
        
        # 4. SET YOUR KEYPHRASE AND THRESHOLD
        config.set_string('-keyphrase', keyphrase)
        config.set_float('-kws_threshold', kws_threshold)
        
        config.set_string('-logfn', 'nul') # Suppress log output

        print("Initializing PocketSphinx...")
        decoder = Decoder(config)
        decoder.start_utt()
        print(f"PocketSphinx initialized. Listening for '{keyphrase}'...")
        print(f"Using dictionary: {dict_path}")
        print(f"Using threshold: {kws_threshold}")

    except Exception as e:
        print(f"Error initializing PocketSphinx: {e}")
        if not os.path.exists(dict_path):
            print(f"ERROR: Cannot find '{dict_path}'. Did you create it?")
        return

    try:
        # --- Initialize PyAudio Stream ---
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=16000,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=1024
        )

        while True:
            pcm = audio_stream.read(1024, exception_on_overflow=False)
            decoder.process_raw(pcm, False, False)
            
            hyp = decoder.hyp()
            if hyp is not None:
                print(f"Hotword detected: {hyp.hypstr}")
                
                # Emulate pressing Win+Y shortcut
                pyautogui.keyDown("win")
                pyautogui.press("y")
                time.sleep(2)
                pyautogui.keyUp("win")
                
                # Restart the decoder
                print(f"Restarting listener for '{keyphrase}'...")
                decoder.end_utt()
                decoder.start_utt()

    except KeyboardInterrupt:
        print("Stopping...")
    except Exception as e:
        print(f"Error in hotword detection: {e}")
    finally:
        # --- Cleanup ---
        print("Cleaning up...")
        if decoder is not None:
            decoder.end_utt()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

# --- To run the script directly ---
if __name__ == "__main__":
    hotword()