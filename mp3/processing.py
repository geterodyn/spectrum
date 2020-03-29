import base64
from io import BytesIO

from librosa import load, stft
from matplotlib.figure import Figure
import numpy as np


def uploaded_file_handle(file):
    y, sr = load(file)
    D = np.abs(stft(y))
    fig = Figure()
    ax = fig.subplots()
    ax.plot(D)
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data