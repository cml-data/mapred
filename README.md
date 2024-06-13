# mapred 
M(app)er (and) R(educ)er

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


2nd version written in bash (mapper.sh and reducer.sh)
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
