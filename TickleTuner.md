---
layout: post
title: TickleTuner
description: Haptic Cover for Smartphones
image: assets/images/webp/TickleTuner_Back.webp
---

<!-- Main -->
<div id="main" class="alt">

<!-- One -->
<section id="one">
	<div class="inner">
		<header class="major">
			<!-- <h1>SoundCubes</h1> -->
		</header>


<!-- Content -->

<h2>What is it?</h2>
<p>Tickle Tuner is a haptic smartphone cover that provides high quality vibrotactile feedback. It is designed to help individuals with hearing loss to improve their experience of music and sound while using their smart devices. It has been proven to be also suitable for msucial training activities.</p>	

<h2>Why is it important?</h2>
<p>Cochlear implants have been proven to be a successful treatment for severe hearing loss. However, they do not provide the same sound quality as natural hearing. This can make it difficult for users to enjoy complex sounds such as music. Tickle Tuner aims to improve the experience of music and sound for cochlear implant users by providing vibrotactile feedback that enhances the perception of sound.</p>

<h2>How does it work?</h2>
<p><span class="image right" style="max-width: 400px;"><video width="100%" autoplay loop muted>
    <source src="{% link assets/videos/TickleTuner_Insert_Remove.webm %}" type="video/mp4">
    Your browser does not support the video tag.
</video><br><em style="display: block; text-align: center; font-size: 0.9em;">Tickle Tuner insertion and removal</em></span></p>

<h3>Hardware</h3>
<p>This prototype features a 3D-printed body composed of two handles and a sliding bridge that allows securing the phone in a smooth and simple way. The handles were obtained by scanning a clay model using the photogrammetry technique.</p> 

<p>Tickle Tuner is equipped with two high-fidelity voice coil actuators to provide powerful and accurate vibrotactile feedback. The smartphone can be connected to the cover through the USB-C port without installing any program. The USB-C delivers both the audio signal and power to the cover. The Tickle Tuner amplifies the signal coming from one channel that is streamed to the actuators, and the second channel is sent to the 3.5mm jack output (for headphones or active loudspeakers).</p>

<h3>Software</h3>
<p>To explore the possibilities offered by the Tickle Tuner, I developed a testbench app that allows separate control of audio and vibrotactile feedback. The app can generate simple sounds using a basic sequencer and envelope shaper, and it includes a pitch tracking algorithm to select specific features of the music played by an audio player. This app allows experimentation and investigation of what can be done with this prototype.</p>

<h2>Who is involved?</h2>
<p>This project is a collaboration between the <a href="https://melcph.create.aau.dk">Multisensory Experience Lab at Aalborg University</a> and Oticon Medical. It has been supervised by <a href="https://vbn.aau.dk/en/persons/107881">Prof. Stefania Serafin</a> and Marianna Vatti.</p>

<h2>What have I learned?</h2>
<p>I designed, developed, programmed, and built the system. I learned about haptics and vibrotactile feedback, 3D printing, audio programming, rapid audio app prototyping, and data analysis.</p> 

<h2>Can I see more?</h2>
<p>There is article that provides in-depth information about the Tickle Tuner. You can find it <a href="https://link.springer.com/chapter/10.1007/978-3-031-15019-7_2">here</a>.</p>


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
