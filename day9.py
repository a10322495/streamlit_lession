import pandas as pd  
import sklearn 
import numpy as np 
import streamlit as st  
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from sklearn.datasets import load_iris 



st.header('Line Chart')

df = pd.DataFrame(np.random.randn(30,3),columns=['a','b','c'])

st.line_chart(df)

option = st.selectbox('你要选择那种颜色？',('红','绿色','白色'))

st.write('你选择的颜色是',option)

st.subheader('下面显示的是多选组件')


option_1 = st.multiselect('多选组件的选择容器：',('选择一','2','3','Link Park','Queen','Embreen'))

st.write('你在多选组件中的操作：',option_1)


st.subheader('勾选组件[checkbox]的学习')

ch1 = st.checkbox('咖啡')
ch2 = st.checkbox('抽烟')
ch3 = st.checkbox('喝酒')

if ch1:
    st.write('你选择了咖啡')
if ch2:
    st.write('你选择了抽烟')
if ch3:
    st.write('你选择了喝酒')


st.subheader('pandas_profileing工具的介绍')

st.write('加载数据！')
iris_file = load_iris() 

df = pd.DataFrame(iris_file.data)
# df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
# pr = df.profile_report 
# st_profile_report(pr)

st.subheader('Day16：Streamlit 的自己定义主题')

st.title('数据主题看板！')

st.write('Contents of the `.streamlit/config.toml` file of this app,这个文件的存放位置 `C:\\Users\Administrator\\.streamlit`')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)

st.write('Selected number from slider widget is:', number,'我的这个测试看不到效果！')

st.subheader('Day17:密文的Demo，这个功能测试失败了')

# st.write(st.secrets['message'])

st.subheader('Day18: st.file_upload 上传文件demo')
st.markdown('#### 上传一个CSV格式文件')
uploaded_file = st.file_uploader('选择一个文件')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file,encoding='utf-8')    # utf-8  能解决中文
    st.subheader('DateFrame')
    st.write(df)
    st.subheader('DateFrame 表格的描述')
    st.write(df.describe())
