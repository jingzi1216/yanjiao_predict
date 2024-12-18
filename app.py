import streamlit as st
import joblib

# 加载模型
model_v = joblib.load("viscosity.pkl")
model_s = joblib.load("solids.pkl")

# 设置页面标题和布局
st.set_page_config(page_title="黏度与固含量预测", layout="centered", initial_sidebar_state="collapsed")
st.title("烟胶生产预测系统")
hide_streamlit_style = """
    <style>
    /* 隐藏右上角 GitHub 图标 */
    #MainMenu {visibility: hidden;}
    /* 隐藏页脚 */
    footer {visibility: hidden;}
    /* 隐藏顶部的 Streamlit 菜单 */
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("""
<style>

    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    label {
        font-size: 20px;
        font-weight: bold;
        color: #333;
    }
    .stSuccess {
        font-size: 20px;
        font-weight: bold;
        color: #155724;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        padding: 10px;
        border-radius: 5px;
    }
    h3 {
        font-size: 20px;
        font-weight: bold;
        color: #2c3e50;
    }
</style>
<div class="main">
""", unsafe_allow_html=True)

st.write("请输入以下参数(百分数以小数格式输入)，点击预测按钮以查看结果。")

# 用户输入数据
乳液A = st.number_input("**乳液A**", value=0.0, step=0.001)
乳液A粘度 = st.number_input("**乳液A粘度**", value=0.0, step=0.001)
乳液A固含量 = st.number_input("**乳液A固含量**", value=0.0, step=0.001, format="%.3f")
乳液F = st.number_input("**乳液F**", value=0.0, step=0.001)
乳液F粘度 = st.number_input("**乳液F粘度**", value=0.0, step=0.001)
乳液F固含量 = st.number_input("**乳液F固含量**", value=0.0, step=0.001, format="%.3f")
水溶液E = st.number_input("**水溶液E**", value=0.0, step=0.001)
水溶液E固含量 = st.number_input("**水溶液E固含量**", value=0.0, step=0.001, format="%.3f")
水溶液F = st.number_input("**水溶液F**", value=0.0, step=0.001)
水溶液F固含量 = st.number_input("**水溶液F固含量**", value=0.0, step=0.001, format="%.3f")
水 = st.number_input("**水**", value=0.0, step=0.001)
其它 = st.number_input("**其它**", value=0.0, step=0.001)
其他固含量 = st.number_input("**其它固含量**", value=0.0, step=0.001, format="%.3f")

# 构建特征数组
X_viscosity = [[乳液A粘度, 乳液F粘度, 水溶液E, 水, 乳液A固含量, 乳液F固含量]]
X_solids_content = [[乳液A固含量, 乳液F固含量, 水, 乳液A粘度, 水溶液E, 乳液F粘度]]

if st.button("🔍 预测"):
    print(1)
    # 进行预测
    预测黏度 = model_v.predict(X_viscosity)[0]
    预测固含量 = model_s.predict(X_solids_content)[0]

    # 输出结果
    st.subheader("预测结果")

    st.markdown(f"<div class='stSuccess'>预测黏度: {预测黏度:.2f}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='stSuccess'>预测固含量: {预测固含量*100:.2f}%</div>", unsafe_allow_html=True)

st.markdown("""
</div>
""", unsafe_allow_html=True)
