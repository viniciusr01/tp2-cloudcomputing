import pandas as pd
import ssl
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pickle
import os

ssl._create_default_https_context = ssl._create_unverified_context


url = os.environ.get('url')

df = pd.read_csv(url)

basket = df.groupby(['pid', 'track_name'])['track_name'].count().unstack().fillna(0)


def encode_units(x):
	if x<=0:
		return False
	if x>=1:
		return True

basket_sets = basket.applymap(encode_units)

frequent_itemsets = apriori(basket_sets, min_support=0.07, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

rules.to_pickle("./ml_rules/model_rules.pkl")

