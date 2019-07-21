episodescript
=============
[![pypi](https://badge.fury.io/py/episodescript.svg)](https://badge.fury.io/py/episodescript)

Retrieve TV Show Scripts.


## Install

* From PyPi.

```
pip install episodescript
```

* Alternatively, recommended for Conda users.

```
conda install -y beautifulsoup4 'html5lib<1'
pip install episodescript --no-deps
```

* Alternatively, from GitHub.
```
git clone https://github.com/kota7/episodescript
pip install ./episodescript
```


## Use the console command

```
episode-script the-mentalist 2 6
```
  
Or, if you want to read step by step:
  
```
episode-script the-mentalist 2 6 | less
```


## Use in a python script

```
>>> from episodescript import scrape_episode_scripts
>>> title, script = scrape_episode_scripts("the-mentalist", 2, 6)
>>> print(title)
>>> print(script)
```


## Note

This program relies on the website [TV Show Episode Script](https://www.springfieldspringfield.co.uk/tv_show_episode_scripts.php).
See this page for available TV show names.