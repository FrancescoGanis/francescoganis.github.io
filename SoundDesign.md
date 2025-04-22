---
layout: post
title: Sound Design Projects
description: A collection of projects realeted to sound design and sound synthesis
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

<p>These projects explore sound design for autonomous vehicles. The first focuses on continuous auditory feedback for passenger safety and comfort. The second uses bubble sounds and physical modeling for intuitive navigation cues. Both aim to enhance interaction between passengers and autonomous systems through sound.</p>

<nav id="toc">
<ul>
    <li><a href="#continuous-sonification">Continuous Sonification for Autonomous Driving Vehicles</a></li>
    <li><a href="#sonification-bubbles">Bubble Generator and an Ideal Bar for Autonomous Vehicles Sonification</a></li>
</ul>
</nav>

<h1 id="continuous-sonification">Continuous Sonification for Autonomous Driving Vehicles</h1>

<span class="image main"><img src="{% link assets/images/ADV_Sleep.jpg %}" alt="Person sleeping while on an autonomous driving vehicle" /></span>

<h2>What is it?</h2>
<p>This is a first attempt to provide auditory feedback to passengers of fully autonomous vehicles. The idea consists of providing continuous sound feedback that adapts to the situation on the road and eventually draws the attention of the occupants to take over driving and intervene in emergency situations.</p>

<h2>Why is it important?</h2>
<p>In <a href="https://www.sae.org/standards/content/j3016_202104/">level 4 autonomous vehicles</a>, passengers might need to intervene in emergencies but can relax or engage in leisure activities otherwise. Motion sickness, anxiety, and alertness can negatively impact their experience. A simple drone-like sound that blends into the background while increasing alertness when needed aims to mitigate these issues.</p>

<h2>How does it work?</h2>
<p>Three different levels of sound information, along with a neutral sound combining FM and granular synthesis, were designed. The synthesizers were created in MAX MSP 8, featuring multiple voices, presets, recording, and visualization capabilities. To assess the efficacy of the proposed sounds, several audio samples were generated and a pool of 20 participants was asked to rate the perceived urgency while listening to them. The evaluation showed a high rate of accordance between the intended information and the perceived urgency by the participants (85% of the cases).</p>

<div class="row">
    <div class="6u 12u$(small)">
        <span class="image fit" style="max-width: 500px;"><img src="{% link assets/images/AE_FM.jpg %}" alt="Screenshot of the sound synthesis generator" /><br><em style="display: block; text-align: center; font-size: 0.9em;">Multi-voice FM synthesis generator made in MAX MSP.</em></span>
    </div>
    <div class="6u 12u$(small)">
        <span class="image fit" style="max-width: 500px;"><img src="{% link assets/images/AE_Granular.jpg %}" alt="Screenshot of the sound synthesis generator" /><br><em style="display: block; text-align: center; font-size: 0.9em;">Multi-voice granular synthesis generator made in MAX MSP.</em></span>
    </div>
</div>

<h2>Who is involved?</h2>
<p>This project was a thesis for the Bachelor's program in Electronic Music and Sound Technician at the Conservatory of Music "Cesare Pollini" in Padova. The thesis was supervised by <a href="https://it.linkedin.com/in/nbernardini">Prof. Nicola Bernardini</a>.</p>

<h2>What have I learned?</h2>
<p>Through this project, I gained hands-on experience with sound synthesis techniques, designing and programming synthesizers in MAX/MSP, applying sound design principles, conducting user evaluations, and exploring the intersection of auditory feedback and human-computer interaction.</p>


<h2>Can I see more?</h2>
<p>Unfortunately, there is no additional publicly available documentation.</p>

<br>
<br>


<h1 id="sonification-bubbles">Bubbles and an Ideal Bar for Autonomous Vehicles Sonification</h1>

<div style="text-align: center;">
    <span class="image main">
        <iframe src="https://www.youtube.com/embed/CMKcBtrwiUg?si=CP7CH1HhnsPnEwCH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="min-height: 200px; width: 100%; aspect-ratio: 16/9;"></iframe>
    </span>
</div>

