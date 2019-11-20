import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_recall_fscore_support
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

dados_treino = pd.read_csv('breastcancerwisconsin.csv')
dados_treino.columns

atributos = []
for atributo in dados_treino.columns:
    if atributo != 'diagnosis' and atributo != 'id' and atributo != 'Unnamed: 32':
        atributos.append(atributo)


caracteristicas_train,caracteristicas_test,rotulos_train,rotulos_test = train_test_split(dados_treino[atributos],
                                                             dados_treino['diagnosis'],test_size=0.2, random_state=0)

#Utilizando o algoritmo KNN
algoritmo_knn = KNeighborsClassifier()
algoritmo_knn.fit(caracteristicas_train, rotulos_train)

print("Acurácia = {0}%".format(100*np.sum(algoritmo_knn.predict(caracteristicas_test) == rotulos_test)/len(rotulos_test)))
print("algoritmo KNN (Precisão, Revogação, Fscore)")
print(precision_recall_fscore_support(rotulos_test, algoritmo_knn.predict(caracteristicas_test),average=None))

#Aplicando PCA
dados_normalizados = StandardScaler().fit_transform(dados_treino[atributos])
pca = PCA(n_components=0.90)
componentes_principais = pca.fit_transform(dados_normalizados)

caracteristicas_train,caracteristicas_test,rotulos_train,rotulos_test = train_test_split(dados_normalizados,
                                                             dados_treino['diagnosis'],test_size=0.2, random_state=0)

#Utilizando o algoritmo KNN
algoritmo_knn = KNeighborsClassifier()
algoritmo_knn.fit(caracteristicas_train, rotulos_train)

print("Acurácia = {0}%".format(100*np.sum(algoritmo_knn.predict(caracteristicas_test) == rotulos_test)/len(rotulos_test)))
print("algoritmo KNN (Precisão, Revogação, Fscore)")
print(precision_recall_fscore_support(rotulos_test, algoritmo_knn.predict(caracteristicas_test),average=None))

