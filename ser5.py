#!/usr/bin/env python

from threading import Thread
import serial
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import struct
import pandas as pd
import time
import sys
from flask import Flask

app = Flask(__name__)

@app.route("/")

class serialPlot:
    def __init__(self, serialPort='COM3', serialBaud=38400, plotLength=100, dataNumBytes=2):
        self.port = serialPort
        self.baud = serialBaud
        self.plotMaxLength = plotLength
        self.dataNumBytes = dataNumBytes
        self.rawData = bytearray(dataNumBytes)
        self.data = collections.deque([0] * plotLength, maxlen=plotLength)
        self.isRun = True
        self.isReceiving = False
        self.thread = None
        self.plotTimer = 0
        self.previousTimer = 0
        self.csvData = []


        self.serialConnection = serial.Serial(serialPort, serialBaud, timeout=4)


    def readSerialStart(self):
        if self.thread == None:
            self.thread = Thread(target=self.backgroundThread)
            self.thread.start()
            # Block till we start receiving values
            while self.isReceiving != True:
                time.sleep(0.1)

    def getSerialData(self, frame, lines, lineValueText, lineLabel, timeText):
        currentTimer = time.perf_counter()
        self.plotTimer = int((currentTimer - self.previousTimer) * 1000)  # the first reading will be erroneous
        self.previousTimer = currentTimer
        timeText.set_text('Plot Interval = ' + str(self.plotTimer) + 'ms')
        value, = struct.unpack('f', self.rawData)  # use 'h' for a 2 byte integer
        self.data.append(value)  # we get the latest data point and append it to our array
        lines.set_data(range(self.plotMaxLength), self.data)
        lineValueText.set_text('[' + lineLabel + '] = ' + str(value))
        self.csvData.append(self.data[-1])

    def backgroundThread(self):  # retrieve data
        time.sleep(1.0)  # give some buffer time for retrieving data
        self.serialConnection.reset_input_buffer()
        while (self.isRun):
            self.serialConnection.readinto(self.rawData)
            self.isReceiving = True
            print(self.rawData)
            TimeCount()


    def close(self):
        self.isRun = False
        self.thread.join()
        self.serialConnection.close()
        df = pd.DataFrame(self.csvData)
        df.to_csv('C:/Users/hamza/PycharmProjects/serial/data.csv')

t_end = time.time() + 10
def TimeCount():
    if time.time() > t_end:
        #plt.close()
        sys.exit()
        #quit()


def main():
    portName = 'COM3'
    baudRate = 38400
    maxPlotLength = 100
    dataNumBytes = 4  # number of bytes of 1 data point
    s = serialPlot(portName, baudRate, maxPlotLength, dataNumBytes)  # initializes all required variables
    s.readSerialStart()  # starts background thread

    # plotting starts below
    pltInterval = 50  # Period at which the plot animation updates [ms]
    xmin = 0
    xmax = maxPlotLength
    ymin = -(1)
    ymax = 1
    fig = plt.figure()
    ax = plt.axes(xlim=(xmin, xmax), ylim=(float(ymin - (ymax - ymin) / 10), float(ymax + (ymax - ymin) / 10)))

    lineLabel = ''
    timeText = ax.text(0.50, 0.95, '', transform=ax.transAxes)
    lines = ax.plot([], [], label=lineLabel)[0]
    lineValueText = ax.text(0.50, 0.90, '', transform=ax.transAxes)
    anim = animation.FuncAnimation(fig, s.getSerialData, fargs=(lines, lineValueText, lineLabel, timeText),
                                    interval=pltInterval)  # fargs has to be a tuple


    plt.axis('off')
    plt.show()
    s.close()


if __name__ == '__main__':
    main()