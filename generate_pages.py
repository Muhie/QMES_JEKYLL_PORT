#!/usr/bin/env python3
"""
Generate additional static pages for QMES website
"""

import os
from jinja2 import Template

def generate_about_us():
    """Generate about-us.html"""
    print("Generating about-us.html...")
    
    content = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link href="https://fonts.googleapis.com/css?family=Nunito:200,300,400,700" rel="stylesheet">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
        <link rel="stylesheet" href="styles/Styles.css">
        <title>QMES - Become a Member</title>
    </head>
    <body>
        <nav id="mainNavbar" class="navbar navbar-dark navbar-expand-md py-0 sticky-top">
            <a href="index.html" class="navbar-brand">
                <img class="navbar-team-logo" src="images/logo.png" alt="team logo">
            </a>
            <button class="navbar-toggler" data-toggle="collapse" data-target="#navLinks">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navLinks">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a href="index.html" class="nav-link">HOME</a>
                    </li>
                    <li class="nav-item">
                        <a href="about-us.html" class="nav-link active">BECOME A MEMBER</a>
                    </li>
                    <li class="nav-item">
                        <a href="our-progress.html" class="nav-link">OUR PROGRESS</a>
                    </li>
                    <li class="nav-item">
                        <a href="gallery.html" class="nav-link">GALLERY</a>
                    </li>
                    <li class="nav-item">
                        <a href="contact.html" class="nav-link">CONTACT US</a>
                    </li>
                </ul>
            </div>
        </nav>
        
        <div>
            <h1 class="heading-subtitle"><strong>Become a Member of QMES!</strong></h1>
        </div>
        
        <div class="container-fluid" style="margin: 15px;">
            <div class="row">
                <div class="col-md-6 col-sm-12">
                    <h2 class="line">Why Join QMES?</h2>
                    <p class="body-content">Join the Queen Mary Electronics Society to:</p>
                    <ul class="body-content">
                        <li>Learn electronics, programming, and robotics</li>
                        <li>Participate in exciting competitions</li>
                        <li>Network with like-minded students</li>
                        <li>Gain hands-on experience with real projects</li>
                        <li>Build your portfolio and skills</li>
                    </ul>
                </div>
                <div class="col-md-6 col-sm-12">
                    <h2 class="line">How to Join</h2>
                    <p class="body-content">To become a member:</p>
                    <ol class="body-content">
                        <li>Attend our weekly meetings</li>
                        <li>Fill out our membership form</li>
                        <li>Pay the annual membership fee</li>
                        <li>Start participating in our activities!</li>
                    </ol>
                </div>
            </div>
        </div>
        
        <div class="footer-sticky">
            <div class="container-fluid">
                <div class="line-light">
                    <nav class="navbar-dark navbar-expand-md py-0 sticky-top">
                        <ul class="navbar-nav justify-content-center">
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="index.html">Home</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://twitter.com/" target="_blank">Twitter</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://www.youtube.com/" target="_blank">Youtube</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://www.tiktok.com/" target="_blank">TikTok</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://www.instagram.com/" target="_blank">Instagram</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://www.facebook.com/" target="_blank">Facebook</a>
                            </li>
                        </ul>
                    </nav>
                </div>
                <br>
                <h6>This site was created for QMES by the QMES team, EST 2024</h6>
            </div>
        </div>
        
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
        <script>
            $(function () {
                $(document).scroll(function () {
                    var $nav = $("#mainNavbar");
                    $nav.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
                });
            });
        </script>
    </body>
