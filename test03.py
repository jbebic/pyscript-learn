from js import document, URL
from io import StringIO, BytesIO
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as dpdf

def plot_w_python(data):
    datastr = StringIO(data)
    df1 = pd.read_csv(datastr)
    buf = BytesIO()
    pltPdf = dpdf.PdfPages('buf.pdf')

    display(df1.columns, target="display-write")
    fig, ax = plt.subplots()
    ax.plot(df1["t"], df1["v"])
    ax.plot(df1["t"], df1["i"])
    ax.grid()
    plt.title("Plot from a local csv file")
    display(fig, target="graph-area", append=False)
    pltPdf.savefig()
    # plt.savefig(buf, format='pdf')
    plt.close()
    
    pltPdf.close()
    buf.seek(0)
    file = URL.createObjectURL([buf])
    # file = URL.createObjectURL(pltPdf)
    filelink = Element("download-link")
    filelink.element.innerHTML= "Jovan was here"
    # fin = Element("file_input")
    # filelink.element.href=fin.element.files[0]
    return buf
