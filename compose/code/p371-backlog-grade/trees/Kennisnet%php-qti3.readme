# PHP QTI 3.0 Library

This library provides functionality for reading, writing and manipulating QTI 3.0 packages, assessment tests and assessment items.

## Installation

You can install the library via Composer:

```bash
composer require wikiwijs/php-qti3
```

## Usage

The library uses the `QtiClient` as a service container for accessing various services.

### Initializing the QtiClient

To use the library, you first need to initialize the `QtiClient` with the required dependencies. The library provides default implementations using PSR interfaces and Flysystem.

#### Required implementations

The `QtiClient` expects three implementations:

1.  **IFilesystemPackageFactory**: For reading and writing files to a (temporary) file system.
2.  **IResourceValidator**: For validating external resources (e.g. URLs).
3.  **IResourceDownloader**: For downloading external resources to the local file system.

#### Example with default implementations

The implementations below are available in the library but may require additional composer packages (see the `suggest` section in `composer.json`).

```php
use League\Flysystem\Local\LocalFilesystemAdapter;
use League\Flysystem\Filesystem;
use Qti3\QtiClient;
use Qti3\Package\Filesystem\FlysystemPackageFactory;
use Qti3\Package\Validator\Resource\PsrHttpClientResourceValidator;
use Qti3\Package\Downloader\Resource\PsrHttpClientResourceDownloader;
use Qti3\Package\Filesystem\FileSystemUtils;

// 1. Setup Flysystem (e.g. local file system)
// Required: composer require league/flysystem
$adapter = new LocalFilesystemAdapter('/tmp/qti-data');
$filesystem = new Filesystem($adapter);
$filesystemPackageFactory = new FlysystemPackageFactory($filesystem);

// 2. Setup PSR-18 HTTP Client and PSR-17 Request Factory
// E.g. Symfony's HTTP Client: composer require symfony/http-client psr/http-client nyholm/psr7
$httpClient = new \Symfony\Component\HttpClient\Psr18Client();
$requestFactory = new \Nyholm\Psr7\Factory\Psr17Factory();

// 3. Initialize the validator and downloader
$resourceValidator = new PsrHttpClientResourceValidator($httpClient, $requestFactory);
$resourceDownloader = new PsrHttpClientResourceDownloader(
    new FileSystemUtils(),
    $httpClient,
    $requestFactory,
    '/tmp/qti-data' // Folder where downloads are stored
);

// 4. Create the QtiClient
$qtiClient = new QtiClient(
    $filesystemPackageFactory,
    $resourceValidator,
    $resourceDownloader,
);
```

### QTI Package Level

**UC-P1: Import QTI3 package in ZIP format to package object**

```php
$qtiPackageReader = $qtiClient->getQtiPackageReader();
$qtiPackage = $qtiPackageReader->fromZip('/tmp/qti3.zip');
// $qtiPackage is now of type Qti3\Package\Model\QtiPackage
```

**UC-P2: Import QTI3 package from folder to package object**

```php
$qtiPackageReader = $qtiClient->getQtiPackageReader();
$qtiPackage = $qtiPackageReader->fromFilesystem('/tmp/folder');
// $qtiPackage is now of type Qti3\Package\Model\QtiPackage
```

**UC-P3: Generate ZIP file from package object**

```php
$zipPackageFactory = $qtiClient->getZipPackageFactory();
$writer = $zipPackageFactory->getWriter('/tmp/qti3.zip');
$writer->write($qtiPackage);
```

**UC-P4: Generate folder from package object**

```php
$filesystemPackageFactory = $qtiClient->getFilesystemPackageFactory();
$writer = $filesystemPackageFactory->getWriter('/tmp/folder');
$writer->write($qtiPackage);
```

**UC-P5: Validate a QTI package**

```php
$validator = $qtiClient->getQtiPackageValidator();
$errors = $validator->validate($qtiPackage);

if ($errors->count() > 0) {
    // $errors is a StringCollection of validation error messages
}
```

By default the library uses an XSD-based syntax validator (`QtiSchemaValidator`). To use the official **IMS Global QTI validator** (Docker image) instead, pass a custom `IQtiSyntaxValidator` implementation as the fourth argument to `QtiClient`. See [docs/ims-global-validator.md](docs/ims-global-validator.md) for setup instructions and a ready-to-use skeleton class.

