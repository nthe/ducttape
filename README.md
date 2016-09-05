## pythe
Bunch of decorators and function I made during code investigation.

__pysk__

Module contains functions for retrieval of values (or lines) from JSON / dictionary or text file. 

Function `parse` has four parameters:
 - source file
 - source file type ( options: json | text )
 - lookup string
 - percentual offset from beginning of file( range: 0 - 100 )
 
When looking for line(s) in text file, the response is list lines containing lookup string.

```python
import pythe
pythe.parse('source.txt', 'text', 'October 13th', 50)
>>> ['Today is October 13th.', 'Another line with sub-string we\'re looking for. It\'s October 13th']
```

When looking for value(s) or property(ies) of dictionary / JSON, the response is list of values where key == lookup string.
```python
import pythe
pythe.parse('data.json', 'json', 'tags', 10)
>>> [['drama', 'comedy', 'thriller'], ['horror', 'thriller', 'drama'], ['documentary', 'nature']] 
```

