# clean_metadata_script
This script will read a csv file of metadata that was created by exiftools 
(separate script: extract metadata from image & video files and store it in a csv)
And will 
1. delete unwanted columns
2. reformat certain columns
3. rename columns (to facilitate import into postgresql database)
4. automatically fill camera_trap_id column based on source_path column value
5. and ouput the cleaned csv file 


to use this script, the csv files already needs to be in a certain format with specific columns
copy this script into the directory where your csv files are found
create a new directory called "cleaned"
first delete the "UserComment" column manually from your csv file, as it poses problems
then run "python clean_metadata.py"
it will then ask you to input a file name, then output the cleaned csv file within the cleaned directory
