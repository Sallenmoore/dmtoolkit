# dmtoolkit

!!!!!!!!!!!!!!!!!!!! NOT YET STABLE !!!!!!!!!!!!!!!!!!!!!!!!

![Tests](https://github.com/Sallenmoore/autonomous/actions/workflows/tests.yml/badge.svg)

TBD

- **pypi**: https://test.pypi.org/project/autonomous
- **github**: https://github.com/Sallenmoore/autonomous

## Features

- TBD

## Dependencies

- **Languages**
  - [Python 3.10](/Dev/language/python)
- **Frameworks**
  - [Autonomous](https://github.com/Sallenmoore/autonomous)
  - [gql](#)
- **Containers**
  - [Docker](https://docs.docker.com/)
  - [Docker Compose](https://github.com/compose-spec/compose-spec/blob/master/spec.md)
- **Networking and Serialization**
  - [requests](https://requests.readthedocs.io/en/latest/)
- **Testing**
  - [pytest](/Dev/tools/pytest)
  - [coverage](https://coverage.readthedocs.io/en/6.4.1/cmd.html)
- **Documentation** - Coming Soon
  - [pdoc](https://pdoc.dev/docs/pdoc/doc.html)
  - [highlight.js](https://highlightjs.org/)

---

## Developer Notes

## {.tabset}

### TODO

- Auto generate API documentation
- Setup/fix template app generator
- Add type hints
- Switch to less verbose html preprocessor
- Add more database options
- Improve database search
- 100% testing coverage

### Issue Tracking

- None

## Commands

### Generate app

TDB

### Tests

```sh
make tests
```

### package

1. Update version in `/src/autonomous/__init__.py`
2. ```sh
   make tests
   ```
