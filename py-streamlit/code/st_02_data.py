import streamlit as st

## Load data
# iris에 대한 Dataframe 구성
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris['target']
iris_df['target'] = iris_df['target'].apply(lambda x: 'setosa' if x == 0 else ('versicolor' if x == 1 else 'virginica'))
 
 
## Return table/dataframe
 # streamlit에서 웹 브라우저로 dataframe 출력

# 테이블 형태
#st.table(iris_df.head())
st.table(iris_df)

 # 데이터 프레임 형태
st.dataframe(iris_df)
 # 텍스트 형태
st.write(iris_df)


#
st.header("Load diabetes data")
diabetes_df = pd.read.csv("https://github.com/Redwoods/Py/raw/master/pdm2020/my-note/py-pandas/data/diabetes.csv")
st.dataframe(diabetes_df)