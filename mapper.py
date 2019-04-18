#!/usr/bin/env python
import sys
import json

firstLine = 'ID,YEAR/MONTH/DAY,ELEMENT,DATA VALUE,M-FLAG,Q-FLAG,S-FLAG,OBS-TIME'

for line in sys.stdin:
    if line == firstLine: # Ignore the header
        continue

    entries = line.split(',')
    station = entries[0]
    year = entries[1][:4]
    data_type = entries[2]
    data = float(entries[3])
    
    result = {
        total_tmin: data if data_type == 'TMIN' else float('inf'),
        total_tmin_station: station if data_type == 'TMIN' else None,
        total_tmax: data if data_type == 'TMAX' else float('-inf'),
        total_tmax_station: station if data_type == 'TMAX' else None,
        by_year: {}
        }
    by_year = result['by_year']
    by_year[year] = {
        tmin_sum: data if data_type == 'TMIN' else 0,
        tmin_min: data if data_type == 'TMIN' else float('inf'),
        tmin_total: 1 if data_type == 'TMIN' else 0,
        tmin_avg: data if data_type == 'TMIN' else None,
        tmax_sum: data if data_type == 'TMAX' else 0,
        tmax_max: data if data_type == 'TMAX' else float('-inf'),
        tmax_total: 1 if data_type == 'TMAX' else 0,
        tmax_avg: data if data_type == 'TMAX' else None
        # TODO: 5 hottest , 5 coldest weather stations for each year excluding abnormalities or missing data 
        }

    print(json.dumps(result))