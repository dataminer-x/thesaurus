# thesaurus

## Synopsis

Get synonyms, antonyms, or short definitions of a word

## Installation
```
kalliope install --git-url https://github.com/dataminer-x/thesaurus.git
```

## Options

| parameter | required | default | choices                     | comment                                                                                                                           |
|-----------|----------|---------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| word      | yes      |         | E.g: "umpire", "data"       | Any word will do!                                                                          |


## Return Values

| Name       | Description                             | Type   | sample                                                                                                                              |
|------------|-----------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------|
| Synonyms   | Words with the same meaning as the word | list   | [['adjudicator', 'arbiter', 'arbitrator', 'judge', 'referee']]
| Antonyms   | Words with the opposite meaning         | list   | []                                                                                                                      |
| Definition | A short ddefinition of the word         | string | ['']   |


## Synapses example

This synapse will look for the {{ word }} in a thesaurus
```
- name: "thesaurus"
  signals:
    - order: "what's another word for {{ word }}"
  neurons:
    - thesaurus:
        word: "{{ word }}"
    - say:
        - "Another word for {{ word }} is {{ Synonyms }}   

```


```

## Notes


## License

Copyright (c) 2020. All rights reserved.

```