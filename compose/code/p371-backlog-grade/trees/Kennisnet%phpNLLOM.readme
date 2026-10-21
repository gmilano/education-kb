[![Build Status](https://travis-ci.org/kennisnet/phpNLLOM.svg?branch=master)](https://travis-ci.org/kennisnet/phpNLLOM)

# NL LOM

NL LOM is the Dutch applicationprofile of LOM. This profile was constructed after a project by 
Stichting Kennisnet and SURFfoundation. 

In NL LOM the agreements 'Content-zoekprofiel' and 'LORElom' are merged to form a metadata agreement for 
Dutch education based on IEEE-LOM.

## Summary

This library offers a couple classes to simplify creating and parsing Lom objects and XML.

The Lom class consists of multiple setters/getters which rely on data wrapped in a class. For example, setting the general language uses a value wrapped in a `LomString` object:

```php
<?php
$lom = new NLLOM();
$lom->addGeneralLanguage(new LomString('nl'));
```

There are multiple types of these Lom wrapper classes, which can be found in the `Library` folder. For an example of creating a complete Lom record this way, check the unittest `NLLOMTest.php` in `tests`. 

## Usage

**Creating a new Lom object**

```php
<?php
namespace Example;

use Kennisnet\NLLOM;

//---Example: new lom with some properties set---

// Create an options array: only possible option is 'language', which has a default setting of 'nl'
$options = [
    'language' => 'en'
];

$lom = new NLLOM\NLLOM($options);

$lom->setGeneralTitle(
    new LomMultiLanguage([
        //Create different titles
        new LomLanguageString('Dit is een titel', 'nl'), //override default language
        new LomLanguageString('This is a title')
    ])
);
```

**Converting a Lom object to DomDocument**

```php
<?php
namespace Example;

use Kennisnet\NLLOM;

//---Example: convert lom  object to XML ---
$lom = new NLLOM\NLLOM();

$mapper = new NLLOM\LomToDomMapper();
$dom = $mapper->lomToDom($lom);

$result = $dom->saveXML();
```

**Converting existing Lom XML/DomDocument to Lom object** 
```php
<?php
namespace Example;

use Kennisnet\NLLOM;

//---Example: convert DomDocument to lom object ---
$domDocument = new \DOMDocument('1.0', 'utf-8');
$domDocument->load('lom_example.xml');

$mapper = new NLLOM\DomToLomMapper();
$lom = $mapper->domToLom($domDocument);
```

**Validation**
```php
<?php
namespace Example;

use Kennisnet\NLLOM;

//---Example: validate Lom XML

$xml = <<<XML
<?xml version="1.0" encoding="UTF-8"?>
<lom xmlns="http://www.imsglobal.org/xsd/imsmd_v1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsmd_v1p2 http://www.imsglobal.org/xsd/imsmd_v1p2p4.xsd">
    <general>
        <title>
            <langstring xml:lang="nl">Foobar</langstring>
        </title>
    </general>
</lom>
XML;

NLLOM\Validator::validate($xml);
```


## Links

[Kennisnet Developers Wiki](https://developers.wiki.kennisnet.nl/index.php?title=Standaarden:NL_LOM)

[NL LOM](https://wiki.surfnet.nl/display/nllom/Home)
