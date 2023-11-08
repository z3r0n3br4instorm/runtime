import os
import sys
import subprocess
import json
import time

def commGPT(data):
    __commOS = 'python gpt_response.py \"'+str(data)+'\"'
    return subprocess.check_output(__commOS, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

def split_string(string):
    return [c for c in string]

if __name__ == "__main__":
    print("ZeroneLabs | RunTime v1.0")
    while True:
        get_input = input("> ")
        data = commGPT(get_input)
        for i in split_string(data):
            if i != "`":
                time.sleep(0.001)
                sys.stdout.write("\033[1m"+i)
                sys.stdout.flush()
        if "```" in data:
            print("Script detected !, Autorun")
            try:
                if True:
                    string_data = data.replace("```","")
                    if string_data.split("\n")[0].lower() == "bash":
                        print("Executing bash script")
                        writeTemp = open("TempScript.sh","a")
                        string_data = string_data.split("\n")
                        string_data.pop(0)
                        for i in string_data:
                            writeTemp.write(i+"\n")
                        writeTemp.close()
                        os.system("chmod +x TempScript.sh")
                        os.system("./TempScript.sh")
                        #os.system("rm TempScript.sh")
                    if string_data.split("\n")[0].lower() == "python":
                        print("Executing Python script")
                        writeTemp = open("TempScript.py","a")
                        string_data = string_data.split("\n")
                        string_data.pop(0)
                        for i in string_data:
                            writeTemp.write(i+"\n")
                        writeTemp.close()
                        os.system("python TempScript.py")
                        os.system("rm TempScript.py")
                    if string_data.split("\n")[0].lower() == "c":
                        print("Executing C program")
                        writeTemp = open("TempScript.c","a")
                        string_data = string_data.split("\n")
                        string_data.pop(0)
                        for i in string_data:
                            writeTemp.write(i+"\n")
                        writeTemp.close()
                        print("Compiling Resource...")
                        os.system("gcc TempScript.c -o temp")
                        os.system("./temp")
                        os.system("rm TempScript.c")
                        os.system("rm temp")
            except:
                print("Program Failed to run !")
        sys.stdout.write("\033[0m")
