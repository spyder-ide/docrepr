# Contributing Guide

Docrepr is part of the Spyder IDE Github org, and is developed with standard Github flow.

If you're not comfortable with at least the basics of ``git`` and GitHub, we recommend reading beginner tutorials such as [GitHub's Git Guide](https://github.com/git-guides/), its [introduction to basic Git commands](https://guides.github.com/introduction/git-handbook/#basic-git) and its [guide to the fork workflow](https://guides.github.com/activities/forking/), or (if you prefer) their [video equivalents](https://www.youtube.com/githubguides).
However, this contributing guide should fill you in on most of the basics you need to know.

Let us know if you have any further questions, and we look forward to your contributions!


## Reporting Issues

Discover a bug?
Want a new feature?
[Open](https://github.com/spyder-ide/docrepr/issues/new/choose) an [issue](https://github.com/spyder-ide/docrepr/issues)!
Make sure to describe the bug or feature in detail, with reproducible examples and references if possible, what you are looking to have fixed/added.
While we can't promise we'll fix everything you might find, we'll certainly take it into consideration, and typically welcome pull requests to resolve accepted issues.



## Setting Up a Development Environment

**Note**: You may need to substitute ``python3`` for ``python`` in the commands below on some Linux distros where ``python`` isn't mapped to ``python3`` (yet).


### Fork and clone the repo

First, navigate to the [project repository](https://github.com/spyder-ide/docrepr) in your web browser and press the ``Fork`` button to make a personal copy of the repository on your own Github account.
Then, click the ``Clone or Download`` button on your repository, copy the link and run the following on the command line to clone the repo:

```bash
git clone <LINK-TO-YOUR-REPO>
```

Finally, set the upstream remote to the official Docrepr repo with:

```bash
git remote add upstream https://github.com/spyder-ide/docrepr.git
```


### Create and activate a fresh environment

Particularly for development installs, we highly recommend you create and activate a virtual environment to avoid any conflicts with other packages on your system or causing any other issues.
Of course, you're free to use any environment management tool of your choice (conda, virtualenvwrapper, pyenv, etc).

To do so with Conda (recommended), simply execute the following:

```bash
conda create -c conda-forge -n docrepr-env python=3.9
```

And activate it with

```bash
conda activate docrepr-env
```

With pip/venv, you can create a virtual environment with

```bash
python -m venv docrepr-env
```

And activate it with the following on Linux and macOS,

```bash
source docrepr-env/bin/activate
```

or on Windows (cmd),

```cmd
.\docrepr-env\Scripts\activate.bat
```

Regardless of the tool you use, make sure to remember to always activate your environment before using it.


### Install Docrepr in editable mode

Then, to install the Docrepr package and its dependencies in editable ("development") mode, where updates to the source files will be reflected in the installed package, and include any additional dependencies used for development, run

```bash
python -m pip install -e .[test]
```

You can then import and use Docrepr as normal.
When you make changes in your local copy of the git repository, they will be reflected in your installed copy as soon as you re-run Python.



## Deciding Which Branch to Use

When you start to work on a new pull request (PR), you need to be sure that your work is done on top of the correct branch, and that you base your PR on Github against it.

To guide you, issues on Github are marked with a milestone that indicates the correct branch to use.
If not, follow these guidelines:

* Use the latest release branch (e.g. ``1.x``) to fix security issues and critical bugs only (if in any doubt, ask first)
* Use ``master`` branch for anything else, particularly introducing new features or breaking compatibility with previous versions

Of course, if a bug is only present in ``master``, please base bugfixes on that branch.



## Making Your Changes

To start working on a new PR, you need to execute these commands, filling in the branch names where appropriate (``<BASE-BRANCH>`` is the branch you're basing your work against, e.g. ``master``, while ``<FEATURE-BRANCH>`` is the branch you'll be creating to store your changes, e.g. ``fix-startup-bug`` or ``add-widget-support``:

```bash
git checkout <BASE-BRANCH>
git pull upstream <BASE-BRANCH>
git checkout -b <FEATURE-BRANCH>
```

Once you've made and tested your changes, commit them with a descriptive, unique message of 74 characters or less written in the imperative tense, with a capitalized first letter and no period at the end.
Try to make your commit message understandable on its own, giving the reader a high-level idea of what your changes accomplished without having to dig into the diffs.
For example:

```bash
git commit -am "Fix bug reading env variable when importing package on Windows"
```

If your changes are complex (more than a few dozen lines) and can be broken into discrete steps/parts, its often a good idea to make multiple commits as you work.
On the other hand, if your changes are fairly small (less than a dozen lines), its usually better to make them as a single commit, and then use the ``git -a --amend`` (followed by ``git push -f``, if you've already pushed your work) if you spot a bug or a reviewer requests a change.

These aren't hard and fast rules, so just use your best judgment, and if there does happen to be a significant issue we'll be happy to help.



## Running the Tests

Once you've made your changes (or ideally, before), you'll want to run the full test suite and write new tests of your own, if you haven't already done so.

This package uses the [Pytest](https://pytest.org) framework for its unit and integration tests, which are located inside the package alongside the tested code, in the ``tests/`` subdirectory.
We **strongly** suggest you run the full test suite before every commit (it should only take a few seconds to run on most machines).

In general, any new major functionality should come with tests, and we welcome contributing to expand our coverage, increase reliability, and ensure we don't experience any regressions.
If you need help writing tests, please let us know, and we'll be happy to guide you.

To run the tests, install the development dependencies as above, and then simply execute

```bash
pytest
```

For a more rigorous run mirroring what is executed on our CIs, execute the following:

```bash
cd docrepr
python -bb -X dev -W error -m pytest
cd ..
```

The ``pytest.ini`` config file configures a variety of settings and command line options for you.
If you want to preview the rendered docstrings from the tests in your web browser, you can run ``pytest`` with Docrepr's custom ``--open-browser`` option:

```bash
pytest --open-browser
```

Docrepr uses [Playwright](https://playwright.dev/python/) to run automated visual regression tests on our CIs, checking for deltas against screenshots of previous runs of the various output-facing tests on each platform.
To run these locally, first install the required dependencies:

```bash
python -m pip install -e .[visual_test]
```

Then, run the test suite with the ``--compare-screenshots`` custom option:

```bash
pytest --compare-screenshots
```

If you make a change that deliberately causes a difference in the output, carefully inspect each test that flags a delta to ensure it looks as you intend.
Then, if needed, you can regenerate the screenshots to reflect your change; while you *can* do so locally with the ``--update-reference-screenshots`` option, you should do so on the CIs instead as part of your pull request, so the results are consistent, generated for each platform and optimized to minimize storage consumption.
See that section for more.


## Pushing your Changes

Now that your changes are ready to go, you'll need to push them to the appropriate remote.
All contributors, including core developers, should push to their personal fork and submit a PR from there, to avoid cluttering the upstream repo with feature branches.
To do so, run:

```bash
git push -u origin <FEATURE-BRANCH>
```

Where ``<FEATURE-BRANCH>`` is the name of your feature branch, e.g. ``fix-startup-bug``.



## Submitting a Pull Request

Finally, create a pull request to the [spyder-ide/docrepr repository](https://github.com/spyder-ide/docrepr/) on Github.
Make sure to set the target branch to the one you based your PR off of (``master`` or ``X.x``).

If you need to update the reference screenshots, leave a comment on the PR with the text ``Please update reference screenshots`` and the CI will take care of the rest.
Keep in mind it will commit the changes for you, so make sure you've pushed everything to your remote branch first and don't have any uncomitted work, and make sure to ``git pull`` immediately afterward to pull in the updates.

We'll then review your changes, and after they're ready to go, your work will become an official part of Docrepr.

Thanks for taking the time to read and follow this guide, and we look forward to your contributions!
