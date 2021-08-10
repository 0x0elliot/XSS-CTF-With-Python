# XSS CTF With Python
A Web CTF that was originally made for AppSec Village DEFCON 29 CTFs and had the name <b>"Send me something interesting!"</b>

<img src = "https://i.imgur.com/qsWsFf7.png" /><br>
<img src = "https://i.imgur.com/OyedNhN.png" />
<br>

<h1>How to launch deploy this?</h1>

<p>
  It's very simple to deploy.<br> 
  1. First go to <code>"config.py"</code> and add the ReCaptcha tokens. You can get them from <a href = "https://www.google.com/recaptcha/">here.</a><br>
  
  I have left the test keys provided by google so that it is always ready to be deployed and tested locally. Similarly, When you're deploying the CTF then it's recomended to
  change the host to whatever your host is!
  <br>
  
  2. <code>sudo docker-compose up</code> It's that simple!
</p>

<h1>Why Does this CTF exist?</h1>

<p>
  When I thought about creating a CTF, I thought I might look around in the community to understand exactly what kind of CTFs are being used out there written in Python
  and dealing with XSS. I noticed that most that I found used Js and Python integration. Often times those integrations were done through the subprocesses module using
  the command line with the link of the site that has to be visited by the bot being sent as a command line argument. I didn't like this and wanted to put in enough effort
  to make a stand-alone Python only XSS challenge that didn't require any other tech stack so that the InfoSec community can learn from each other!

</p>

<h1>Found a bug in this code Or want to improve certain aspect of it?</h1>

Go ahead, do your thing. I will respond to issues as quickly as possible for fixes. Right now, There isn't any immediate issue I would open formally as I plan on
Expanding on this CTF in upcoming events and add 2-3 more layers to it. But If you feel like doing something, I would say the frontend of the site was a bit too rushed.
If someone helped prettify it, it would be great!

<h1>Solutions by the community: </h1>

<ul>
  <li>
    <a href = "https://www.eivindarvesen.com/blog/2021/08/10/appsec-village-def-con-29-ctf-writeup">Go to the last section of this write up and you will find a section with the name "Send Me Something Interesting!"</a>
  </li>
</ul>

