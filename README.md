## pythe
Basic utilities I use.

### __pysk__

Module contains functions for retrieval of values (or lines) from JSON / dictionary or text file. The advantage is that the source file won't be loaded into main memory and may work with invalid JSON(s) / dictionary(ies).

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

### __pymin__

Simple Python script minifier.

```python
import pymin
pymin.minify('source.py', 'min_source.py')
```
