import os

directory = './tarot_descriptions'

if __name__ == "__main__":
    for filename in os.listdir(directory):
        if filename.find("***"):
            os.rename(directory+'/'+filename, directory+'/'+filename.split(' ***')[0])
        if filename.find("Tarot Card Meaning"):
            os.rename(directory+'/'+filename, directory+'/'+filename.split(' Tarot Card Meaning')[0])
