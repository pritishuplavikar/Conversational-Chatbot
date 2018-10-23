import numpy
# import tensorflow as tf
import nltk
from random import shuffle

def preprocess_data(data):
    max_dialogue_len = 0
    padded_data_X = []
    padded_data_Y = []
    for conversation in data:
        for dialogue in conversation:
            query = dialogue[0].split()
            padded_query = query
            
            response = dialogue[1].split()
            padded_response = ["<START>"] + response
            
            padded_data_X.append(padded_query)
            padded_data_Y.append(padded_response)

            if max(len(query), len(response)) > max_dialogue_len:
            	max_dialogue_len = max(len(query), len(response))
    
    return padded_data_X, padded_data_Y, max_dialogue_len


def create_dataset(): #data_file
	data_file = open("new_dialogues.txt")
	data = data_file.readlines()
	data_file.close()

	dataset = []

	for line in data:
		convsersation = []
		dialogues = line.replace("\xe2\x80\x99", "'").split("\n")[0].split("__eou__")[:-1]

		index = 0
		while index < len(dialogues) - 1:
			convsersation.append([dialogues[index].lower().strip() + " <EOS>", dialogues[index+1].lower().strip() + " <EOS>"])
			index += 1
		dataset.append(convsersation)

	data_file = open("to_augment.txt")
	data = data_file.readlines()
	data_file.close()

	aug_dataset = []

	for line in data:
		convsersation = []
		dialogues = line.replace("\xe2\x80\x99", "'").split("\n")[0].split("__eou__")[:-1]

		index = 0
		while index < len(dialogues) - 1:
			convsersation.append([dialogues[index].lower().strip() + " <EOS>", dialogues[index+1].lower().strip() + " <EOS>"])
			index += 2

		aug_dataset.append(convsersation)

	for i in range(6):
		aug_dataset.extend(aug_dataset)

	dataset.extend(aug_dataset)
	shuffle(dataset)
	data_X, data_Y, l = preprocess_data(dataset)

	return data_X, data_Y, l