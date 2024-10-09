#include <stdio.h>

#define MAX_R_PEAKS 100

// Function to detect R peaks
int detectRPeaks(int* signal, int length, int threshold, int* rPeaks) {
    int numRPeaks = 0;

    int i;
    for (i = 1; i < length - 1; i++) {
        if (signal[i] > signal[i - 1] && signal[i] > signal[i + 1] && signal[i] > threshold) {
            rPeaks[numRPeaks] = i;
            numRPeaks++;
        }
    }

    return numRPeaks;
}

// Function to calculate heart rate
float calculateHeartRate(int* rPeaks, int numRPeaks, int fs) {
    int rrSum = 0;
    int i;

    for (i = 1; i < numRPeaks; i++) {
        rrSum += rPeaks[i] - rPeaks[i - 1];
    }

    float avgRRInterval = (float)rrSum / (numRPeaks - 1);
    float heartRate = (float)fs / avgRRInterval * 60;

    return heartRate;
}

int main() {
    // Define constants
    int fs = 20;  // Sampling frequency in Hz
    int threshold = 126;  // Threshold for R peak detection
    int signalLength = 20;
    int rPeaks[MAX_R_PEAKS];
    int numRPeaks;

    // Read the signal from the text file
    FILE* file = fopen("signal.txt", "r");
    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;
    }

    int signal[signalLength];
    int i;
    for (i = 0; i < signalLength; i++) {
        fscanf(file, "%d", &signal[i]);
    }
    fclose(file);

    // Detect R peaks
    numRPeaks = detectRPeaks(signal, signalLength, threshold, rPeaks);

    // Calculate heart rate
    float heartRate = calculateHeartRate(rPeaks, numRPeaks, fs);

    // Print the heart rate
    printf("Heart rate: %.2f BPM\n", heartRate);

    return 0;
}
