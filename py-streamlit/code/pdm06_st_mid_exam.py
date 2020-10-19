import streamlit as st

## streamlit charts
## Plotting
# load iris.csv
# Raw 링크 주소 복사
# https://github.com/Redwoods/Py/raw/master/pdm2020/my-note/py-pandas/data/iris.csv
st.set_option('deprecation.showPyplotGlobalUse', False)
import pandas as pd
iris_df = pd.read_csv("https://github.com/Redwoods/Py/raw/master/pdm2020/my-note/py-pandas/data/iris.csv")
# read_csv 주소 값은 문자열로 입력
st.subheader('dataframe of iris data')
st.dataframe(iris_df)

## Plotting
st.subheader("Matplotlib/Pandas로 차트 그리기")
iris_df[iris_df['variety']=='Virginica']['petal.length'].hist()
# target -> variety, petal length (cm) -> petal.length
# Setosa / Versicolor / Virginica , 대소문자 구분
st.pyplot()