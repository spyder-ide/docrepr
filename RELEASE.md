To release a new version of docrepr on PyPI:

* Close the current milestone on Github

* git pull or git fetch/merge

* git clean -xfdi

* Update CHANGELOG.md

* Update _version.py (set release version, remove 'dev')

* git add and git commit with `Release X.X.X`

* python setup.py sdist upload

* python setup.py bdist_wheel upload

* git tag -a vX.X.X -m 'Release X.X.X'

* Update _version.py (add 'dev' and increment minor)

* git add and git commit

* git push upstream master

* git push upstream --tags
