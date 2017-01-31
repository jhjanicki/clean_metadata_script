import numpy as np 
import pandas as pd

#step 1: UserComment has problem, so manually delete it

filename = raw_input('Enter a filename: ')

# step 2: load csv based on user input name
df = pd.read_csv(filename)

#step 3: drop unwanted columns
df.drop(['ExifToolVersion','Directory', 'FileModifyDate', 'FileAccessDate','FileInodeChangeDate','FilePermissions','FileTypeExtension', 'MIMEType','ExifByteOrder','Make','Model','Software','ModifyDate','Copyright','Orientation','XResolution','YResolution','ResolutionUnit','YCbCrPositioning','ExifVersion','DateTimeOriginal','ExposureTime','FNumber','MeteringMode','WhiteBalance','ColorSpace','ExposureProgram','ExifImageWidth','ExifImageHeight','Warning','ImageWidth','ImageHeight','EncodingProcess','BitsPerSample','ColorComponents','YCbCrSubSampling','ShutterSpeed'], axis=1, inplace=True)
        
#step4: split CreateDate into date and time
df['CreateDate'], df['CreateTime'] = df['CreateDate'].str.split(' ', 1).str

#reformat
df['CreateDate'] = df['CreateDate'].str.replace(':','-')

# add note column
df.insert(12, 'note','')

#function to get camera trap ID from source file
def getCameraTrap(srcFile):
	srcFileArray=srcFile.split('/')
	targetString=srcFileArray[5]
	output = targetString[:4]
	return output
srcFilePath = df['SourceFile'].iloc[0]
cameraTrapValue=getCameraTrap(srcFilePath)

# Step 5: insert camera_trap_id column
df.insert(1, 'camera_trap_id',cameraTrapValue)


# Step 6: rename columns
df = df.rename(columns={'SourceFile': 'source_path', 'FileName': 'original_file_name', 'FileSize':'file_size','FileType':'file_type','CreateDate':'date_created','Flash':'flash','ISO':'iso','Aperture':'aperture','ImageSize':'image_size','Megapixels':'megapixels','LightValue':'light_value','CreateTime':'time_created'})

# prepare output file name
date_part = filename.split('.')
outputfilename=cameraTrapValue+'_'+date_part[0]+'_cleaned.csv'
# print outputfilename

df.to_csv('./cleaned/'+outputfilename, sep=',', encoding='utf-8')


# todo:
# rewrite script to take into consideration video files