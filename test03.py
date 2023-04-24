from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt

def plot_w_python(data):
    datastr = StringIO(data)
    df1 = pd.read_csv(datastr)
    display(df1.columns, target="display-write")
    fig, ax = plt.subplots()
    ax.plot(df1["t"], df1["v"])
    ax.plot(df1["t"], df1["i"])
    ax.grid()
    plt.title("Plot from a local csv file")
    display(fig, target="graph-area", append=False)

