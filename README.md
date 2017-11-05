# Pelican Static Site Generator

These are my notes for setting up a virtual environment for Pelican, the static
site generator that I use to build my blog.

## Reasons for using this guide

This document guides you through the processes of setting up a virtual
environment, this way you can use the lastest version of Pelican, pulling it
fron pypi without worrying about breaking or poluting your system.

- This ensure true portability and reproducible environments.

## Installing `virtualenv` and `pip`

> Fedora

```sh
su -c 'dnf install python2-virtualenv.noarch python3-virtualenv.noarch'
```

```sh
su -c 'dnf install python2-pip.noarch python3-pip.noarch'
```

## Create a directory for virtualenvs

```sh
cd ~/Documents
mkdir virtualenvs
cd virtualenvs
```

## Create a virtualenv for Pelican

Use the `virtualenv-3` or the `virtualenv-3.6` command.

```sh
virtualenv-3 --no-site-packages pelican
```

```sh
cd pelican
```

## Activate the virtualenv

```sh
source bin/activate
```

## Install upgrade the `setuptools` and `pip`

```sh
pip install --upgrade setuptools pip
```
## Install Optional Packages

```sh
pip install Markdown typogrify
```

## Install Pelican

```sh
pip install pelican
```

## Upgrading Everything

```sh
pip install --upgrade pelican Markdown typogrify setuptools pip
```

## Clone the github repo

```sh
git@github.com:porfiriopaiz/site.git
```

## Pelican commands

### Build a site after edit or new post

```sh
make html
```

### Serve site locally at `http://localhost:8000/:`

```sh
make serve
```

## Github serving

```sh
git checkout master
git subtree split --prefix output -b gh-pages
git push -f origin gh-pages:gh-pages
git branch -D gh-pages
```
