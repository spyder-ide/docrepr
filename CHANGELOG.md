# Changelog

All notable changes to this project will be documented in this file.
[Loghub](https://github.com/spyder-ide/loghub) is used to help generate it.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).



## [0.2.0] - 2022-01-29

Thanks to @SylvainCorlay, @martinRenou, @fasiha and the QuantStack team for helping make this release possible!


### Highlights

* Update to work again with modern Python, IPython, Sphinx and Matplotlib
* Fix multiple significant outstanding issues and enhance functionality
* Add CIs, test suite and visual regression checks
* Overhaul packaging to follow modern standards and best practices
* Add/rewrite user and developer documentation and metadata
* Conform project to up to date conventions
* Other smaller improvements and maintenance


### Issues Closed

* [Issue 42](https://github.com/spyder-ide/docrepr/issues/42) - Release Docrepr 0.2.0 ([PR 44](https://github.com/spyder-ide/docrepr/pull/44) by [@CAM-Gerlach](https://github.com/CAM-Gerlach))
* [Issue 39](https://github.com/spyder-ide/docrepr/issues/39) - Improve tests to actually check that the rendered content is what we expected ([PR 41](https://github.com/spyder-ide/docrepr/pull/41) by [@martinRenou](https://github.com/martinRenou))
* [Issue 37](https://github.com/spyder-ide/docrepr/issues/37) - Update and standardize documentation and meta-files (Readme, Contributing, Authors, Release Guide, etc) ([PR 43](https://github.com/spyder-ide/docrepr/pull/43) by [@CAM-Gerlach](https://github.com/CAM-Gerlach))
* [Issue 34](https://github.com/spyder-ide/docrepr/issues/34) - Docrepr doesn't understand Sphinx ":type" and ":param" directives? ([PR 36](https://github.com/spyder-ide/docrepr/pull/36) by [@CAM-Gerlach](https://github.com/CAM-Gerlach))
* [Issue 31](https://github.com/spyder-ide/docrepr/issues/31) - Matplotlib images not located properly ([PR 32](https://github.com/spyder-ide/docrepr/pull/32) by [@martinRenou](https://github.com/martinRenou))
* [Issue 29](https://github.com/spyder-ide/docrepr/issues/29) - Get rid of the Matplotlib's plot_directive copy ([PR 30](https://github.com/spyder-ide/docrepr/pull/30) by [@martinRenou](https://github.com/martinRenou))
* [Issue 26](https://github.com/spyder-ide/docrepr/issues/26) - Docrepr fails with Sphinx v4 ([PR 30](https://github.com/spyder-ide/docrepr/pull/30) by [@martinRenou](https://github.com/martinRenou))
* [Issue 24](https://github.com/spyder-ide/docrepr/issues/24) - Add basic CI checks via GitHub Actions to run tests and validate packaging ([PR 33](https://github.com/spyder-ide/docrepr/pull/33) by [@CAM-Gerlach](https://github.com/CAM-Gerlach))
* [Issue 23](https://github.com/spyder-ide/docrepr/issues/23) - Update tests to use Pytest as a runner and fix/modernize as needed ([PR 33](https://github.com/spyder-ide/docrepr/pull/33) by [@CAM-Gerlach](https://github.com/CAM-Gerlach))
* [Issue 22](https://github.com/spyder-ide/docrepr/issues/22) - Update packaging metadata, release guide and infra to avoid deprecated practices and follow current standards ([PR 33](https://github.com/spyder-ide/docrepr/pull/33) by [@CAM-Gerlach](https://github.com/CAM-Gerlach))
* [Issue 20](https://github.com/spyder-ide/docrepr/issues/20) - Sphinxify licensing ([PR 43](https://github.com/spyder-ide/docrepr/pull/43) by [@CAM-Gerlach](https://github.com/CAM-Gerlach))
* [Issue 19](https://github.com/spyder-ide/docrepr/issues/19) - Is this package abandoned?
* [Issue 16](https://github.com/spyder-ide/docrepr/issues/16) - sphinx 1.8 fails when srcdir and output dir are the same
* [Issue 12](https://github.com/spyder-ide/docrepr/issues/12) - Signature is not displayed for function objects ([PR 40](https://github.com/spyder-ide/docrepr/pull/40) by [@CAM-Gerlach](https://github.com/CAM-Gerlach))

In this release, 14 issues were closed.


### Pull Requests Merged

* [PR 44](https://github.com/spyder-ide/docrepr/pull/44) - Release Docrepr 0.2.0 [@CAM-Gerlach](https://github.com/CAM-Gerlach) ([37](https://github.com/spyder-ide/docrepr/issues/37), [20](https://github.com/spyder-ide/docrepr/issues/20))
* [PR 43](https://github.com/spyder-ide/docrepr/pull/43) - Add contributing guide/docs & security policy, and update/standardize readme, release guide, license info, & links, by [@CAM-Gerlach](https://github.com/CAM-Gerlach) ([37](https://github.com/spyder-ide/docrepr/issues/37), [20](https://github.com/spyder-ide/docrepr/issues/20))
* [PR 41](https://github.com/spyder-ide/docrepr/pull/41) - Add visual regression tests with playwright, by [@martinRenou](https://github.com/martinRenou) ([39](https://github.com/spyder-ide/docrepr/issues/39))
* [PR 40](https://github.com/spyder-ide/docrepr/pull/40) - Fix and improve definition extraction, avoid deprecated/removed calls and clean up other issues, by [@CAM-Gerlach](https://github.com/CAM-Gerlach) ([12](https://github.com/spyder-ide/docrepr/issues/12))
* [PR 36](https://github.com/spyder-ide/docrepr/pull/36) - Add ability to render Sphinx-format docstrings, by [@CAM-Gerlach](https://github.com/CAM-Gerlach) ([34](https://github.com/spyder-ide/docrepr/issues/34))
* [PR 35](https://github.com/spyder-ide/docrepr/pull/35) - Ignore spurious ResourceWarning in tests when opening the rendered result in the browser on Linux, by [@martinRenou](https://github.com/martinRenou)
* [PR 33](https://github.com/spyder-ide/docrepr/pull/33) - Add tests and CIs, upgrade packaging and metafiles, drop Py2 and add Py3.10, standardize infra and config, and more, by [@CAM-Gerlach](https://github.com/CAM-Gerlach) ([24](https://github.com/spyder-ide/docrepr/issues/24), [23](https://github.com/spyder-ide/docrepr/issues/23), [22](https://github.com/spyder-ide/docrepr/issues/22), [17](https://github.com/spyder-ide/docrepr/issues/17))
* [PR 32](https://github.com/spyder-ide/docrepr/pull/32) - Merge Sphinx build destination and source directory, by [@martinRenou](https://github.com/martinRenou) ([31](https://github.com/spyder-ide/docrepr/issues/31))
* [PR 30](https://github.com/spyder-ide/docrepr/pull/30) - Remove plot_directive and use the one from Matplotlib, by [@martinRenou](https://github.com/martinRenou) ([29](https://github.com/spyder-ide/docrepr/issues/29), [26](https://github.com/spyder-ide/docrepr/issues/26))
* [PR 25](https://github.com/spyder-ide/docrepr/pull/25) - Fix render_math condition, by [@martinRenou](https://github.com/martinRenou)
* [PR 21](https://github.com/spyder-ide/docrepr/pull/21) - Update to work with latest Sphinx and IPython, by [@fasiha](https://github.com/fasiha)

In this release, 11 pull requests were merged.



## [0.1.1] - 2017-12-19

### Issues Closed

* [Issue 15](https://github.com/spyder-ide/docrepr/issues/15) - docrepr failing to import in readthedocs

In this release, 1 issue was closed.


### Pull Requests Merged

* [PR 14](https://github.com/spyder-ide/docrepr/pull/14) - Remove dangling r in Readme
* [PR 13](https://github.com/spyder-ide/docrepr/pull/13) - Fix possible Sphinxify.py TypeError on import

In this release, 2 pull requests were merged.



## [0.1.0] - 2016-03-07

* Initial release
