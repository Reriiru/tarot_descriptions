import os

from pymongo import MongoClient

client = MongoClient("mongo")
tarot_db = client.rolz_database
tarot_collection = tarot_db.tarot

if __name__ == "__main__":
    images_directory = './tarot_cards'
    description_directory = './tarot_descriptions'


    for description_filename, image_filename in zip(
                                    sorted(os.listdir(description_directory)),
                                    sorted(os.listdir(images_directory))):

        with open(description_directory+'/'+description_filename, 'r') as file:
            description = file.read()
        
        tarot_data = {
            'Name': description_filename,
            'Descruption': description,
            'Url': 'http://space-walross.ml/tarot/'+description_filename
        }
        
        tarot_collection.insert_one(tarot_data)
