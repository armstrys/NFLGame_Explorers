## What is this?
The applets on this page serve as a [Streamlit](https://www.streamlit.io/) interface to explore the [NFLGame](https://github.com/derek-adair/nflgame) Python package.

The first applet included is the 'Play_Explorer' applet, which lets you explore some pieces of the nflgame JSON data structure. Be sure to check the docs for the API [here](http://nflgame.derekadair.com/) to get a better feel fro the capabilities of the package beyond the data model.  Note that the [NFLDB](https://github.com/BurntSushi/nfldb) provides a more structured data model which is described [here](https://github.com/BurntSushi/nfldb/wiki/The-data-model). The nfldb repository is no longer active, but can be used along side an installation of [nflgame-redux](https://pypi.org/project/nflgame-redux/).

## Running the Applets
The applets are written using [Streamlit](https://www.streamlit.io/) and pull data from [NFLGame](https://github.com/derek-adair/nflgame). Most applets will rely on only those two packages, while some may require other common Pyhton packages. To run these applets either download the code and run using Streamlit in your terminal or alternatively call the Github file direcly. An example using the 'Play_Explorer' applet.
```python
streamlit run https://github.com/ryscar13/NFLGame_Explorers/blob/master/Play_Explorer.py
```