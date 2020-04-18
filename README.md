# thesaurus

## Synopsis

Get synonyms, antonyms, or short definitions of a word

## Installation
```
kalliope install --git-url https://github.com/dataminer-x/thesaurus.git
```

## Options

| parameter | required | default | choices                     | comment                                                 |                            
|-----------|----------|---------|-----------------------------|---------------------------------------------------------|
| word      | yes      | none    | E.g: "umpire", "data"       |Any word will do!                                        |
| api_key   | yes      | none    | api key stored in variables |From dictionaryapi.com - this should be a thesaurus key  |
 

## Return Values

| Name       | Description                             | Type   | sample                                                       |
|------------|-----------------------------------------|--------|--------------------------------------------------------------|
| Synonyms   | Words with the same meaning as the word | list   | [['adjudicator', 'arbiter', 'arbitrator', 'judge', 'referee']]
| Antonyms   | Words with the opposite meaning         | list   | []                                                                                                                      |
| Definition | A short definition of the word         | string | ['']   |


## Synapses example

This synapse will look for synonyms of a {{ word }}
```
  - name: "thesaurus"
    signals:
        - order: "what's another word for {{ word }}"
        - api_key: "{{ api_key }}"
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