</html>
    """
    
    with open("docs/about-us.html", "w", encoding="utf-8") as f:
        f.write(content)

def generate_our_progress():
    """Generate our-progress.html"""
    print("Generating our-progress.html...")
    
    # Sample blog posts for the progress page
    posts = [
        {
            "id": 1,
            "title": "Welcome to QMES!",
            "subtitle": "Our First Blog Post",
            "author": "QMES Team",
            "date_posted": "2024-01-15"
        },
        {
            "id": 2,
            "title": "First Robotics Competition",
            "subtitle": "A Great Success",
            "author": "QMES Team",
            "date_posted": "2024-02-20"
        }
    ]
    
    template_content = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link href="https://fonts.googleapis.com/css?family=Nunito:200,300,400,700" rel="stylesheet">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
        <link rel="stylesheet" href="styles/Styles.css">
        <title>QMES - Our Progress</title>
    </head>
    <body>
        <nav id="mainNavbar" class="navbar navbar-dark navbar-expand-md py-0 sticky-top">
            <a href="index.html" class="navbar-brand">
                <img class="navbar-team-logo" src="images/logo.png" alt="team logo">
            </a>
            <button class="navbar-toggler" data-toggle="collapse" data-target="#navLinks">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navLinks">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a href="index.html" class="nav-link">HOME</a>
                    </li>
                    <li class="nav-item">
                        <a href="about-us.html" class="nav-link">BECOME A MEMBER</a>
                    </li>
                    <li class="nav-item">
                        <a href="our-progress.html" class="nav-link active">OUR PROGRESS</a>
                    </li>
                    <li class="nav-item">
                        <a href="gallery.html" class="nav-link">GALLERY</a>
                    </li>
                    <li class="nav-item">
                        <a href="contact.html" class="nav-link">CONTACT US</a>
                    </li>
                </ul>
            </div>
        </nav>
        
        <div>
            <h1 class="heading-subtitle"><strong>Our Progress - Where are we now?</strong></h1>
        </div>
        
        <div class="row" style="margin: 15px;">
            <h2 class="line" style="margin: 15px;">Latest Posts From The QMES Team</h2>
            <div class="col-md-6 col-sm-12">
                {% for post in posts %}
                <div class="post-preview" style="margin: 15px;">
                    <a href="post-{{ post.id }}.html">
                        <h2 class="post-title">{{ post.title }}</h2>
                    </a>
                    <h3 class="post-subtitle">{{ post.subtitle }}</h3>
                    <p class="post-meta">Posted by {{ post.author }} on {{ post.date_posted }}</p>
                </div>
                {% endfor %}
            </div>
        </div>
        
        <div class="footer-sticky">
            <div class="container-fluid">
                <div class="line-light">
                    <nav class="navbar-dark navbar-expand-md py-0 sticky-top">
                        <ul class="navbar-nav justify-content-center">
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="index.html">Home</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://twitter.com/" target="_blank">Twitter</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://www.youtube.com/" target="_blank">Youtube</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://www.tiktok.com/" target="_blank">TikTok</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://www.instagram.com/" target="_blank">Instagram</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://www.facebook.com/" target="_blank">Facebook</a>
                            </li>
                        </ul>
                    </nav>
                </div>
                <br>
                <h6>This site was created for QMES by the QMES team, EST 2024</h6>
            </div>
        </div>
        
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
        <script>
            $(function () {
                $(document).scroll(function () {
                    var $nav = $("#mainNavbar");
                    $nav.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
                });
            });
        </script>
    </body>
</html>
    """
    
    template = Template(template_content)
    html_content = template.render(posts=posts)
    
    with open("docs/our-progress.html", "w", encoding="utf-8") as f:
        f.write(html_content)

def generate_gallery():
    """Generate gallery.html"""
    print("Generating gallery.html...")
    
    # Sample gallery images
    gallery_images = [
        "gallery-image-1.jpg",
        "gallery-image-2.jpg", 
        "gallery-image-3.jpg",
        "gallery-image-4.jpg",
        "gallery-image-5.jpg",
        "robot.jpg",
        "robot.png",
        "pcb.png"
    ]
    
    template_content = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link href="https://fonts.googleapis.com/css?family=Nunito:200,300,400,700" rel="stylesheet">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
        <link rel="stylesheet" href="styles/Styles.css">
        <title>QMES - Gallery</title>
    </head>
    <body>
        <nav id="mainNavbar" class="navbar navbar-dark navbar-expand-md py-0 sticky-top">
            <a href="index.html" class="navbar-brand">
                <img class="navbar-team-logo" src="images/logo.png" alt="team logo">
            </a>
            <button class="navbar-toggler" data-toggle="collapse" data-target="#navLinks">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navLinks">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a href="index.html" class="nav-link">HOME</a>
                    </li>
                    <li class="nav-item">
                        <a href="about-us.html" class="nav-link">BECOME A MEMBER</a>
                    </li>
                    <li class="nav-item">
                        <a href="our-progress.html" class="nav-link">OUR PROGRESS</a>
                    </li>
                    <li class="nav-item">
                        <a href="gallery.html" class="nav-link active">GALLERY</a>
                    </li>
                    <li class="nav-item">
                        <a href="contact.html" class="nav-link">CONTACT US</a>
                    </li>
                </ul>
            </div>
        </nav>
        
        <div>
            <h1 class="heading-subtitle"><strong>QMES Gallery</strong></h1>
        </div>
        
        <div class="container-fluid" style="margin: 15px;">
            <div class="row">
                {% for image in gallery_images %}
                <div class="col-md-4 col-sm-6 col-12" style="margin-bottom: 20px;">
                    <div class="gallery-item">
                        <img src="images/{{ image }}" alt="Gallery Image" class="img-fluid gallery-image" style="width: 100%; height: 250px; object-fit: cover; border-radius: 8px;">
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
        
        <div class="footer-sticky">
            <div class="container-fluid">
                <div class="line-light">
                    <nav class="navbar-dark navbar-expand-md py-0 sticky-top">
                        <ul class="navbar-nav justify-content-center">
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="index.html">Home</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://twitter.com/" target="_blank">Twitter</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://www.youtube.com/" target="_blank">Youtube</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://www.tiktok.com/" target="_blank">TikTok</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://www.instagram.com/" target="_blank">Instagram</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://www.facebook.com/" target="_blank">Facebook</a>
                            </li>
                        </ul>
                    </nav>
                </div>
                <br>
                <h6>This site was created for QMES by the QMES team, EST 2024</h6>
            </div>
        </div>
        
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
        <script>
            $(function () {
                $(document).scroll(function () {
                    var $nav = $("#mainNavbar");
                    $nav.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
                });
            });
        </script>
    </body>
