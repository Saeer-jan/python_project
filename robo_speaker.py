import os

if __name__ == '__main__':
    while True:
        x = input("Enter the text you want to speak: ")
        if x.lower() == "ok":
            # when someone enters "ok", the program will exit, and i want to say good bye so
            os.system(
                'PowerShell -Command "Add-Type -AssemblyName System.Speech; '
                f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Goodbye!\')"'
            )
            print("Exiting the program.")
            exit(0)
        # Properly format and escape the PowerShell command
        os.system(
            f'PowerShell -Command "Add-Type -AssemblyName System.Speech; '
            #the above line is used to load the System.Speech assembly
            # the below line is used to create a new SpeechSynthesizer object and call the Speak method
            f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
        )



        """        The above code is used to take input from the user and speak it
         out loud using the System.Speech.Synthesis.SpeechSynthesizer class in PowerShell.
         this is just my simple practising project
         """