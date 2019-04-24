import json

tableData = {}

with open('result.json', 'r') as file:
    result = json.loads(file.read())

for check in ['tmax_max', 'tmin_min']:
    tableData[check] = ''
    for year in range(2000, 2020):
        info = result['by_year'][str(year)]
        tableData[check] += '|' + str(year) + '|' + str(round(info['tmax_avg' if check == 'tmax_max' else 'tmin_avg'], 1)) + '*C|'
        for i in info[check]:
            tableData[check] += str(i['temp']) + '*C<br>' + i['station'] + '<br>' + i['date'][4:6] + '/' + i['date'][6:8] + '|'
        tableData[check] += '\n'



print('|Year|Avg TMAX|1st hottest TMAX|2nd hottest TMAX|3rd hottest TMAX|4th hottest TMAX|5th hottest TMAX|')
print('|--|--|--|--|--|--|--|')
print(tableData['tmax_max'])
print('|Year|Avg TMIN|1st coldest TMIN|2nd coldest TMIN|3rd coldest TMIN|4th coldest TMIN|5th coldest TMIN|')
print('|--|--|--|--|--|--|--|')
print(tableData['tmin_min'])