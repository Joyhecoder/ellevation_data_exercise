import csv
import json

#file path
csvPath = r'temp.csv'
jsonPath = r'temp_data.json'

#*add a column of id numbers to the csv file
with open('sample-mcas.csv') as input, open('temp.csv', 'w') as output:
    reader = csv.reader(input, delimiter= ',')
    writer = csv.writer(output, delimiter=',')
    
    all = []
    row = next(reader)
    row.insert(0, 'ID')
    all.append(row)
    for k, row in enumerate(reader):
        all.append([str(k+1)] + row)
    writer.writerows(all)

#*convert CSV to JSON 
def make_json(csvFilePath, jsonFilePath):
    #create a dictionary
    data = []
    
    #open a csv reader called DictReader
    with open (csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        
        #convert each row into a dictionary and add it to data
        for rows in csvReader:
            
            # key = rows['ID']
            # data[key] = rows
            data.append(rows)
            
    #open a json writer, and use the json.dump() function to jump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
        
        

# make_json(csvPath,jsonPath)

#* replace the Performance Level values
def replace_performance_level_values(json_file):
    #load the JSON file into a Python object
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    #eperf2
    for student in data:
        if student["eperf2"] == "F":
            student["eperf2"] = "1-F"
        elif student["eperf2"] == "W":
            student["eperf2"] = "2-W"
        elif student["eperf2"] == "NI":
            student["eperf2"] = "3-NI"
        elif student["eperf2"] == "P":
            student["eperf2"] = "4-P"
        elif student["eperf2"] == "A":
            student["eperf2"] = "5-A"
        elif student["eperf2"] == "P+":
            student["eperf2"] = "6-P+"
    
    #mperf2
    for student in data:
        if student["mperf2"] == "F":
            student["mperf2"] = "1-F"
        elif student["mperf2"] == "W":
            student["mperf2"] = "2-W"
        elif student["mperf2"] == "NI":
            student["mperf2"] = "3-NI"
        elif student["mperf2"] == "P":
            student["mperf2"] = "4-P"
        elif student["mperf2"] == "A":
            student["mperf2"] = "5-A"
        elif student["mperf2"] == "P+":
            student["mperf2"] = "6-P+"
    
    
    #sperf2
    for student in data:
        if student["sperf2"] == "F":
            student["sperf2"] = "1-F"
        elif student["sperf2"] == "W":
            student["sperf2"] = "2-W"
        elif student["sperf2"] == "NI":
            student["sperf2"] = "3-NI"
        elif student["sperf2"] == "P":
            student["sperf2"] = "4-P"
        elif student["sperf2"] == "A":
            student["sperf2"] = "5-A"
        elif student["sperf2"] == "P+":
            student["sperf2"] = "6-P+"
    
    #write the updated python object back to the JSON file   
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)    

replace_performance_level_values(jsonPath)
