#!/usr/bin/env python
import sys
import json

for line in sys.stdin:
    entries = line.split(',')
    station = entries[0]
    date = entries[1]
    year = date[:4]
    data_type = entries[2]
    data = float(entries[3]) / 10
    qflag = entries[5]

    if qflag != '': # Ignore bad data
        continue
    
    result = {
        'total_tmin': data if data_type == 'TMIN' else float('inf'),
        'total_tmin_station': station if data_type == 'TMIN' else None,
        'total_tmax': data if data_type == 'TMAX' else float('-inf'),
        'total_tmax_station': station if data_type == 'TMAX' else None,
        'by_year': {}
        }
    by_year = result['by_year']
    by_year[year] = {
        'tmin_sum': data if data_type == 'TMIN' else 0,
        'tmin_min': [{'temp': data, 'station': station, 'date': date}] if data_type == 'TMIN' else [],
        'tmin_total': 1 if data_type == 'TMIN' else 0,
        'tmin_avg': data if data_type == 'TMIN' else None,
        'tmax_sum': data if data_type == 'TMAX' else 0,
        'tmax_max': [{'temp': data, 'station': station, 'date': date}] if data_type == 'TMAX' else [],
        'tmax_total': 1 if data_type == 'TMAX' else 0,
        'tmax_avg': data if data_type == 'TMAX' else None
        }

    print(json.dumps(result))