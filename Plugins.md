---
layout: post
title: Plugins
description: A collection of plugins I have developed
image:
---

<!-- Main -->
<div id="main" class="alt">

<!-- One -->
<section id="one">
<div class="inner">
<header class="major">
</header>
<!-- 

<!-- Content -->

<p>Here you can find the two plug-ins I developed during my Master education.</p>

<nav id="toc">
<ul>
    <li><a href="#ddsp-in-real-time">DDSP in Real Time</a></li>
    <li><a href="#real-time-pitch-estimation">Real-time Pitch Estimation</a></li>
</ul>
</nav>

<h1 id="ddsp-in-real-time">DDSP in Real Time</h1>

<span class="image main"><img src="{% link assets/images/DDSP_Plugin.png %}" alt="DDSP Synthesizer Plugin" /></span>

<h2>What is it?</h2>
<p>The Differential Digital Signal Processing (DDSP) architecture was developed by the Google Magenta research group and released in October 2020. It allows the transfer of timbre from one audio source to another while keeping other characteristics (e.g., pitch, envelope, loudness) unaltered.</p>

<h2>Why is it important?</h2>
<p>The DDSP project has been pioneering in incorporating DSP techniques with deep learning. The flexibility of the architecture allows the preservation of the original characteristics of the input sound while changing the timbre in realistic and surprising ways. Uses can be found in speech manipulation or music production. In October 2020, when we started working on the project, there was no real-time implementation available. We decided to accept the challenge and create our own implementation. Later, other research groups and developers also took on the challenge. Google released its own real-time implementation only in <a href="https://magenta.tensorflow.org/ddsp-vst-blog">mid-2022</a>.</p>

<h2>How does it work?</h2>
<p>The algorithm can be summarized in three main steps:</p>
<ul>
    <li><strong>Feature Extraction:</strong> The system extracts features from the input audio, such as pitch, loudness, and harmonic structure.</li>
    <li><strong>Neural Network Processing:</strong> These features are fed into a neural network that has been trained on a variety of timbres. The network learns to map these features to the desired timbre.</li>
    <li><strong>Signal Reconstruction:</strong> The modified features are used to reconstruct the audio signal, preserving the original characteristics like pitch and loudness while changing the timbre.</li>
</ul>
<p>The user can choose the input sound and the target timbre from the interface. The system will then process the input sound in real-time, applying the timbre transfer and outputting the modified sound. It is also possible to play the synthesizer with a MIDI controller.</p>

<h2>Who is involved?</h2>
<p>This project is part of my first semester as a Master's student in Sound and Music Computing at Aalborg University, together with Erik F. Knudsen, Søren V. K. Lyster, Robin Otterbein, and David Südholt. It is supervised by <a href="https://vbn.aau.dk/en/persons/107881">Prof. Cumhur Erkut</a>.</p>

<h2>What have I learned?</h2>
<p>As a group member, I collaborated on the design, development, programming, and evaluation of the system. I learned about timbre transfer technology, machine learning, C++ and the JUCE framework, plug-in design and development, and software user evaluation.</p> 

<h2>Can I see more?</h2>
<p>The project was published at the Sound and Music Computing conference in 2021, and the paper can be found <a href="https://vbn.aau.dk/ws/portalfiles/portal/467128544/SMC_2021_paper_55.pdf">here</a>.</p>

<br>
<br>

<h1 id="real-time-pitch-estimation">Real-time Pitch Estimation</h1>
<span class="image main" style="width: 65%;"><img src="{% link assets/images/PitchEstimator.png %}" alt="Pitch Estimator Plugin" /></span>

<h2>What is it?</h2>
<p>It's a simple audio plug-in made in MATLAB (Audio Toolbox environment) that allows real-time pitch estimation of an audio source using the harmonic summation algorithm.</p>

<h2>Why is it important?</h2>
<p>This was a valuable learning experience that provided hands-on experience with an important technique used to estimate pitch. Being able to estimate pitch with low latency is crucial in fields like music production, speech processing, and audio analysis, where accurate and low-latency pitch estimation is essential for tasks such as tuning, transcription, and real-time audio effects.</p>

<h2>How does it work?</h2>
<p>The signal is processed in small chunks of data, called segments. The algorithm works by analyzing the frequency content of each segment and identifying the fundamental frequency based on the harmonic structure of the signal. The process can be summarized in the following steps.</p>
<ul>
For each audio segment:
    <li>Perform a frequency transform (FFT) on the segment.</li>
    <li>Calculate the harmonic summation (sum the squared magnitudes of the FFT at harmonic frequencies).</li>
    <li>Identify the frequency with the highest summation as the fundamental frequency.</li>
</ul>

<span class="image main"><img src="{% link assets/images/HS_Spectrogram.png %}" alt="Spectrogram with pitch estimation" /><br><em style="display: block; text-align: center; font-size: 0.9em;">Spectrogram of a viola playing an ascending scale. In red, the pitch estimation.</em></span>

<h2>Who is involved?</h2>
<p>This project was a "mini-project" as part of my Master's degree in Sound and Music Computing, specifically for the course "Sound and Music Signal Analysis."</p>

<h2>What have I learned?</h2>
<p>I learned about common pitch estimation algorithms, signal analysis, real-time sound processing, plug-in development, and the creation of scientific documentation.</p> 

<h2>Can I see more?</h2>
<p>Unfortunately, there is no additional publicly available documentation.</p>

<br>
<div style="text-align: center;">
<ul class="actions">
<li><a href="Portfolio.html" class="button">Back to Portfolio</a></li>
</ul>
</div>
