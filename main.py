import json

filename = 'image1.txt'
dict1 = {}
list1 = []

# fields in the sample file
fields = ['x', 'y', 'width', 'height']

# get the data from txt file
with open(filename) as fh:
    for line in fh:
        description = list(line.strip().split(' '))
        print(description)
        i = 0
        dict2 = {}
        while i < len(fields):
            dict2[fields[i]] = float(description[i + 1])
            i = i + 1
        dict2['rotation'] = 0
        dict2['rectanglelabels'] = ["object"]
        list1.append({'image_rotation': 0, 'value': dict2})

dict1['annotations'] = [{'result': list1}]
dict1['data'] = {"image": "\/data\/upload\/image1.jpg"}

# creating json file
out_file = open("image1.json", "w")
json.dump(dict1, out_file, indent=4)
out_file.close()
