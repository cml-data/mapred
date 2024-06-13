# mapred 
M(app)er (and) R(educ)er

Both versions were tested with the books dataset we used in class on the Google Cloud Comput Engine VM built last week.
Hadoop mapred used (https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)

## Version 1
[G4G](https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/) with comments removed, utf tag added, and converted to Python3. 

Works over text files with a Python3 installed and execute permissions.

Removes URL strings and roman numerals.  Keeps most hyphenated words.

```
mapred streaming \
  -input <path to text files> \
  -output <path to output directory> \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py
```

## Version 2
Written in bash (mapper.sh and reducer.sh)
Performance is much slower than the Python version.  Much stricter in removing strings with unwanted characters.

```
mapred streaming \
  -input <path to text files> \
  -output <path to output directory> \
  -mapper mapper.sh \
  -reducer reducer.sh \
  -file mapper.sh \
  -file reducer.sh
```
