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

# Testing purposes
in_file = "../tests/data/rwl/co021.rwl" # to change such that file can be called from outside
out_json = "./tree_loc_inf.json" # to change to something that the user wants specified (?)

# Create empty JSON
def create_json(in_file, out_json):
    
    # Creating dictionary
    jsonfile = {}
    
    with open(in_file, "r" ) as rings:
        data= rings.read()
        lines = data.splitlines()
        # print (lines[0-2])
        # read every single line
        for  rows  in lines:
            rows  = rows.split()
            print(rows)
            key = rows[0]
            jsonfile[key] = rows
            try:
                # site_id = rows[0]
                site_name = rows[1]
                species_code = rows[2]
                state_country = rows[3]
                species = rows[4]
                elevation = rows[5]
                latitude = rows[6]
                longitude = rows[7]
                first_year = rows[8]
                last_year= rows[9]
                lead_inv = rows[10]
                completion = rows[11]
            except IndexError: 
                pass

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
        jsonfile["site_name"] = site_name
        jsonfile["species_code"] = species_code
        jsonfile["state_country"] = state_country
        jsonfile["species_name"] = species
        jsonfile["elevation"] = elevation
        jsonfile["latitude"] = latitude
        jsonfile["longitude"] = longitude
        jsonfile["first_year"] = first_year
        jsonfile["last_year"] = last_year
        jsonfile["lead_investigator"] = lead_inv
        jsonfile["completion_date"] = completion
        # if unit == "999":
        #     jsonfile["unit"] = "0.01mm"
        # elif unit == "-9999":
        #     jsonfile["unit"] = "0.001mm"
        # else:
        #     print("ERROR - Stop code is not 999 or -9999. Cannot identify a unit.")
        #     exit

        # Testing purposes
    with open(out_json, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(jsonfile, indent=4))

# Driver Code
 
# Decide the two file paths according to your
# computer system

# Testing
create_json(in_file,out_json)
# Input file format
## File format is rwl
### Understanding the rwl format: https://rdrr.io/cran/dplR/man/write.tucson.html
### Example file: https://www.treeringsociety.org/resources/SOM/Brewer_Murphy_SupplementaryMaterial.pdf