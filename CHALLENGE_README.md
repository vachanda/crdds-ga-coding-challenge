# crdds-ga-coding-challenge
Coding challenge for the Graduate Assistant opening at CRDDS.

## Challenge
Oops! Someone's sed/awk command has gone awry, and stripped all of the whitespace from a directory of text documents! You've been given the task of reconstructing these documents as best as you can.

Write a command line utility called `reconstruct-document` that takes a lexicon and a ruined document, and returns the document with its spaces restored.

### Ruined Documents
You may make the following assumptions about the ruined documents:
* Each document is comprised of one or more sentences, each sentence terminating in a `.`.
* Every sentence will be terminated.
* Documents will contain only the characters `a-z` and `.`. The documents will have no whitespace.
* Every document will have at least one valid reconstruction.

You have been given a collection of example documents in the `ruined-documents/` directory of this repository.

### Lexicon
For this challenge, a lexicon will be a text document with one word per line, that represents all valid words that you may use to reconstruct a document. An example lexicon `example-lexicon.txt` has been provided in this repository as an example.

### Reconstruction
Your document reconstruction must **only replace missing spaces**. Any solution that satisfies the following criteria constitutes a valid reconstruction:
* Missing spaces have been replaced.
* All alphabet characters in the document are used in a word.
* Only words from the lexicon are used.

#### Example
Given the ruined document
```
thequickfoxjumpsoverthelazydog.
```
The following would be a valid reconstruction
```
the quick fox jumps over the lazy dog.
```
if the lexicon contained _(at a minimum)_
```
quick
fox
jumps
over
the
lazy
dog
```

## Requirements
Your submission must satisfy the requirements detailed below.

### Command Line Utility
Build a command line utility called `reconstruct-document` that takes a lexicon and a ruined document, and returns the document with its spaces restored.

The utility will accept three flags, each one taking a filepath to a document:
* `--lexicon`: Filepath to the lexicon being used.
* `--document`: Filepath to the ruined document to reconstruct.
* `--output`: Filepath to which the reconstructed document will be written.

### Test Suite
Write a test suite that exercises your implementation.

### Documentation
Include a README that documents how to build and run your utility, and how to run its test suite.

### Language
You may use the following languages in your implementation: Python, JavaScript, Java.

## Submitting
Once you have completed your implementation, return your solution via email as a compressed file.
