import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({"x": [10, 20, 30, 40],
                   "y": [100, 200, 300, 400],
                   "name": ['alpha', 'beta', 'gamma', 'delta']})

x_max = st.slider("Max value of x", float(df['x'].max()))
st.title("My First App")
st.markdown("""Let's look at this fine dataframe)""")
df[df["x"]<= x_max]
st.markdown("""Now let's draw""")
a = st.slider("Amplitude", 0, 10)
b = st.slider("Frequency", 0, 10)
x = np.linspace(0, 10)
fig = plt.figure()
plt.plot(x, a*np.sin(x*b))
plt.ylim(-5, 5)
st.pyplot(fig)
