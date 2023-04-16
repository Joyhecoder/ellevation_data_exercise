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

# replace_performance_level_values(jsonPath)


#* create a new json file with existing json data:
def new_json(input_js_file, output_js_file):
    #read data from existing JSON file
    with open(input_js_file, 'r') as f:
        data = json.load(f)
    
    #create a new dictionary for new file
    all_data_arr = []
    #manipulate data as per requirement
    
    #*ELA data only
    for row in data:
        new_data_dic = {}
        new_data_dic['NCESID'] = 373737
        new_data_dic['StudentTestID'] = row['sasid']
        new_data_dic['StudentLocalID'] = 'missing'
        new_data_dic['StudentGradeLevel'] = row['stugrade']
        new_data_dic['TestDate'] = 'April 1'
        new_data_dic['TestName'] = 'MCAS'
        new_data_dic['TestTypeName'] = 'MCAS ELA'
        new_data_dic['TestSubjectName'] = 'ELA'
        new_data_dic['TestGradeLevel'] = row['stugrade']
        new_data_dic['Score1Label'] = 'Performance Level'
        new_data_dic['Score1Type'] = 'Level'
        new_data_dic['Score1Value'] = row['eperf2']
        new_data_dic['Score2Label'] = 'Scaled Score'
        new_data_dic['Score2Type'] = 'Scale'
        new_data_dic['Score2Value'] = row['escaleds']
        new_data_dic['Score3Label'] = 'CPI'
        new_data_dic['Score3Type'] = 'Scale'
        new_data_dic['Score3Value'] = row['ecpi']
        new_data_dic['Score4Label'] = ''
        new_data_dic['Score4Type'] = ''
        new_data_dic['Score4Value'] = ''
        
        #append each data dictionary into the array
        all_data_arr.append(new_data_dic)
    
    #*Math data only
    for row in data:
        new_data_dic = {}
        new_data_dic['NCESID'] = 373737
        new_data_dic['StudentTestID'] = row['sasid']
        new_data_dic['StudentLocalID'] = 'missing'
        new_data_dic['StudentGradeLevel'] = row['stugrade']
        new_data_dic['TestDate'] = 'May 1'
        new_data_dic['TestName'] = 'MCAS'
        new_data_dic['TestTypeName'] = 'MCAS Math'
        new_data_dic['TestSubjectName'] = 'Math'
        new_data_dic['TestGradeLevel'] = row['stugrade']
        new_data_dic['Score1Label'] = 'Performance Level'
        new_data_dic['Score1Type'] = 'Level'
        new_data_dic['Score1Value'] = row['mperf2']
        new_data_dic['Score2Label'] = 'Scaled Score'
        new_data_dic['Score2Type'] = 'Scale'
        new_data_dic['Score2Value'] = row['mscaleds']
        new_data_dic['Score3Label'] = 'CPI'
        new_data_dic['Score3Type'] = 'Scale'
        new_data_dic['Score3Value'] = row['mcpi']
        new_data_dic['Score4Label'] = ''
        new_data_dic['Score4Type'] = ''
        new_data_dic['Score4Value'] = ''
        
        #append each data dictionary into the array
        all_data_arr.append(new_data_dic)
        
    
    #*Science data only
    for row in data:
        new_data_dic = {}
        new_data_dic['NCESID'] = 373737
        new_data_dic['StudentTestID'] = row['sasid']
        new_data_dic['StudentLocalID'] = 'missing'
        new_data_dic['StudentGradeLevel'] = row['stugrade']
        new_data_dic['TestDate'] = 'June 1'
        new_data_dic['TestName'] = 'MCAS'
        new_data_dic['TestTypeName'] = 'MCAS Science'
        new_data_dic['TestSubjectName'] = 'Science'
        new_data_dic['TestGradeLevel'] = row['stugrade']
        new_data_dic['Score1Label'] = 'Performance Level'
        new_data_dic['Score1Type'] = 'Level'
        new_data_dic['Score1Value'] = row['sperf2']
        new_data_dic['Score2Label'] = 'Scaled Score'
        new_data_dic['Score2Type'] = 'Scale'
        new_data_dic['Score2Value'] = row['sscaleds']
        new_data_dic['Score3Label'] = 'CPI'
        new_data_dic['Score3Type'] = 'Scale'
        new_data_dic['Score3Value'] = row['scpi']
        new_data_dic['Score4Label'] = ''
        new_data_dic['Score4Type'] = ''
        new_data_dic['Score4Value'] = ''
        
        #append each data dictionary into the array
        all_data_arr.append(new_data_dic)
        
    #sort the array by student id 
    sorted_all_data_arr = sorted(all_data_arr, key=lambda d: d['StudentTestID'])
    # print(sorted_all_data_arr)
    #create a new JSON file and write data to it
    with open(output_js_file, "w") as file:
        json.dump(sorted_all_data_arr, file, indent=4)

   
  
    
    

new_json(jsonPath, "result.json")

