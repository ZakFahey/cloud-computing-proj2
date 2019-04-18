#!/usr/bin/env python
import sys
import json

result = {
    total_tmin: float('inf'),
    total_tmin_station: None,
    total_tmax: float('-inf'),
    total_tmax_station: None,
    by_year: {}
    }

for line in sys.stdin:
    mapper_input = json.loads(line)
    if mapper_input['total_tmin'] < result['total_min']:
        result['total_tmin'] = mapper_input['total_tmin']
        result['total_tmin_station'] = mapper_input['total_tmin_station']
    if mapper_input['total_tmax'] > result['total_max']:
        result['total_tmax'] = mapper_input['total_tmax']
        result['total_tmax_station'] = mapper_input['total_tmax_station']

    for key in mapper_input['by_year'].keys():
        if key not in result['by_year']:
            result['by_year'][key] = mapper_input['by_year'][key]
        else:
            mapper_year = mapper_input['by_year'][key]
            result_year = result['by_year'][key]
            
            result_year['tmin_sum'] += mapper_year['tmin_sum']
            result_year['tmin_min'] = min(result_year['tmin_min'], mapper_year['tmin_min'])
            result_year['tmin_total'] += mapper_year['tmin_total']
            result_year['tmin_avg'] += result_year['tmin_sum'] / result_year['tmin_total'] if result_year['tmin_total'] > 0 else None
            result_year['tmax_sum'] += mapper_year['tmax_sum']
            result_year['tmax_max'] = max(result_year['tmax_max'], mapper_year['tmax_max'])
            result_year['tmax_total'] += mapper_year['tmax_total']
            result_year['tmax_avg'] += result_year['tmax_sum'] / result_year['tmax_total'] if result_year['tmax_total'] > 0 else None
            # TODO: 5 hottest , 5 coldest weather stations for each year excluding abnormalities or missing data 


print(json.dumps(result))