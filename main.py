import streamlit as st
import time
# import numpy as np
# import pandas as pd
# from PIL import Image

st.title("streamlit入門")

st.write("プログレスバーの表示")
'start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration:{i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!'


left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("右カラム")

expander１ = st.expander("問い合わせ内容1")
expander1.write("問い合わせ内容1の回答")

expander2 = st.expander("問い合わせ内容2")
expander2.write("問い合わせ内容2の回答")

expander3 = st.expander("問い合わせ内容3")
expander3.write("問い合わせ内容3の回答")




# text = st.sidebar.inputbox("あなたの趣味を教えてください")
# "あなたの趣味：", text

# condition = sidebar.slider("あなたの今の調子は？",0,10,6)
# "あなたの調子", condition
# option = st.selectbox(
#     "あなたが好きな数字を教えてください",
#     list(range(1,11))
# )

# "あなたの好きな数字は", option, "です。"


# if st.checkbox("Show Image"):
#     img = Image.open("home.png")
#     st.image(img, caption = "test image", use_column_width=True)




# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     columns=['lat','lon']
# )
# st.map(df)

# st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)
# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """




