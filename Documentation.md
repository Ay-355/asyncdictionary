# Documentation
An asynchronous wrapper for freeDictionaryAPI.

**IMPORTANT: This is not my API. This is merely a wrapper. Any issues with the API should be reported at the [API's repository](https://github.com/meetDeveloper/freeDictionaryAPI).**

---

# Getting Started
---
First install the package using either:
- `pip install asyncdictionary`
- `python -m pip install asyncdictionary`

---
### Then you have to initiate an instance of the client

```py
import asyncdictionary
# create an instance of `Client`
dictionary = asyncdictionary.Client()
```
> If you have a [ClientSession], you may pass that in as a kwarg instead.

# Usage
---

### *await* Client.get_word(word)

This is essentially all the information that a raw request to the API will return to you. Gives everything that the http API will give you including the definitions and phonetics.

#### Parameters
- word ([str]) - The word you want the information of.

#### Returns

[Word]

---

### *await* Client.get_meanings(word)

This returns the definitions and the part of speech of that definition. Does **NOT** give the phonetics or the word itself.

#### Parameters
- word ([str]) - The word you want the meaning of.

#### Returns

List[[Meaning]]

---

### *await* Client.get_phonetics(word)

This returns the phonetics of the word. Does not give anything else.

### Parameters
- word([str]) - The word you want the phonetics of

#### Returns

List[[Phonetic]]

---

### *await* Client.get_pronunciations(word)

An alias to [Client.get_phonetics](#await-Client.get_phonetics(word))
See that for more information.

---

### *await* Client.close()

Closes the Client.

---

# Objects

Explains what exactly the methods return

> **NOTE:** Some of the attributes might return `None` if nothing was given by the API.

## Word
---
The object returned from `Client.get_word` method.

### Word.word
The word inputted

### Word.phonetics

A [list] of [Phonetic] objects the word has.

### Word.meanings

A [list] of [Meaning] objects.

---

## Phonetic
---
The object returned from `Client.get_phonetics` and `Word.phonetics`

### Phonetic.text
The text representation of the pronunciation of the word.

### Phonetic.audio
A link to the audio speech of the word.

---

## Meaning
---
The object returned from `Client.get_meanings` and `Word.meanings`

### Meaning.part_of_speech

The part of speech for a certain definition.

### Meaning.definitions

A [list] of [Definition] objects. The API returns multiple definitions of a word, hence the list of `Definition` objects

---

## Definition
---
The object returned from `Meaning.definitions`

### Definition.definition

A definition of the word.

### Definition.example

An example of how the word is used.

### Definition.synonyms
A [list] of words that are synonyms to the word or `None` if there were none given.

---



[str]: https://docs.python.org/3/library/stdtypes.html#str

[list]: https://docs.python.org/3/library/stdtypes.html#list

[ClientSession]: https://docs.aiohttp.org/en/stable/client_reference.html?aiohttp.ClientSession

[Word]: Documentation.md#word

[Meaning]: Documentation.md#meaning

[Phonetic]: Documentation.md#phonetic

[Definition]: Documentation.md#definition
