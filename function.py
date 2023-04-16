def process_data(original_csv_file, temp_csv_file, temp_json_file, result_json_file, final_csv_file):
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