
<div align="center">
<h1><b>asyncdictionary</b></h1>


[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![PyPI version](https://badge.fury.io/py/asyncdictionary.svg)](https://badge.fury.io/py/asyncdictionary)

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
- Full API coverage
- Organized Responses

## Installation
___
Available through PyPi (pip)

```bash
$ pip install asyncdictionary
```

Or through git.
```bash
$ pip install git+https://github.com/Ay-355/asyncdictionary
```
> Note: if these don't work then try using prefixing them with either `py -m` or `python -m` 

## Documentation
___

As this isn't that big of a lib, the docs are a simple markdown file [located here](Documentation.md).

## Issues
___
**Any issues directly with the API should be reported at the [API's repository page](https://github.com/meetDeveloper/freeDictionaryAPI/issues).**

If there is anything wrong with this package, feel free to open up an issue and explain what happened.

## Examples
___

An example to print out some information about a word
```py
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
___
 - [Documentation](Documentation.md)
 - [PyPi](https://pypi.org/project/asyncdictionary/)
 - [freeDictionaryAPI repository](https://github.com/meetDeveloper/freeDictionaryAPI)
 - [API Home Page](https://dictionaryapi.dev/)


## License
___

[MIT](https://choosealicense.com/licenses/mit/)


## Todo
___
- Add dunder methods (`__str__` & `__repr__`) to all dataclasses.
- Use less dataclasses to make it simpler for end user.

- Add support for non english languages.
    - Might require rewrite of classes to support missing attributes.

- Add some more examples, preferably one in a discord bot.
