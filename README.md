
<div align="center">
<h1><b>asyncdictionary</b></h1>


[![MIT License](https://img.shields.io/pypi/l/asyncdictionary.svg)](https://spdx.org/licenses/MIT.html)
[![PyPI version](https://badge.fury.io/py/asyncdictionary.svg)](https://pypi.python.org/pypi/asyncdictionary)
[![PyPi Downloads](http://pepy.tech/badge/asyncdictionary)](http://pepy.tech/project/asyncdictionary)

<h3>An asynchronous Python wrapper for https://dictionaryapi.dev/</h3>

</div>

___

> #### **NOTE: Currently I have only implemented fetching words from English, not other languages. This is because the actual API's implementation of languages other than english is different. Support for different languages coming soon though.**


___
## Requirements

- Python 3.6+
- aiohttp

## Features

- Asynchronous
- Typed
- Easy to use

## Installation

Available through PyPi (pip)

```bash
$ pip install asyncdictionary
```

Or through git.
```bash
$ pip install git+https://github.com/Ay-355/asyncdictionary
```
> You might have to do `python3 -m pip`

## Documentation

You can find a markdown file [here](Documentation.md).

## Issues

**Any issues directly with the API should be reported at the [API's repository page](https://github.com/meetDeveloper/freeDictionaryAPI/issues).**

If there is anything wrong with this package, feel free to open up an issue and explain what happened.

## Examples

An example to print out some information about a word
```python3
import asyncdictionary
import asyncio

# create an instance of the client
dictionary = asyncdictionary.Client()

async def word_info(word):
    word = await dictionary.get_word(word) # get a Word object
    print(f"Word: {word.word}")
    print(f"Phonetic text: {word.phonetics[0].text}")
    print(f"Part of Speech: {word.meanings[0].part_of_speech}")
    print(f"Definition: {word.meanings[0].definitions[0].definition}")
    print(f"Synonyms: {', '.join(word.meanings[0].definitions[0].synonyms)}")
    print(f"Example: {word.meanings[0].definitions[0].example}")

asyncio.run(word_info("hello"))
```

## Links

 - [Documentation](Documentation.md)
 - [PyPi](https://pypi.org/project/asyncdictionary/)
 - [freeDictionaryAPI repository](https://github.com/meetDeveloper/freeDictionaryAPI)
 - [API Home Page](https://dictionaryapi.dev/)


## License

[MIT](https://choosealicense.com/licenses/mit/)
