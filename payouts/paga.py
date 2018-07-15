import json

with open("payout01072018.json", "r") as read_file:
    data_dict = json.load(read_file)


for data in data_dict:





    print(data['recipient'])

	
	
	
