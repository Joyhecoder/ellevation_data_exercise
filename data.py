import csv
import json

#file path
csvPath = r'temp.csv'
jsonPath = r'temp_data.json'

#*add a column of id numbers to the csv file
def add_id(csv_file, temp_csv_file):
    with open(csv_file) as input, open(temp_csv_file, 'w') as output:
        reader = csv.reader(input, delimiter= ',')
        writer = csv.writer(output, delimiter=',')
        
        all = []
        row = next(reader)
        row.insert(0, 'ID')
        all.append(row)
        for k, row in enumerate(reader):
            all.append([str(k+1)] + row)
        writer.writerows(all)
    
    
# add_id(csvPath, jsonPath)
# add_id("sample-mcas.csv", "test.csv")

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
    
    #hashtable
    performance_level_value_reference = {
        "F": "1-F",
        "W": "2-W",
        "NI": "3-NI",
        "P": "4-P",
        "A": "5-A",
        "P+": "6-P+"
    }
    
    for student in data:
        #eperf2
        student["eperf2"] = performance_level_value_reference[student["eperf2"]]
         #mperf2
        student["mperf2"] = performance_level_value_reference[student["mperf2"]]
          #sperf2
        student["sperf2"] = performance_level_value_reference[student["sperf2"]]       
    
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

# new_json(jsonPath, "result1.json")


#* Convert json file to csv
def json_to_csv(json_file, final_csv_file):
    #open json file and load the data 
    with open(json_file) as json_file:
        data = json.load(json_file)
        
    #open a file for writing
    data_file = open(final_csv_file, 'w')
    
    #create the csv writer object
    csv_writer = csv.writer(data_file)
    
    #counter variable used for writing headers to the CSV file
    count = 0
    
    for student in data:
        #writing headers of CSV file
        if count == 0:
            header = student.keys()
            csv_writer.writerow(header)
            count += 1
            
        #write data of CSV file
        csv_writer.writerow(student.values())
        
    data_file.close()
    
json_to_csv("result1.json", "result1.csv")

