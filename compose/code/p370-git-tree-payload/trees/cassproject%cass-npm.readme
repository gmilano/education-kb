cass-npm

CaSS NPM is the CaSS Library, published and available on NPM.

# Documentation

Documentation for the CaSS Library can be found in the [documentation](documentation/) folder:

* **[Architecture & Walkthrough](documentation/ARCHITECTURE.md)**: An overview of the library's architecture, core components, and common workflows.
* **[Coding Rules & Standards](documentation/RULES.md)**: Guidelines, conventions, and architectural rules for contributors.
* **[Requirements](documentation/REQUIREMENTS.md)**: Project requirements and scope.
* **[Design Patterns](documentation/DESIGN.md)**: Detailed design principles and patterns.


# Getting Started as a user of the library
We're assuming you're coming from the NPM / GitHub space. To see a developer guide, go to https://devs.cassproject.org/

* `npm install --save cassproject`

# Getting Started as a contributor

The CaSS Library is a library, and as such can only be run self-contained against unit tests.

# Dependencies

 * `git clone --recurse-submodules -b <branch> https://github.com/cassproject/cass-npm` - Get the code.
 * `npm i` - Install dependencies.

# Tests
Running `npm test` requires Docker.

## Release testing

  * `npm test` - Runs unit tests in docker images against the CaSS 1.5 repositories using supported Node versions (18+) and Cypress against Edge, Chrome and Electron. Takes some time.

## Development unit testing
Development unit tests presume you have a CaSS Repository running on `localhost:80`. You may get one by running `docker run -d --name cass-test -p80:80 cassproject/cass:1.5.0`

 * `npm automocha` - Runs mocha unit tests against current Node environment. Will rerun unit tests on-save.
 * `npm mocha` - Runs mocha unit tests.
 * `npm webpack:cypress` - Runs unit tests in Cypress against Chrome (headless)
 * `npm webpack:cypressEdge` - Runs unit tests in Cypress against Edge (headless)
 * `npm webpack:cypress:open` - Runs unit tests in Cypress in development mode using webpack packaging. Will rerun unit tests on-save.
 * `npm browserify:cypress:open` - Runs unit tests in Cypress in development mode using browserify packaging. Will rerun unit tests on-save.

## Publish checklist

  * `npm upgrade --save` Review dependencies, autocomplete version numbers to latest versions.
  * Increment version number using `npm version --no-git-tag-version <patch|minor|major>`. This automatically updates `package.json` and `yuidoc.json`.
  * Update changelog using `npm run changelog`, and review the changes in `CHANGELOG.md`.
  * `npm install`
  * `npm audit` and fix any audit issues. Stop if `npm audit --omit=dev` has findings.
  * `npm test` - Must not fail any tests.
  * `npm run webpack:cypressFirefoxHttps` See if the firefox test case has changed.
  * Document code coverage output by the previous step.
  * Commit changes to GitHub.
  * Tag release with semantic version from package.json, push tag.
  * `npm publish` (must be `npm login`ed) 

# Changelog

See [CHANGELOG.md](CHANGELOG.md)
