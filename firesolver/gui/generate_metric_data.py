import csv, random
    
# field names 
fields = ['fips','unemp'] 
rows = []
    
# data rows of csv file 
width = 246
height = 304

id = 0
for i in range(width):
    for j in range(height):
        rows.append([id, random.random()*100])
        id += 1
    
# name of csv file 
filename = "metric_data_template.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)