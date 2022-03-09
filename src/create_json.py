from __future__ import print_function

__copyright__ = """
   dplPy for tree ring width time series analyses
   Copyright (C) 2021  OpenDendro

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
__license__ = "GNU GPL3"

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Date:2021-08-13
# Author: Sarah Jackson & Michele Cosi
# Project: OpenDendro - rwl (Tucson) Format 
# Description: Assigns variable names to each value in the tucson formated datasets using the emptyjson file.
# example usage:

import csv
import json
import os
import pandas as pd
import re

# Testing purposes
in_file = "../tests/data/rwl/co021_short.rwl" # to change such that file can be called from outside
out_json = "./tree_loc_inf.json" # to change to something that the user wants specified (?)

if os.path.exists(out_json):
    os.remove(out_json)
    print("out_json was overwritten")
else:
    print("nothing was deleted")

# Create empty JSON
def create_json(in_file, out_json):
    
    # Creating dictionary, json array
    dictionary = {}
    json_arr = []
    # df = pd.DataFrame(columns = ["site_id","site_name","species_code","state_country",
    # "species_name","elevation","latitude","longitude","first_year",
    # "last_year","lead_investigator","completion_date"])

    # Iterate through every line of the input file and assign strings
    with open(in_file, "r" ) as rings:
        data= rings.read()
        lines = data.splitlines() # splits lines
    
    all_rows = []
    for rows in lines:
        rows = re.sub("\s+",",",rows.strip()) # splits strings by spaces (default)
        all_rows.append(rows.split(","))

    df = pd.DataFrame(all_rows, columns = ["site_id","site_name","species_code","state_country",
    "species_name","elevation","latitude","longitude","first_year",
    "last_year","lead_investigator","completion_date"])
    
    # df = df.set_index("site_id")
    # df = df.fillna(value="None")
    print(df)
    result = df.to_json("temp.json", orient="records")
    json.dumps(result, indent = 4,  sort_keys = True)


    ##### MAJOR REWRITE. JSON IS NOT PRETTY, BUT DOES THE JOB. CODE WORKS FOR RWL FORMAT.
    ##### TO DO: PRETTIFY, CSV, TEST AND CHECK.
    

        # df.append(int(rows))
        # print(rows)

    # df = pd.DataFrame(rows)
    # print(df)
    # df.columns = ["site_id","site_name","species_code","state_country",
    #                 "species_name","elevation","latitude","longitude","first_year",
    #                 "last_year","lead_investigator","completion_date"]

    # df.to_csv("test.csv")   
        
        # # Assign primary key to first column (site_id)
        # key = rows[0]
        # dictionary[key] = rows

        # # There has to be a better way to do this:
        # # Assignning na to non existing strings in rwl format
        # try:
        #     site_name = rows[1]
        # except IndexError:
        #     site_name = "na"
        
        # try:
        #     species_code = rows[2]              
        # except IndexError:
        #     species_code = "na"            
        
        # try:            
        #     state_country = rows[3]
        # except IndexError:
        #     state_country = "na"            
        
        # try:              
        #     species = rows[4]
        # except IndexError:
        #     species = "na"            
        
        # try:              
        #     elevation = rows[5]
        # except IndexError:
        #     elevation = "na"            
        
        # try:              
        #     latitude = rows[6]         
        # except IndexError:
        #     latitude = "na"            
        
        # try:              
        #     longitude = rows[7]
        # except IndexError:            
        #     longitude = "na"
        
        # try:              
        #     first_year = rows[8]
        # except IndexError:
        #     first_year = "na"            
        
        # try:             
        #     last_year = rows[9]
        # except IndexError:     
        #     last_year = "na"       
        
        # try:                          
        #     lead_inv = rows[10]
        # except IndexError:
        #     lead_inv = "na"
        
        # try:
        #     completion = rows[11]
        # except IndexError:
        #     completion = "na"

        # # Assign strigs
        # dictionary["site_name"] = site_name
        # dictionary["species_code"] = species_code
        # dictionary["state_country"] = state_country
        # dictionary["species_name"] = species
        # dictionary["elevation"] = elevation
        # dictionary["latitude"] = latitude
        # dictionary["longitude"] = longitude
        # dictionary["first_year"] = first_year
        # dictionary["last_year"] = last_year
        # dictionary["lead_investigator"] = lead_inv
        # dictionary["completion_date"] = completion

        # json_out = json.dumps(dictionary, indent = 4)
    
        # json_arr.append(json_out)

    # with open(out_json, 'a', encoding='utf-8') as jsonf:
    #     # while(len(lines)):
    #     json.dump(json_arr, jsonf)


        # if unit == "999":
        #     jsonfile["unit"] = "0.01mm"
        # elif unit == "-9999":
        #     jsonfile["unit"] = "0.001mm"
        # else:
        #     print("ERROR - Stop code is not 999 or -9999. Cannot identify a unit.")
        #     exit

        # Testing purposes
    # with open(out_json, 'a', encoding='utf-8') as jsonf:
    #     # while(len(lines)):
    #     jsonf.write(json.dumps(jsonfile, indent=4))

# Driver Code
 
# Decide the two file paths according to your
# computer system

# Testing
create_json(in_file,out_json)
# Input file format
## File format is rwl
### Understanding the rwl format: https://rdrr.io/cran/dplR/man/write.tucson.html
### Example file: https://www.treeringsociety.org/resources/SOM/Brewer_Murphy_SupplementaryMaterial.pdf

## NOTES: work done thus far only cover rwl format.
## Future objtvs: support for csv; Reflect on json req format. 





        # convert every element in each list to string- it is easier to manupilate the elements

            # str(rows)  

            # State/province

            # # start year- start of collection 
            # start_date = int(lines[1])#,6])

            # # end year- completion year
            # end_year = int(lines[1])#,7])

        # # site_id
        #     # Via indexing the first three digits of the site id are assigned to var named site_code and the rest to information.
        #     # Check if all the site codes are the same for the whole dataset 
        # for site_code in lines:
        #     current=0
        #     information=0 
        #     site_id=0 
        #     unit = 0
        #     while current >=0 and current<=len(lines)-1:
        #         if current <=3:   
        #             site_code = lines[current,0,0]       
        #         if current>=4 and current<=len(lines)-1:
        #             if lines[current,0,0] == lines[4,0,0]:
        #                 site_id = lines[current,0,0]
        #                 information = site_id[3::]  
        #         site_id= site_code + information 
        #         #data
        #         data=[]
        #         y=1
        #         past= y-1
        #         end=[current,-1]
        #         # if site_id == lines[current,0] and start_date <= int(lines[]):
        #         #     for points in lines[current,2:]:
        #         #         pts=[]
        #         #         pts.append(points)
        #         #         # End of data collection for that year
        #         #         if points== "999" or points== "-9999":
        #         #             pts[:-1]
        #         #             data.append(pts)
        #         #             pts=0
        #         #             unit = points
        #     else:
        #         current = current + 1
        #         pts=0
    
        # jsonfile["site_id"] = site_id