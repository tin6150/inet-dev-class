#!/usr/bin/env python

# need python 2.7 really

# tried from jupyter notebook from LRC "local server"
# but visuals lib not there
# and probably also need to install scikit-learn lib...
# so trying locally on linux (bacbay)


# http://www.ritchieng.com/machine-learning-project-boston-home-prices/
import numpy as np
import pandas as pd
import visuals as vs 
from sklearn.cross_validation import ShuffleSplit

# pretty display, maybe a jupyter notebook thing only
#%matplotlib inline

data = pd.read_csv('housing.csv')

# hmmm, fork 
# https://github.com/ritchieng/machine-learning-nanodegree/blob/master/model_evaluation_prediction/boston_housing/boston_housing.ipynb
# machine-learning-nanodegree/model_evaluation_prediction/boston_housing/

# tin-gh/machine-learning-nanodegree

