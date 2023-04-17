# Ellevation Data Exerise

This is a data exercise from Ellevation Education where I wrote functions to process different CSV files of data to align with the data format found in "sample-mcas.csv". I created different branches to show my working progress. Version 1 and Version 2 branches help visualize how I modify my workflow to support a big volume of similar files a day. 

# Technology

* [Python](https://www.python.org/)

# How to use the project
First all the original CSV files need to be organized in a file and find the path to this file directory. Store this file directory into a variable. To process the csv files, call the "process_all_csv_files(variable)" with the variable of the directory path as a parameter. 

You should expect the processed csv file with a file name "test_final#.csv" (# indicates the number of the file) as an output. 
# Explanation of the code
All my main functions are located in the "main.py" file. In order to process CSV data and modifity it to align with the sample processed data, I used 5 steps which I summarized it in the function.py file.

Here are my steps:

- Step 1: Add a column of id numbers to the original CSV file. The reason of the step is that when I first tried to convert the CSV into a JSON file by using the first column "district", the rows with the same "district" values were overwritten by the last row of data with the same value. 
- Step 2: Convert CSV file to JSON file. I created an empty array to store all the data from CSV file. A for loop was run to get each row of data and append it to the data array. 
- Step 3: Replace the Performance Level values in the JSON file by the code reference provided in the instruction document. 
- Step 4: Create a new JSON file with existing data and modify it to align with the data format found in "sample-mcas-processed.cvs". Each student will have 3 rows of data to display the score data for each subject (ELA, math and science). The final data is sorted by student test ID so that all 3 subjects' data are together for easy lookup. 
- Step 5: Convert the new JSON file back to CSV file. 



# How to process multiple CSV files 
Here are my steps to approach efficiency to process multiple CSV files: 

- In my Version 1 branch, I created a function called process_data() and include each step as a function inside process_data function so that I just need to invoke one function to run each step. However, this function needs to be triggered each time when a new CSV file needs to be processed. 
- In my Version 2 branch, I modified the code to allow the function to be called based on however many CSV files that need to be processed. I created a function "find_csv_files()" to find all the CSV files in a same directory and store the file names into an array variable "all_file". By the end I created a function "process_all_csv_files()" where it will first get all the file names and process the files to meet the requirements of the "sample-mcas-processed.csv". 

# Files
- "files" folder includes a few copies of same "sample-mcas.csv" for testing purposes to see if I could run my function to process multiple files. 
- "main.py" is my main python file for my functions and code.
- "function.py" is a summary of my logic of how to process data.
- The rest of the files are the results from running tests. 