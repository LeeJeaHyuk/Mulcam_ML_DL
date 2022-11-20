from MyModule import lib,person
from MyModule import girdcvconv as gv

print(lib.add(1,2))

print(person.person('a'))

best_score_ = 0.4
best_params = {'criterion': 'entropy', 'max_depth': 8, 'min_impurity_decrease': 0.0, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'random_state': 42, 'splitter': 'best'}

gv.paramsTocsv('DicisonTreeClassifier',best_params,best_score_)




