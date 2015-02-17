# ceci-est-un-pipeau

This file contains organisation information.

## Environment Setup

We will be using the latest Python2.

It may take quite a while to install some packages. To save time, it is preferable to do this before the contest.

### [Anaconda](http://continuum.io/downloads)

Anaconda comes with a lot of useful libraries and environment management tools. It's easy to set up.

After installing, go to the repo and use
```(sh)
conda env create -n pipeau
```
to create a environment named ```pipeau``` containing packages in ```environment.yml```.

To (de)activate the environment:
```(sh)
source activate pipeau
source deactivate pipeau
```

To install a new package and share with others:
```(sh)
# install in pipeau environment
conda install <name of package>
pip install <name of package> # if conda failed
conda env export -n pipeau -f environment.yml
# in git, push changes in environment.yml to remote
```
To get packages that others shared:
```(sh)
# pull changes from remote
conda env update -n pipeau
```
Some handy repls/editors from anaconda:
```(sh)
ipython
ipython qtconsole
spyder
# and others
```



## Strategies

- Greedy
- CP + NEOS
- Iterative Optimisation
- Approximation


## TODO