<h2>What is it?</h2>
<p>This project is a second iteration for the sonification of autonomous vehicles using bubble sounds and a dampened bar model. Inspired by techniques to <a href="https://opinvisindi.is/bitstream/handle/20.500.11815/702/paper_IJHCS_pre-print.pdf?sequence=3">guide the blind individuals</a>, the outcome of the project is two real-time audio plug-ins for Digital Audio Workstations (DAWs) that can be used as a starting point for a sonification process.</p>

<h2>Why is it important?</h2>
<p>Sonification adds a safety layer by converting visual information into sound, helping drivers understand their surroundings better. This project aims to enhance autonomous driving systems with audio technology.</p>

<h2>How does it work?</h2>
<p><span class="image right"><img src="{% link assets/images/Arrow_Bubbles.jpg %}" alt="Sketch of bubbles and turning direction."/><br><em style="display: block; text-align: center; font-size: 0.9em;">Possible mapping between bubbles, distance, and direction of the turn.</em></span></p>

<p>The sound informs passengers about the vehicle's direction on a pre-planned route, such as turning at an intersection. Bubble sounds are used because they can be easily parameterized, with the rate of bubbles per second being a key sonification parameter. The bubble generator works in real-time, controlling the rate, intensity, and panning of bubbles. The sonification is controlled according to the path and played through the car's audio system. Anticipating the car's movements might reduce anxiety and motion sickness in passengers who are unaware of the vehicle's next actions.</p>

<p>The plug-ins are made using physical models that accurately describe the properties of bubbles and ideal bars to provide full control over the generating parameters. Connecting the output of the Bubble Plug-in with the Ideal Bar plug-in can produce interesting sounds.</p>

<h3>Bubble Plug-in</h3>
<!-- <span class="image right"><img src="{% link assets/images/Bubbles_PlugIn.jpg %}" alt="Bubble plug-in."/><br><em style="display: block; text-align: center; font-size: 0.9em;">Bubble plug-in</em></span> -->
<p>The Bubble plug-in generates sounds that mimic bubbles rising through a liquid. Here's how it works:</p>
<ul>
    <li><strong>Bubble Creation:</strong> Each bubble has a specific size (radius), depth in the liquid, and a rising pitch (sound frequency that increases as the bubble rises).</li>
    <li><strong>Sound Generation:</strong> The sound of each bubble is created using mathematical formulas that consider its size, depth, and how quickly its pitch rises.</li>
    <li><strong>User Control:</strong> The plug-in allows users to control the number of bubbles per second, their intensity, and their position in the stereo sound field.</li>
</ul>

<h3>Ideal Bar Plug-in</h3>
<!-- <span class="image right"><img src="{% link assets/images/FDS_Bar_Plugin.jpg %}" alt="Ideal bar plug-in."/><br><em style="display: block; text-align: center; font-size: 0.9em;">Ideal Bar plug-in</em></span> -->
<p>The Ideal Bar plug-in simulates the sound of a vibrating bar, like a metal or wooden rod. Here's how it works:</p>
<ul>
    <li><strong>Bar Properties:</strong> The bar has properties like length, radius, material density, and elasticity (how easily it bends).</li>
    <li><strong>Sound Generation:</strong> The sound is generated by exciting the bar (making it vibrate) and applying dampening (reducing the vibration over time).</li>
    <li><strong>User Control:</strong> Users can control the bar's properties, the type of excitation (internal or external), and the dampening factors.</li>
</ul>

<!-- <span class="image main"><img src="{% link assets/images/Car_Bubbles.jpg %}" alt="Sketch of the sonification concept with bubbles" /><br><em style="display: block; text-align: center; font-size: 0.9em;">Simple sketch of how the sonification panning might happen.</em></span> -->

<h2>Who is involved?</h2>
<p>This project was a "mini-project" as part of a Master's degree in Sound and Music Computing, specifically for the course "Physical Models and Sound Synthesis," supervised by <a href="https://vbn.aau.dk/en/persons/107881">Prof. Stefania Serafin</a>.</p>

<h2>What have I learned?</h2>
<p>During this project, I gained knowledge of finite-difference schemes and their real-time implementation, explored physical models for sound synthesis, and deepened my understanding of fundamental sound design concepts.</p>

<h2>Can I see more?</h2>
<p>Unfortunately, there is no additional publicly available documentation.</p>


<br>
<div style="text-align: center;">
<ul class="actions">
<li><a href="Portfolio.html" class="button">Back to Portfolio</a></li>
</ul>
</div>


