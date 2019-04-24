# Cloud Computing Project 2

This repository contains the mapper and reducer functions to get the temperature data for the noaa.gov data set. It also includes `result.json`, my results when running the program, and `result_parser.py`, which takes the JSON data and converts it into more readable Markdown tables.

To run the analysis, copy `mapper.py` and `reducer.py` to the Hadoop gate and run the command

```hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /user/tatavag/weather/* -output proj2-output```

The output can be found in the `proj2-output` directory. If you want to test the code locally, you can also use the sample data provided and run the command

```cat test.txt | python mapper.py | python reducer.py```
