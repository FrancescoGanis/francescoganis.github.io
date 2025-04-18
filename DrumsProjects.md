---
layout: post
title: Drums and Ryhthm Projects
description: A collection of projects realeted to drums and rhythm
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

<p>Here you can find three projects related to drums, movement analysis and beat perception:</p>

<nav id="toc">
<ul>
    <li><a href="#conductive-cajon">Conductive Cajón</a></li>
    <li><a href="#perceived-danceability">Beat Precision and Perceived Danceability</a></li>
    <li><a href="#laban-movement-analysis">Laban Movement Analysis for Drum Technique</a></li>
</ul>
</nav>

<h1 id="conductive-cajon">Conductive Cajón</h1>

<div style="text-align: center;">
    <span class="image main">
        <iframe src="https://www.youtube-nocookie.com/embed/7WtAIyE0Rm8?si=9bHUYgo2i1Orogqr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="min-height: 200px; width: 100%; aspect-ratio: 16/9;"></iframe>
    </span>
</div>

<h2>What is it?</h2>
<p>The Conductive Cajón is a <a href="https://nime.org">NIME (New Interfaces for Musical Expression)</a> that enhances the traditional cajón. Equipped with sensors and a microcontroller, it adds digital sound synthesis and sample triggering, offering a novel way to play and interact with the instrument.</p>

<h2>Why is it important?</h2>
<p>NIME is a well-established field where researchers and musicians design and explore innovative ways of interacting with existing musical instruments or creating entirely new ones. This project stems from my personal interest in percussion instruments and my desire to discover new ways of engaging with the cajón.</p>

<h2>How does it work?</h2>
<p>
<span class="image right"><img src="{% link assets/images/Cajon_Strip_Circuit.png %}" alt="Circuit of the conductive strip."/><br><em style="display: block; text-align: center; font-size: 0.9em;">Sketch of the circuit for the conductive strip.</em></span></p>
<p>The Conductive Cajón is equipped with two piezoelectric triggers on the batter panel, a resistive touch input made of conductive paint on one side, an IMU, and a Bela BeagleBone Black microcontroller. The software running on the Bela is written in SuperCollider and features two mapping modalities with sample triggering and embedded sound synthesis. Users can interact with the batter panel to activate the triggers, use one hand to play the touch input strip, and tilt the cajón to modulate various parameters through the IMU.</p>


<h2>Who is involved?</h2>
<p>This project was a "mini-project" as part of my Master's degree in Sound and Music Computing, specifically for the course "New Interfaces for Musical Expression", supervised by <a href="https://vbn.aau.dk/en/persons/dano">Associate Prof. Daniel Overholt</a>.</p>

<h2>Can I see more?</h2>
<p>Unfortunately, there is no additional publicly available documentation.</p>

<br>
<br>

<h1 id="perceived-danceability">Beat Precision and Perceived Danceability</h1>

<h2>What is it?</h2>
<p>This study investigates the link between micro-timing variations in live-played rhythms and the perceived "danceability"—the urge to move when you hear the music. The hypothesis is that these variations by real drummers enhance the groove's danceability. How much do these changes affect our perception? Can listeners, musicians or not, recognize these timing shifts?</p>


<h2>Why is it important?</h2>
<p><p>In contemporary music, drummers tweak rhythms to create a specific feel through micro-timing variations. These small adjustments shift the beats' timing based on preference, genre, and tempo, making the rhythm more dynamic and engaging. The term "groove" describes rhythms that make you want to move, thanks to these subtle timing changes.</p></p>

<h2>How does it work?</h2>
<span class="image right"><img src="{% link assets/images/Drums_Patterns.jpg %}" alt="Scores of the drums' patterns."/><br><em style="display: block; text-align: center; font-size: 0.9em;">Grooves played in the study.</em></span>

<p>The study was conducted through a listening test where participants rated the danceability of drum patterns with different timing styles (laid-back, on-beat, pushed). Drummers' performances were recorded and analyzed for micro-timing variations. These recordings were then mixed and presented to participants via Google Forms, which included recordings of the drum patterns. Participants listened to the tracks and rated their danceability on a Likert scale. The experiment also included randomization to minimize bias and ensure the reliability of the results.</p>

<p>The results showed that on-beat grooves were perceived as the most danceable, while laid-back and pushed styles had lower danceability ratings. This suggests that precise timing in drumming is crucial for enhancing the danceability of music.</p>


<h2>Who is involved?</h2>
<p>This project was a "mini-project" as part of my Master's degree in Sound and Music Computing, specifically for the course "Music Perception and Cognition", supervised by <a href="https://vbn.aau.dk/en/persons/sof">Associate Prof. Sofia Dahl</a>.</p>

<h2>Can I see more?</h2>
<p>The project was published at the RITMO Rhythm Production and Perception Workshop 2021, and the poster can be found <a href="https://vbn.aau.dk/ws/portalfiles/portal/468862621/Ganis_Beat_Precision_Danceability_RPPW21.pdf">here</a>.</p>


<br>
<br>

<h1 id="laban-movement-analysis">Laban Movement Analysis for Drum Technique</h1>
<p><span class="image main"><video width="100%" autoplay loop muted>
    <source src="{% link assets/images/Comparison_Techniques.webm %}" type="video/mp4">
    Your browser does not support the video tag.
</video><br><em style="display: block; text-align: center; font-size: 0.9em;">Video analysis with skeleton overlay</em></span></p>

<h2>What is it?</h2>
<p>This mini-project analyzes the differences between a drum stroke performed using the <a href="https://en.wikipedia.org/wiki/Moeller_method">Moeller technique</a> and a stroke executed in a rigid, mechanical manner, typical of beginners. The analysis is conducted offline using webcam recordings and various descriptors to identify the differences.</p>

<h2>Why is it important?</h2>
<p>Natural and fluid movement is essential when playing any instrument. This project aims to use simple technology, like a webcam and a script, to spot differences in stroke execution. With further development, it could potentially become a valuable training tool for drummers, requiring only a laptop or mobile device with a front-facing camera.</p>

<h2>How does it work?</h2>
<p>The program uses a webcam video recording of a person seated in front of it to detect body joints with <a href="https://github.com/CMU-Perceptual-Computing-Lab/openpose">OpenPose</a>. The data files contain 25 body joints and 21 joints for each hand. These joints are described as points moving in a two-dimensional space over time, and their coordinates are analyzed using the <a href="https://github.com/mocaptoolbox">MOCAP Toolbox</a> and the <a href="https://dl.acm.org/doi/10.1145/2790994.2790998">Laban Effort descriptors</a>: weight, time, space, and flow. By comparing the datasets from the correct and incorrect technique executions, it is possible to identify differences and distinguish the correct technique from the wrong one.</p>

<span class="image main"><img src="{% link assets/images/LMA_LeftHand.png %}" alt="LMA Descriptors for the left hand" /><br><em style="display: block; text-align: center; font-size: 0.9em;">LMA analysis for the left hand comparing the correct (Moeller) and wrong techniques.</em></span>

<h2>Who is involved?</h2>
<p>This project was a mini-project as part of my Master's degree in Sound and Music Computing, specifically for the course "Embodied Interaction," supervised by <a href="https://vbn.aau.dk/en/persons/cer">Associate Prof. Cumhur Erkut</a>.</p>

<h2>Can I see more?</h2>
<p>Unfortunately, there is no additional publicly available documentation.</p>


<br>
<div style="text-align: center;">
<ul class="actions">
<li><a href="Portfolio.html" class="button">Back to Portfolio</a></li>
</ul>
</div>