</html>
    """
    
    template = Template(template_content)
    html_content = template.render(gallery_images=gallery_images)
    
    with open("docs/gallery.html", "w", encoding="utf-8") as f:
        f.write(html_content)

def generate_contact():
    """Generate contact.html"""
    print("Generating contact.html...")
    
    content = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link href="https://fonts.googleapis.com/css?family=Nunito:200,300,400,700" rel="stylesheet">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
        <link rel="stylesheet" href="styles/Styles.css">
        <title>QMES - Contact Us</title>
    </head>
    <body>
        <nav id="mainNavbar" class="navbar navbar-dark navbar-expand-md py-0 sticky-top">
            <a href="index.html" class="navbar-brand">
                <img class="navbar-team-logo" src="images/logo.png" alt="team logo">
            </a>
            <button class="navbar-toggler" data-toggle="collapse" data-target="#navLinks">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navLinks">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a href="index.html" class="nav-link">HOME</a>
                    </li>
                    <li class="nav-item">
                        <a href="about-us.html" class="nav-link">BECOME A MEMBER</a>
                    </li>
                    <li class="nav-item">
                        <a href="our-progress.html" class="nav-link">OUR PROGRESS</a>
                    </li>
                    <li class="nav-item">
                        <a href="gallery.html" class="nav-link">GALLERY</a>
                    </li>
                    <li class="nav-item">
                        <a href="contact.html" class="nav-link active">CONTACT US</a>
                    </li>
                </ul>
            </div>
        </nav>
        
        <div>
            <h1 class="heading-subtitle"><strong>Contact QMES</strong></h1>
        </div>
        
        <div class="container-fluid" style="margin: 15px;">
            <div class="row">
                <div class="col-md-6 col-sm-12">
                    <h2 class="line">Get in Touch</h2>
                    <p class="body-content">We'd love to hear from you! Here are the best ways to reach us:</p>
                    <ul class="body-content">
                        <li><strong>Email:</strong> qmes@qmul.ac.uk</li>
                        <li><strong>Instagram:</strong> @qmes_official</li>
                        <li><strong>Twitter:</strong> @QMES_Official</li>
                        <li><strong>Facebook:</strong> QMES Official</li>
                    </ul>
                </div>
                <div class="col-md-6 col-sm-12">
                    <h2 class="line">Location</h2>
                    <p class="body-content">Queen Mary University of London</p>
                    <p class="body-content">Mile End Road</p>
                    <p class="body-content">London E1 4NS</p>
                    <p class="body-content">United Kingdom</p>
                </div>
            </div>
        </div>
        
        <div class="footer-sticky">
            <div class="container-fluid">
                <div class="line-light">
                    <nav class="navbar-dark navbar-expand-md py-0 sticky-top">
                        <ul class="navbar-nav justify-content-center">
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="index.html">Home</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://twitter.com/" target="_blank">Twitter</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://www.youtube.com/" target="_blank">Youtube</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://www.tiktok.com/" target="_blank">TikTok</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://www.instagram.com/" target="_blank">Instagram</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link footer-link" href="https://www.facebook.com/" target="_blank">Facebook</a>
                            </li>
                        </ul>
                    </nav>
                </div>
                <br>
                <h6>This site was created for QMES by the QMES team, EST 2024</h6>
            </div>
        </div>
        
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
        <script>
            $(function () {
                $(document).scroll(function () {
                    var $nav = $("#mainNavbar");
                    $nav.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
                });
            });
        </script>
    </body>
</html>
    """
    
    with open("docs/contact.html", "w", encoding="utf-8") as f:
        f.write(content)

def main():
    """Generate all additional pages"""
    print("Generating additional static pages...")
    
    generate_about_us()
    generate_our_progress()
    generate_gallery()
    generate_contact()
    
    print("All pages generated successfully!")

if __name__ == "__main__":
    main()


