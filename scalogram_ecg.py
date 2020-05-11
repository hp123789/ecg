import numpy as np
from scipy.signal import argrelextrema
from scipy import signal
import matplotlib.pyplot as plt

data = np.loadtxt('hamza/trial1.txt', skiprows=1000)

plt.plot(data)
plt.show()

def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

rawdata = np.array(data)
signal2 = rawdata

filtered_sine = butter_highpass_filter(signal2.data,0.5,30)

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

filtered_sine = moving_average(filtered_sine)

plt.plot(filtered_sine)
plt.show()

y = np.array(filtered_sine)

average = float(max(y)/2)

for n, i in enumerate(y):
    if i < average:
        y[n] = 0

x = y[:]
x = argrelextrema(x, np.greater)
x=x[0]

first_beat = data[x[0]:x[1]]
a = np.array(first_beat)

plt.plot(a)
plt.show()

# scalogram
######
from pylab import *
import pywt

def plot_wavelet(time, signal, scales,
                 waveletname='cmor',
                 cmap=plt.cm.seismic,
                 title='Wavelet Transform (Power Spectrum) of signal',
                 ylabel='Period (years)',
                 xlabel='Time'):
    dt = time[1] - time[0]
    [coefficients, frequencies] = pywt.cwt(signal, scales, waveletname, dt)
    power = (abs(coefficients)) ** 2
    period = 1. / frequencies
    levels = [0.0625, 0.125, 0.25, 0.5, 1, 2, 4, 8]
    contourlevels = np.log2(levels)

    fig, ax = plt.subplots(figsize=(15, 10))
    im = ax.contourf(time, np.log2(period), np.log2(power), contourlevels, extend='both', cmap=cmap)

    # ax.set_title(title, fontsize=20)
    # ax.set_ylabel(ylabel, fontsize=18)
    # ax.set_xlabel(xlabel, fontsize=18)

    yticks = 2 ** np.arange(np.ceil(np.log2(period.min())), np.ceil(np.log2(period.max())))
    ax.set_yticks(np.log2(yticks))
    ax.set_yticklabels(yticks)
    ax.invert_yaxis()
    ylim = ax.get_ylim()
    ax.set_ylim(ylim[0], -1)

    cbar_ax = fig.add_axes([0.95, 0.5, 0.03, 0.25])
    fig.colorbar(im, cax=cbar_ax, orientation="vertical")
    plt.axis('off')
    #plt.show()
    #plt.savefig('scalogram_hamza1.png', bbox_inches='tight')

time = np.arange(0, len(a)) * 0.25 + 0
scales = np.arange(1, 16)
plot_wavelet(time, a, scales)