Besides schema conformance, every assessment item is checked for *scorability* (`ScoringOutcomeValidator`, run by `initItemState()`, see UC-I3). For a question item this enforces that:

- a `qti-response-processing` element — inline, empty or template-based — is matched by a `qti-outcome-declaration` with identifier `SCORE` (a player only enables checking an item when the `SCORE` variable exists);
- inline response processing actually sets `SCORE` (unless the item is scored manually, i.e. only has a `qti-extended-text-interaction`);
- `MAXSCORE` is declared with a numeric, non-negative default (again, unless scored manually).

All violations of one item are reported together, each prefixed with the item's file path, e.g. ``QUE_4_1.xml: Missing `qti-outcome-declaration` with identifier `SCORE` ``.

**UC-P6: Add, update or reorder items in a package**

`getPackageEditor()` returns a `PackageEditor` that edits the assessment items and the test-level rubric blocks of a `QtiPackage` **in place**. It does no filesystem I/O: you load the package, edit it, and save it yourself. Items are passed as typed `AssessmentItem` models — you build or parse them (see UC-I1). Adding an item assigns it the next free `ITEMnnn` identifier by default (or one you pass). Each operation is *surgical*: adding or reordering rewrites a single assessment test (named by its resource identifier `$testId`, so packages with more than one test are supported) and, for an add, appends one item resource; updating replaces a single item resource. Untouched items, media and metadata are left exactly as they are. Editing never refuses an imperfect package: a construct the model cannot hold is dropped on regeneration and reported through the returned `EditResult`'s `warnings` (parsing an item likewise returns an `ItemParseResult` with `item` + `warnings`).

> **See [docs/package-editor.md](docs/package-editor.md)** for worked examples of adding an item from an XML string, updating, removing and reordering items, reading the test model with `parseTest()` and replacing test-level rubric blocks with `setTestRubricBlocks()`, an errors table and notes.

```php
$package = $qtiClient->getQtiPackageReader()->fromFilesystem('/tmp/folder');
$editor  = $qtiClient->getPackageEditor();
$parser  = $qtiClient->getAssessmentItemParser();

// The resource identifier of the test to edit. For a single-test package:
$testId = $package->getAssessmentTestIdentifier();

// Build the item model from your QTI 3 item XML string ($parsed->item), and
// inspect $parsed->warnings for anything the model could not keep.
$parsed = $parser->parseFromString($itemXml);

// Add it; the editor assigns the next free identifier. Returns an EditResult.
$added = $editor->addItemToTest($package, $testId, $parsed->item);
// $added->resource->identifier is 'ITEM001'; $added->warnings covers the edited test.

// Pass your own identifier and/or a zero-based position (default: next id, append).
$editor->addItemToTest($package, $testId, $parsed->item, identifier: 'ITEM042', position: 0);

// Update an existing item's content. The model's own identifier selects the
// item to replace, so parse XML that carries identifier="ITEM001".
$editor->updateItem($package, $parser->parseFromString($updatedItemXml)->item);

// Remove an item from the test.
$editor->removeItemFromTest($package, $testId, 'ITEM001');

// Reorder the items of the assessment test section.
$editor->reorderItemsInTest($package, $testId, ['ITEM002', 'ITEM001']);

// Persist the edited package (folder or ZIP).
$qtiClient->getFilesystemPackageFactory()->getWriter('/tmp/folder')->write($package);
```

Removing an item drops its ref from the named test and, unless another test still references it, deletes the item resource and its file; media the item introduced is left in place. Because editing is surgical, untouched items, media and metadata are left as they are — an unrelated item that uses a construct the typed models cannot represent does not affect editing. A construct the model cannot hold (nested sections, a template declaration, an unconsumed attribute, an outcome rule whose expression the model does not know, ...) is not refused: it is dropped when the XML is regenerated and reported via the `warnings` on `EditResult`/`ItemParseResult`. Test-level rubric blocks, `qti-outcome-processing` and `qti-test-feedback` are kept: they are parsed into `AssessmentTest::$rubricBlocks`, `AssessmentTest::$outcomeProcessing` and `AssessmentTest::$testFeedback` and re-emitted unchanged, including a multi-valued `view` (`view="candidate scorer"`). An unsupported *interaction type* still fails earlier, in the parser, with a `ParseError` (see *Supported interactions* below).

