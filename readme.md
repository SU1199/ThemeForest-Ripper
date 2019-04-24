# ThemeForest Ripper
[![](https://www.jack-the-ripper.org/images/ghost-image.jpg))](http://binarymaniac.com/2019/04/24/selenium-script-to-download-any-theme/)

Python script to download any theme (non-WordPress) from ThemeForest using selenium.

## Usage

- Clone the GitHub repository `clone https://github.com/SU1199/ThemeForest-Ripper.git`
- Download and install [chrome-webdriver](http://chromedriver.chromium.org/downloads) for your chrome version.
- Open virtualenv `source bin/activate`
- Install selenium `pip3 install selenium`

#### Command - `python3 ripper.py <theme-url> <download-location>`
##### Example - `python3 ripper.py https://themeforest.net/item/hervin-creative-ajax-portfolio-showcase-slider-template/23559741?s_rank=1 ../extract`

#### [Demo Video](https://www.youtube.com/watch?v=kEI3jOp1ygo&feature=youtu.be)

## How to prevent theme piracy
Short answer - You can't. All the major components of themes (js/css/html) are rendered on the client side. So no theme is fully immune to web-scraping.
However you can make it difficult. Here are some ideas -

- Use [unescape](https://www.w3schools.com/jsref/jsref_unescape.asp) to encrypt html and use JavaScript to decrypt html on page load.
- Use a cdn with user authentication to deliver resources.
- Use website encryption software(?) . I am a bit sceptical of those.
- Add some tracking code to the theme to track the websites using the theme without permission and file cease and desist against defaulters (near impossible).

## What is envato doing about it ?
- Making/Designing themes and templates is the major source of income for many web-designers. ThemeForest being the mediator of commerce has the main responsibility to protect the interests of creators. They should have a solution in place for developers to protect their creations against theft. 
- Extended support and extended licences are not enough given that envato rarely enforces the licence terms and majority of people don't buy extended license in the first place.

[What do you guys think is the best way to protect themes from piracy ?](mailto:hello@danishjoshi.com)

Maybe i'll release a cloud hosted web-app of this script in the future..