## Working with API's in JavaScript

### What are APIs ?
**Application Programming Interfaces** (APIs) are constructs made available in programming languages to allow developers to create complex functionality more easily.

### APIs in client-side JavaScript
Client-side JavaScript, in particular, has many APIs available to it — these are not part of the JavaScript language itself, rather they are built on top of the core JavaScript language, providing you with extra superpowers to use in your JavaScript code. They generally fall into two categories:

1. **Browser APIs** : are built into your web browser and are able to expose data from the browser and surrounding computer environment and do useful complex things with it.

2. **Third-party APIs**: are not built into the browser by default, and you generally have to retrieve their code and information from somewhere on the Web.

### Common browser API's
1. **APIs for manipulating documents loaded into the browser.** - The most obvious example is the DOM (Document Object Model) API, which allows you to manipulate HTML and CSS — creating, removing and changing HTML, dynamically applying new styles to your page, etc.

2. **APIs that fetch data from the server** - This seemingly small detail has had a huge impact on the performance and behavior of sites — if you just need to update a stock listing or list of available new stories, doing it instantly without having to reload the whole entire page from the server can make the site or app feel much more responsive and "snappy"

3. **APIs for drawing and manipulating graphics** - are widely supported in browsers — the most popular ones are Canvas and WebGL, which allow you to programmatically update the pixel data contained in an HTML <canvas> element to create 2D and 3D scenes.

4. **Audio and Video APIs** like HTMLMediaElement, the Web Audio API, and WebRTC allow you to do really interesting things with multimedia such as creating custom UI controls for playing audio and video, displaying text tracks like captions and subtitles along with your videos, grabbing video from your web camera to be manipulated via a canvas (see above) or displayed on someone else's computer in a web conference, or adding effects to audio tracks (such as gain, distortion, panning, etc.)

5. **Device APIs** enable you to interact with device hardware: for example, accessing the device GPS to find the user's position using the Geolocation API.

6. **Client-side storage APIs** enable you to store data on the client-side, so you can create an app that will save its state between page loads, and perhaps even work when the device is offline.


### Common third-party APIs
- Map APIs, like Mapquest and the Google Maps API, which allow you to do all sorts of things with maps on your web pages.

- The Facebook suite of APIs, which enables you to use various parts of the Facebook ecosystem to benefit your app, such as by providing app login using Facebook login, accepting in-app payments, rolling out targeted ad campaigns, etc.

- The Telegram APIs, which allows you to embed content from Telegram channels on your website, in addition to providing support for bots.

- The YouTube API, which allows you to embed YouTube videos on your site, search YouTube, build playlists, and more.

- The Pinterest API, which provides tools to manage Pinterest boards and pins to include them in your website.

- The Twilio API, which provides a framework for building voice and video call functionality into your app, sending SMS/MMS from your apps, and more.

- The Disqus API, which provides a commenting platform that can be integrated into your site.

- The Mastodon API, which enables you to manipulate features of the Mastodon social network programmatically.

- The IFTTT API, which enables integrating multiple APIs through one platform.