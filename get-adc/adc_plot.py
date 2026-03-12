#!/bin/env python3

import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.grid(True)
    plt.plot(time, voltage)
    plt.title("График зависимости напряжения на входе АЦП от времени")
    plt.legend()
    plt.show()
