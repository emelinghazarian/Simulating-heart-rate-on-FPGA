import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import resample

# Load ECG signal dataset from CSV
dataset = pd.read_csv('mitbih.csv', header=None)

# Extract ECG signal with label 0 and two rows
label = 0
row1 = dataset[dataset.iloc[:, -1] == label].values[0, 70:121]
row2 = dataset[dataset.iloc[:, -1] == label].values[1, 80:131]
ecg_signal = np.concatenate((row1, row2))

# Define constants
fs_original = 100  # Original sampling frequency in Hz
fs_downsampled = 20  # Desired sampling frequency in Hz

# Downsample the ECG signal
num_samples_original = len(ecg_signal)
num_samples_downsampled = int(num_samples_original * fs_downsampled / fs_original)
ecg_signal_downsampled = resample(ecg_signal, num_samples_downsampled)

# Normalize the downsampled ECG signal to the range of 0 to 255
ecg_signal_normalized = ((ecg_signal_downsampled - np.min(ecg_signal_downsampled)) /
                         (np.max(ecg_signal_downsampled) - np.min(ecg_signal_downsampled))) * 255

# Save the signals to a file
np.savetxt('ecg_signals.txt', ecg_signal_normalized)

# Load the signals from the file
loaded_signals = np.loadtxt('ecg_signals.txt')

# Plot original ECG signal
plt.figure(figsize=(10, 4))
plt.plot(ecg_signal, label='Original ECG signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.title('Original ECG Signal')
plt.legend()
plt.show()

# Plot downsampled ECG signal
plt.figure(figsize=(10, 4))
plt.plot(ecg_signal_downsampled, label='Downsampled ECG signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.title('Downsampled ECG Signal')
plt.legend()
plt.show()

# Calculate heart rate
def calculate_heart_rate(r_peaks, fs):
    rr_intervals = np.diff(r_peaks) / fs
    heart_rate = 60 / np.mean(rr_intervals)
    return heart_rate

# Find R peaks
def find_r_peaks(signal, threshold):
    r_peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1] and signal[i] > threshold:
            r_peaks.append(i)
    return r_peaks

# Find the threshold for R peak detection
threshold = 0.6 * np.max(ecg_signal_downsampled)

# Find R peaks in the downsampled ECG signal
r_peaks = find_r_peaks(ecg_signal_downsampled, threshold)

# Calculate heart rate
heart_rate = calculate_heart_rate(r_peaks, fs_downsampled)

# Print heart rate
print("Heart rate: {:.2f} BPM".format(heart_rate))

# Plot downsampled ECG signal with R peaks
plt.figure(figsize=(10, 4))
plt.plot(loaded_signals, label='Loaded ECG signal')
plt.scatter(r_peaks, loaded_signals[r_peaks], color='red', label='R peak')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.title('Loaded ECG Signal with R peaks')
plt.legend()
plt.show()