Adding an item whose identifier already exists in the package throws `InvalidAssessmentTestException`; editing a non-existent test or updating a non-existent item throws `ResourceNotFoundException`; an order that does not match the items in the test throws `InvalidItemOrderException`. Media that the added or updated item references is carried over (files already in the package) or registered as new webcontent, without duplicating resources.

### Assessment Test Level

**UC-T1: Generate test from package**

```php
$testBuilder = $qtiClient->getTestBuilder();
$result = $testBuilder->buildFromPackage($qtiPackage);
$test = $result->test;          // Qti3\AssessmentTest\Model\AssessmentTest
$warnings = $result->warnings;  // constructs the model could not keep
// Pass a test resource identifier as the second argument to select one test
// in a multi-test package: buildFromPackage($qtiPackage, $testId).
```

`buildFromPackage()` returns a `TestParseResult` (`test` + `warnings`). A construct the model cannot represent losslessly (nested sections, an unknown attribute, ...) is not refused: it is dropped on the round-trip and reported in `warnings`. Test-level `qti-rubric-block` elements are represented: they are kept in `AssessmentTest::$rubricBlocks` and survive the round-trip. Their `view` attribute is the schema's list of views (`RubricBlock::$views`, with `hasView()` to test one) and `use` is optional (`RubricBlock::$use` is `null` when the attribute is absent); an `ext:` use value cannot be represented and is dropped with a warning. `qti-outcome-processing` (`AssessmentTest::$outcomeProcessing`: `qti-set-outcome-value`, `qti-lookup-outcome-value`, `qti-exit-test` and `qti-outcome-condition` with any number of rules per branch, expressions including `qti-test-variables`) and `qti-test-feedback` (`AssessmentTest::$testFeedback`) survive the round-trip too. A top-level outcome rule the model cannot hold, for instance one built on `qti-number-correct`, is dropped on its own with a warning that names it; inside a `qti-outcome-condition` the whole condition is dropped, because keeping the other branches would silently change what the test scores.

**UC-T2: Generate package from test**

```php
// $test is of type Qti3\AssessmentTest\Model\AssessmentTest
// $items is an array of Qti3\AssessmentItem\Model\AssessmentItem
$packageBuilder = $qtiClient->getQtiPackageBuilder();
$package = $packageBuilder->buildForTest($test, $items);
// $package is now of type Qti3\Package\Model\QtiPackage
```

**UC-T3: HTML fragment ↔ content model**

A rich-text editor hands you HTML as a string; the model wants a `ContentBody`. `getHtmlFragmentParser()` and `getHtmlFragmentSerializer()` convert in both directions so an application never builds DOM of its own — for instance to store student instructions as a test-level `qti-rubric-block`:

```php
$contentBody = $qtiClient->getHtmlFragmentParser()->parse('<p>Lees eerst de <strong>hele</strong> vraag.</p>');
$block = new RubricBlock(qtiUse::INSTRUCTIONS, new ViewCollection([View::CANDIDATE]), $contentBody);

$editor = $qtiClient->getPackageEditor();
$parsed = $editor->parseTest($package, $testId);
$kept = array_filter($parsed->test->rubricBlocks->all(), fn (RubricBlock $existing) => !$existing->hasView(View::CANDIDATE));
$editor->setTestRubricBlocks($package, $testId, new RubricBlockCollection([...$kept, $block]));

$html = $qtiClient->getHtmlFragmentSerializer()->serialize($block->contentBody); // '<p>Lees eerst de <strong>hele</strong> vraag.</p>'
```

