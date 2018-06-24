
#%%
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%%

#%matplotlib inline

iris = datasets.load_iris()

"""
sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  \
0                5.1               3.5                1.4               0.2   
1                4.9               3.0                1.4               0.2   
2                4.7               3.2                1.3               0.2   
"""
x = pd.DataFrame(iris['data'], columns=iris['feature_names'])
print("target_names: "+str(iris['target_names']))
y = pd.DataFrame(iris['target'], columns=['target'])
iris_data = pd.concat([x,y], axis=1)
iris_data.head(3)

#%%

iris['target_names']

#%%


target_name = {
    0:'setosa',
    1:'versicolor',
    2:'virginica'
}

#%%

iris_data['target_name'] = iris_data['target'].map(target_name)
#Select to 'setosa','versicolor','virginica'..abdon other
iris_data = iris_data[(iris_data['target_name'] == 'setosa')|(iris_data['target_name'] == 'versicolor')]
# And just choice 2 feature
iris_data = iris_data[['sepal length (cm)','petal length (cm)','target_name']]
iris_data.head(5)

#%%
target_class = {
    'setosa':1,
    'versicolor':-1
}


#%%
#using target_calss mapping before removing target_name
iris_data['target_class'] = iris_data['target_name'].map(target_class)

#%%
del iris_data['target_name']

#%%
iris_data.head(5)

#%%
def sign(z):
    if z > 0:
        return 1
    else:
        return -1

#%%

w = np.array([0., 0., 0.])
error = 1
iterator = 0

while error != 0:
    error = 0
    for i in range(len(iris_data)):
        #x is get two feature
        x, y = np.concatenate((np.array([1.]), np.array(iris_data.iloc[i])[:2])), np.array(iris_data.iloc[i])[2]
        if sign(np.dot(w, x)) != y:
            print("iterator: " + str(iterator))
            iterator += 1
            error += 1
            #show iris data 
            sns.lmplot('sepal length (cm)', 'petal length (cm)', data=iris_data, fit_reg=False, hue='target_class')

            # Previous Decision boundary Normal vector
            if w[1] != 0:
                x_last_decision_boundary = np.linspace(0, w[1])
                y_last_decision_boundary = (w[2] / w[1]) * x_last_decision_boundary
                plt.plot(x_last_decision_boundary, y_last_decision_boundary, 'c--')
            # w += y * x is our function
            w += y * x
            print("x: " + str(x))
            print("w: " + str(w))
            # x vector linspace is return (arg1..arg2) space
            x_vector = np.linspace(0, x[1])
            # （ petal len / sepal len) * x
            # y = (feature1 / featrue2) * x
            y_vector = (x[2] / x[1]) * x_vector
            plt.plot(x_vector, y_vector, 'b')
            
            
            # Decision boundary vector
            x_decision_boundary = np.linspace(-0.5, 7)
            y_decision_boundary = (-w[1] / w[2]) * x_decision_boundary - (w[0] / w[2])
            plt.plot(x_decision_boundary, y_decision_boundary, 'r')
            # Decision boundary Normal vector
            x_decision_boundary_normal_vector = np.linspace(0, w[1])
            y_decision_boundary_normal_vector = (w[2] / w[1]) * x_decision_boundary_normal_vector
            plt.plot(x_decision_boundary_normal_vector, y_decision_boundary_normal_vector, 'g')
            
            
            plt.xlim(-0.5, 7.5)
            plt.ylim(5, -3)
            plt.show()