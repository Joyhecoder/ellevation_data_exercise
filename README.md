# Ellevation Data Exerise

This is a data exercise from Ellevation Education where I wrote functions to process different CSV files of data to align with the data format found in "sample-mcas.csv". I created different branches to show my working progress. Version 1 and Version 2 branches help visualize how I modify my workflow to support a big volume of similar files a day. 

# Technology

* [Python](https://www.python.org/)


# How to use it
All my main functions are located in the "main.py" file. In order to process CSV data and modifity it to align with the sample processed data, I used 5 steps which I summarized it in the function.py file.

Here are my steps:

- Step 1: Add a column of id numbers to the original CSV file. The reason of the step is that when I first tried to convert the CSV into a JSON file by using the first column "district", the rows with the same "district" values were overwritten by the last row of data with the same value. 
- Step 2: Convert CSV file to JSON file. I created an empty array to store all the data from CSV file. A for loop was run to get each row of data and append it to the data array. 
- Step 3: Replace the Performance Level values in the JSON file by the code reference provided in the instruction document. 
- Step 4: Create a new JSON file with existing data and modify it to align with the data format found in "sample-mcas-processed.cvs". Each student will have 3 rows of data to display the score data for each subject (ELA, math and science). The final data is sorted by student test ID so that all 3 subjects' data are together for easy lookup. 
- Step 5: Convert the new JSON file back to CSV file. 

Here are my steps to approach efficiency to process multiple CSV files. 