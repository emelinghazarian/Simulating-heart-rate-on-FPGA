<!DOCTYPE html>
<html>

<body>

<h1>FPGA Project: MicroBlaze and ECG Signal Processing</h1>

<p>This repository contains code and resources for implementing an FPGA project using MicroBlaze, GPIO control, 7-Segment display, and ECG signal processing through Vivado HLS.</p>

<h2>Project Overview</h2>
<p>The project aims to build an FPGA-based system that reads ECG data, detects peaks, calculates heart rate, and displays the result on a dual 7-segment display. It utilizes MicroBlaze as the main processor with GPIO control for input and output.</p>

<h2>Requirements</h2>
<ul>
    <li>FPGA with MicroBlaze processor configured through Vivado</li>
    <li>Vivado HLS for creating IP cores for ECG processing</li>
    <li>SDK for C programming on MicroBlaze</li>
    <li>Dual 7-Segment display for output</li>
</ul>

<h2>Project Setup</h2>
<ol>
    <li><strong>GPIO Control:</strong> Write code in C to toggle GPIO pins on MicroBlaze, using SDK, to control a 7-segment display.</li>
    <li><strong>Single and Dual 7-Segment Display:</strong>
        <ul>
            <li>Single-digit: Display a counter (0-9) with a specified frequency.</li>
            <li>Dual-digit: Use multiplexing to count from 0-99 and display the result on a 7-segment display.</li>
        </ul>
    </li>
    <li><strong>ECG Signal Processing:</strong> Use Vivado HLS to create an IP core that detects peaks in ECG data and calculates heart rate.</li>
</ol>

<h2>Usage Instructions</h2>
<p>Follow these steps to use the project:</p>
<ol>
    <li>Load the project in Vivado and configure the MicroBlaze processor with GPIO settings.</li>
    <li>Compile and deploy the C code using SDK for GPIO operations and 7-segment display control.</li>
    <li>Simulate the ECG signal processing using the provided HLS code to detect peaks and calculate heart rate.</li>
    <li>Run the project on an FPGA board with a 7-segment display connected to verify the heart rate output.</li>
</ol>

<h2>Features</h2>
<ul>
    <li>Toggle GPIO pins to control single and dual 7-segment displays.</li>
    <li>Peak detection and heart rate calculation using Vivado HLS for ECG signals.</li>
    <li>Real-time display of heart rate on a 7-segment display.</li>
</ul>

<h2>Testing and Verification</h2>
<p>The project includes test benches to verify each function:</p>
<ul>
    <li><strong>GPIO Control:</strong> Test the toggling and display of numbers on 7-segment displays.</li>
    <li><strong>ECG Signal Processing:</strong> Validate peak detection and heart rate calculation with test data in <code>ECG.txt</code>.</li>
</ul>

<h2>Resources</h2>
<ul>
    <li><a href="https://www.xilinx.com/products/design-tools/vivado.html">Vivado Design Suite</a></li>
    <li><a href="https://www.xilinx.com/support/documentation/application_notes/xapp502.pdf">MicroBlaze Processor Documentation</a></li>
</ul>



</body>
</html>