`parse()` is lenient about markup but strict about content. Markup goes through PHP's HTML5 parser (`Dom\HTMLDocument`), which repairs an editor's output the way a browser does: unclosed tags, valueless boolean attributes (`<details open>` becomes `open="true"`), `&nbsp;`, a stray `</body>`. Content is then checked against the model: a tag or attribute outside the QTI HTML whitelist throws `InvalidArgumentException`, including a tag that cannot stand on its own at the top of a content body (a stray `<li>`, or a MathML element other than the `<math>` root). Parsing a package is more forgiving: a content body keeps such a tag as authored and reports it as a warning, so an imperfect package stays readable. An item body rejects it in its constructor either way, because the generators that build one write packages and a wrong tag there would travel. A content body holds flow content; pass a rule as the third argument to author for a target with a narrower content model — an item body takes block content only:

```php
$contentBody = $qtiClient->getHtmlFragmentParser()->parse($html, $warnings, ItemBody::allowsAsDirectChild(...));
$itemBody = new ItemBody($contentBody->content); // <strong>vet</strong> at the top would have thrown
```

Note that `style` is not a QTI attribute, so strip presentational markup in the editor before calling `parse()`. Pass a `StringCollection` as the second argument to collect the parser's warnings. Those report markup the HTML5 tree construction could not place and therefore dropped — a `<td>` outside a table, for instance; markup a browser repairs silently is repaired silently here too, and MathML and HTML5 elements parse without complaint.

Whitespace is treated the way a browser renders it: the space between two inline elements (`<strong>vet</strong> <em>cursief</em>`) is content and is kept, while whitespace around block elements — indentation between `</p>` and `<p>`, or just inside a `<p>` — is layout and is dropped. Comments are preserved; a `--` inside one is written back as `- -`, because XML cannot represent it and the package would otherwise no longer parse.

`serialize()` emits XHTML-style markup (`<br/>`, raw U+00A0 rather than `&nbsp;`) and never re-indents. A round trip is faithful rather than byte-identical: an `<img>` without `alt` comes back with `alt=""`, because QTI requires it.

### Assessment Item Level

**UC-I1: Parse item XML to model**

```php
$assessmentItemParser = $qtiClient->getAssessmentItemParser();

// From a DOMElement:
$result = $assessmentItemParser->parse($itemElement);

// Or directly from an XML string (throws ParseError on malformed XML):
$result = $assessmentItemParser->parseFromString($itemXml);

$item = $result->item;          // Qti3\AssessmentItem\Model\AssessmentItem
$warnings = $result->warnings;  // constructs the model could not keep from the source
```

Each warning locates the offending element (line number + identifier-based selector); pass a source label to `parseFromString($xml, $source)` to prefix them with a filename.

**UC-I2: Generate XML from item**

```php
// $item is of type Qti3\AssessmentItem\Model\AssessmentItem
$xmlBuilder = $qtiClient->getXmlBuilder();
$itemXml = $xmlBuilder->generateXmlFromObject($item);
// $itemXml is now of type DomDocument
```

**UC-I3: Response processing**

```php
// $responses is an associative array with response-identifier->value
$responseProcessor = $qtiClient->getResponseProcessor();
$itemState = $responseProcessor->initItemState($itemXml);
$responseProcessor->processResponses($itemState, $responses);
$outcomes = $itemState->outcomeSet->outcomes;
// $outcomes is now an associative array with outcome-identifier->value
```

`initItemState()` validates the item before returning its state: every scoring violation (see UC-P5) and every response processing violation is collected and thrown at once as an `InvalidAssessmentItemException`, whose `validationErrors()` lists them. Malformed processing XML still throws a `ParseError`.

### Supported interactions

The `AssessmentItem` parser supports exactly the interaction types listed below via the `InteractionParser` used by `ItemBodyParser`. Other QTI 3.0 interaction types (e.g. `qti-associate-interaction`, `qti-slider-interaction`, `qti-media-interaction`, the graphic interactions) are **not** supported: parsing such an item throws a `ParseError`, and the item editor (UC-P6) refuses packages containing them.

- `qti-choice-interaction`
- `qti-text-entry-interaction`
- `qti-extended-text-interaction`
- `qti-gap-match-interaction`
- `qti-hotspot-interaction`
- `qti-hottext-interaction`
- `qti-inline-choice-interaction`
- `qti-match-interaction`
- `qti-order-interaction`
- `qti-select-point-interaction`

## Running Tests

You can run the unit tests with the following Composer command:

```bash
composer test
```
