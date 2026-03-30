---
layout: post
title: Movement Sonification
description: A project exploring sound and movement performance sonification
image:
---

<!-- Main -->
<div id="main" class="alt">

<!-- One -->
<section id="one">
	<div class="inner">
		<header class="major">
		</header>


<!-- Content -->
<h2>What is it?</h2>
<p>This project explores the sonification of movement through an iterative approach and co-creation process between a team of developers and two professional dancers. We designed two different instruments that sonify dancers' movements in real-time, creating a loop between movement and sound: the dancers' movements modified the sound, and the sound affected the choreography.</p>

<h2>Why is it important?</h2>
<p></p>

<h2>How does it work?</h2>
<p> We developed two parallel instruments, each with a different approach to sonification. The first instrument is a wearable self-resonating instrument that uses the Larsen effect to create sound based on the dancers' movements. The second instrument is a synthesizer that implements gutter synthesis, controlled by a real-time camera-based motion capture system that analyzes the dancers' movements without any wearable components.</p>

<p>The feedback instrument features a 24-bands filter bank, with automatic gain to ensure a control on resonances and keep the feedback (Larsen effect) stable and follow specific design rules. The system is weared by each performer, and composed by a Lyra T board, a microphone, a loudspeaker, and an IMU. A host computer runs a SuperCollider patch allowing the composer to control the feedback parameters in real-time using OSC commands directly sent on the dancers' devices. This design creates a loop of interactions between the performers, the movements, the sounds, and the composer.</p>

<p>The gutter synthesis instrument is based on a Max/MSP patch that implements the synthesis technique. The system uses a camera-based motion capture system (TRT Pose) running on a NVIDIA Jetson Nano to track the dancers' movements in real-time, extracting features such as position, velocity, and acceleration of each body joint (18 body joints per dancer). These features are then mapped to Laban descriptors used to control various parameters of the gutter synthesis algorithm, allowing the dancers to control the sound through their movements. The system is designed to be flexible and adaptable, allowing for different mappings and configurations based on the choreography and performance context.</p>

<h2>Who is involved?</h2>
<p>This project is part of my second semester as a Master's student in Sound and Music Computing at Aalborg University, together with Gianluca Elia and Robin Otterbein. It was supervised by <a href="https://vbn.aau.dk/en/persons/dano">Associate Prof. Daniel Overholt</a> and <a href="https://vbn.aau.dk/en/persons/sof">Associate Prof. Sofia Dahl.</a></p>

<h2>What have I learned?</h2>
<p>As a group member, I collaborated on the design, development, programming, and evaluation of the system. I learned about .</p> 

<h2>Can I see more?</h2>
<p></p>

<h2>Gallery</h2>
<div class="row">
	<div class="6u 12u$(small)">
		<span class="image fit" style="max-width: 500px;"><img src="{% link assets/images/webp/TickleTuner_Front.webp %}" alt="Front of the TickleTuner"/><br><em style="display: block; text-align: center; font-size: 0.9em;">Tickle Tuner front</em></span>
	</div>
	<div class="6u$ 12u$(small)">
		<span class="image fit" style="max-width: 500px;"><img src="{% link assets/images/webp/Testbench.webp %}" alt="Testbench"/><br><em style="display: block; text-align: center; font-size: 0.9em;">Testbench</em></span>
	</div>
	<div class="6u 12u$(small)">
		<span class="image fit" style="max-width: 500px;"><img src="{% link assets/images/webp/Print_Clay_Comparison.webp %}" alt="Print and Clay Comparison"/><br><em style="display: block; text-align: center; font-size: 0.9em;">Print and Clay Comparison</em></span>
	</div>
	<div class="6u$ 12u$(small)">
		<span class="image fit" style="max-width: 500px;"><img src="{% link assets/images/webp/Blender_Front-Back_Model.webp %}" alt="Blender Front and Back Model"/><br><em style="display: block; text-align: center; font-size: 0.9em;">Blender Front and Back Model</em></span>
	</div>
</div>

<br>
<div style="text-align: center;">
	<ul class="actions">
		<li><a href="Portfolio.html" class="button">Back to Portfolio</a></li>
	</ul>
</div>