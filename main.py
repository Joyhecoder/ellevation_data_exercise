import csv
import json
import os

#file path
csvPath = r'temp.csv'
jsonPath = r'temp_data.json'


#*add a column of id numbers to the csv file
def add_id(csv_file, temp_csv_file):
    try:
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
    
    except Exception as e:
        print(e)
    
    
# add_id(csvPath, jsonPath)
# add_id("sample-mcas.csv", "test.csv")

#*convert CSV to JSON 
def make_json(csvFilePath, jsonFilePath):
    try:
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
    except Exception as e:
        print(e)
     
        

# make_json(csvPath,jsonPath)

#* replace the Performance Level values
def replace_performance_level_values(json_file):
    try:
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
            "P+": "6-P+",
            " ": " "
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
    except Exception as e:
        print(e)


    
# replace_performance_level_values(jsonPath)


#* create a new json file with existing json data:
def new_json(input_js_file, output_js_file):
    try:
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
    except Exception as e:
        print(e)

# new_json(jsonPath, "result1.json")


#* Convert json file to csv
def json_to_csv(json_file, final_csv_file):
    try:
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
    except Exception as e:
        print(e)
    
# json_to_csv("result1.json", "result1.csv")

def process_data(original_csv_file, temp_csv_file, temp_json_file, result_json_file, final_csv_file):
    try:
        #*add a column of id numbers to the csv file
        add_id(original_csv_file, temp_csv_file)
        
        #*convert CSV to JSON 
        make_json(temp_csv_file, temp_json_file)
        
        #* replace the Performance Level values
        replace_performance_level_values(temp_json_file)
        
        #* create a new json file with existing json data:
        new_json(temp_json_file, result_json_file)
        
        #* Convert json file to csv
        json_to_csv(result_json_file, final_csv_file)
        
        print("end of the process_data function")
    except Exception as e:
        print(e)
    
# process_data("sample-mcas.csv", "p_temp.csv", "p_temp.json", "p_result.json", "p_final.csv")



#!run multiple csv files:
#* Get all the CSV files and store into an array
def find_csv_files(path_to_dir, suffix=".csv"):
    try:
        #os.listdir() method is used to et the list of all files and directories in the specified directory
        file_names = os.listdir(path_to_dir)
    
        all_file = [file_name for file_name in file_names if file_name.endswith(suffix)]
        print("all the files:", all_file)
        return all_file
    except Exception as e:
        print(e)
    
#directory where all the original csv files are stored
all_file_path = './files'

#invoke the function to find all the files and stored them into files_arr variable
# files_arr = find_csv_files(all_file_path)
# print(files_arr)

#* delete extra files:
def delete_files(tem_csv_file, temp_json_file, result_json_file):
    try:
        files_to_delete_arr = []
        files_to_delete_arr.extend([tem_csv_file,temp_json_file,result_json_file])
        print("files delete arr", files_to_delete_arr)
        for file in files_to_delete_arr:
            if os.path.exists(file):
                os.remove(file)
            else:
                print("%s does not exist" % file)
    except Exception as e:
        print(e)      
        
# delete_files("test_temp1.csv", "test_temp1.json", "test_result1.json")

#! Process all csv files function
def process_all_csv_files(path_to_dir):
    try:
        #* find all the csv files and store them in array
        files_arr = find_csv_files(path_to_dir)

        #* process multiple csv files:
        count = 1
        for each_file in files_arr:
            original_csv_file = './files/%s' %each_file
            print("current processing file:", original_csv_file)
            temp_csv_file = 'test_temp%s.csv' % count
            temp_json_file = 'test_temp%s.json' % count
            result_json_file = 'test_result%s.json' % count
            final_csv_file = 'test_final%s.csv' % count
            
            process_data(original_csv_file, temp_csv_file, temp_json_file, result_json_file, final_csv_file)
            print('just converted %s file' %count )
            
            #* delete the extra files
            delete_files(temp_csv_file, temp_json_file, result_json_file)
            
            count += 1
    except Exception as e:
        print(e)
    
process_all_csv_files(all_file_path)