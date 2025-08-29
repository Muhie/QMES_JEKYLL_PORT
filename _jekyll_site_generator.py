#!/usr/bin/env python3
"""
Jekyll Site Generator for QMES Website
Converts static HTML to Jekyll format for GitHub Pages
"""

import os
import shutil
from datetime import datetime
from jinja2 import Template

# Sample blog data - you can replace this with your actual blog posts
BLOG_POSTS = [
    {
        "id": 1,
        "title": "Welcome to QMES!",
        "subtitle": "Our First Blog Post",
        "author": "QMES Team",
        "date_posted": "2024-01-15",
        "content": """
        <p>Welcome to the Queen Mary Electronics Society! We're excited to share our journey with you.</p>
        <p>Our society focuses on electronics, programming, and robotics, bringing together passionate students from Queen Mary University.</p>
        <p>Stay tuned for updates on our projects, competitions, and activities!</p>
        """
    },
    {
        "id": 2,
        "title": "First Robotics Competition",
        "subtitle": "A Great Success",
        "author": "QMES Team",
        "date_posted": "2024-02-20",
        "content": """
        <p>We recently participated in our first robotics competition and it was an amazing experience!</p>
        <p>The team worked worked hard to build and program our robot, and we learned so much in the process.</p>
        <p>Special thanks to all our sponsors and supporters who made this possible.</p>
        """
    },
    {
        "id": 3,
        "title": "Weekly Electronics Workshops",
        "subtitle": "Learning Together",
        "author": "QMES Team",
        "date_posted": "2024-03-10",
        "content": """
        <p>Our weekly electronics workshops are in full swing!</p>
        <p>Students are learning about circuit design, Arduino programming, and sensor integration.</p>
        <p>It's great to see everyone's enthusiasm and creativity in action.</p>
        """
    }
]

def create_directory(path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)

def copy_static_files():
    """Copy static files to Jekyll directory"""
    print("Copying static files...")
    
    # Copy images
    if os.path.exists("app/static/images"):
        shutil.copytree("app/static/images", "_site/images", dirs_exist_ok=True)
    
    # Copy styles
    if os.path.exists("app/static/styles"):
        shutil.copytree("app/static/styles", "_site/assets/css", dirs_exist_ok=True)

def create_jekyll_config():
    """Create _config.yml for Jekyll"""
    print("Creating Jekyll configuration...")
    
    config_content = """# Jekyll Configuration for QMES Website
title: Queen Mary Electronics Society
description: QMES - Electronics, Programming, and Robotics Society at Queen Mary University of London
url: "https://qmes.github.io" # Change this to your actual URL
baseurl: "" # Change this if using a project page

# Build settings
markdown: kramdown
highlighter: rouge
permalink: /:title/

# Collections
collections:
  posts:
    output: true
    permalink: /:title/

# Defaults
defaults:
  - scope:
      path: ""
      type: "posts"
    values:
      layout: "post"
      author: "QMES Team"
  - scope:
      path: ""
      type: "pages"
    values:
      layout: "page"

# Plugins
plugins:
  - jekyll-feed
  - jekyll-seo-tag

# Exclude from processing
exclude:
  - Gemfile.lock
  - node_modules
  - vendor
  - .git
  - .github
  - app/
  - static_site_generator.py
  - generate_pages.py
  - build_static_site.py
  - extract_blog_data.py
  - static_requirements.txt
  - STATIC_SITE_README.md
  - DEPLOYMENT_GUIDE.md
  - QUICK_START.md
  - _jekyll_site_generator.py
  - jekyll_requirements.txt
  - Jekyll_README.md
  - Jekyll_DEPLOYMENT_GUIDE.md
"""
    
    with open("_site/_config.yml", "w", encoding="utf-8") as f:
        f.write(config_content)

def create_gemfile():
    """Create Gemfile for Jekyll dependencies"""
    print("Creating Gemfile...")
    
    gemfile_content = """source "https://rubygems.org"

gem "jekyll", "~> 4.3.0"
gem "jekyll-feed", "~> 0.17"
gem "jekyll-seo-tag", "~> 2.8"

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]

# Use 0x0c number id for the command icon.
gem "jekyll-theme-minimal", "~> 0.2"
"""
    
    with open("_site/Gemfile", "w", encoding="utf-8") as f:
        f.write(gemfile_content)

def create_layouts():
    """Create Jekyll layouts"""
    print("Creating Jekyll layouts...")
    
    # Create layouts directory
    create_directory("_site/_layouts")
    
    # Default layout
    default_layout = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="{{ page.description | default: site.description }}">
    <meta name="author" content="{{ page.author | default: site.author | default: 'QMES Team' }}">
    
    <title>{% if page.title %}{{ page.title }} - {{ site.title }}{% else %}{{ site.title }}{% endif %}</title>
    
    <link href="https://fonts.googleapis.com/css?family=Nunito:200,300,400,700" rel="stylesheet">
    <link rel="icon" type="png" href="{{ '/images/robot.png' | relative_url }}">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
    <link rel="stylesheet" href="{{ '/assets/css/Styles.css' | relative_url }}">
    
    {% seo %}
</head>
<body>
    {% include navigation.html %}
    
    {{ content }}
    
    {% include footer.html %}
    
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
</html>"""
    
    with open("_site/_layouts/default.html", "w", encoding="utf-8") as f:
        f.write(default_layout)
    
    # Post layout
    post_layout = """---
layout: default
---

<div id="intro" class="p-5 text-center">
    <h1 class="mb-0 h4"><strong>{{ page.title }}</strong></h1>
    <span>Published <u>{{ page.date | date: "%B %d, %Y" }}</u> by {{ page.author }}</span>
</div>

<main class="mt-4 mb-5">
    <div class="container">
        <div class="col-md-8 mb-4">
            <section>
                {{ content }}
            </section>
        </div>
    </div>
</main>"""
    
    with open("_site/_layouts/post.html", "w", encoding="utf-8") as f:
        f.write(post_layout)
    
    # Page layout
    page_layout = """---
layout: default
---

{{ content }}"""
    
    with open("_site/_layouts/page.html", "w", encoding="utf-8") as f:
        f.write(page_layout)

def create_includes():
    """Create Jekyll includes"""
    print("Creating Jekyll includes...")
    
    # Create includes directory
    create_directory("_site/_includes")
    
    # Navigation include
    navigation = """<nav id="mainNavbar" class="navbar navbar-dark navbar-expand-md py-0 sticky-top">
    <a href="{{ '/' | relative_url }}" class="navbar-brand">
        <img class="navbar-team-logo" src="{{ '/images/logo.png' | relative_url }}" alt="team logo">
    </a>
    <button class="navbar-toggler" data-toggle="collapse" data-target="#navLinks">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navLinks">
        <ul class="navbar-nav">
            <li class="nav-item">
                <a href="{{ '/' | relative_url }}" class="nav-link {% if page.url == '/' %}active{% endif %}">HOME</a>
            </li>
            <li class="nav-item">
                <a href="{{ '/about-us/' | relative_url }}" class="nav-link {% if page.url contains '/about-us/' %}active{% endif %}">BECOME A MEMBER</a>
            </li>
            <li class="nav-item">
                <a href="{{ '/our-progress/' | relative_url }}" class="nav-link {% if page.url contains '/our-progress/' %}active{% endif %}">OUR PROGRESS</a>
            </li>
            <li class="nav-item">
                <a href="{{ '/gallery/' | relative_url }}" class="nav-link {% if page.url contains '/gallery/' %}active{% endif %}">GALLERY</a>
            </li>
            <li class="nav-item">
                <a href="{{ '/contact/' | relative_url }}" class="nav-link {% if page.url contains '/contact/' %}active{% endif %}">CONTACT US</a>
            </li>
        </ul>
    </div>
</nav>"""
    
    with open("_site/_includes/navigation.html", "w", encoding="utf-8") as f:
        f.write(navigation)
    
    # Footer include
    footer = """<div class="footer-sticky">
    <div class="container-fluid">
        <div class="line-light">
            <nav class="navbar-dark navbar-expand-md py-0 sticky-top">
                <ul class="navbar-nav justify-content-center">
                    <li class="nav-item">
                        <a class="nav-link footer-link" href="{{ '/' | relative_url }}">Home</a>
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
</div>"""
    
    with open("_site/_includes/footer.html", "w", encoding="utf-8") as f:
        f.write(footer)

def create_posts():
    """Create Jekyll blog posts"""
    print("Creating Jekyll blog posts...")
    
    # Create posts directory
    create_directory("_site/_posts")
    
    for post in BLOG_POSTS:
        # Convert date format for Jekyll
        date_obj = datetime.strptime(post['date_posted'], '%Y-%m-%d')
        jekyll_date = date_obj.strftime('%Y-%m-%d')
        
        # Create filename with Jekyll format
        filename = f"{jekyll_date}-{post['title'].lower().replace(' ', '-').replace('!', '').replace('?', '')}.md"
        
        # Create front matter and content
        post_content = f"""---
layout: post
title: "{post['title']}"
subtitle: "{post['subtitle']}"
author: "{post['author']}"
date: {jekyll_date}
categories: [blog]
tags: [qmes, electronics, robotics]
---

{post['content']}"""
        
        with open(f"_site/_posts/{filename}", "w", encoding="utf-8") as f:
            f.write(post_content)

def create_pages():
    """Create Jekyll pages"""
    print("Creating Jekyll pages...")
    
    # Create pages directory
    create_directory("_site")
    
    # Homepage (index.html)
    index_content = """---
layout: default
title: Home
---

<div class="justify-content-center donate-container">
    <div class="image-container">
        <img src="{{ '/images/pcb.png' | relative_url }}" class="image-fitter donate-image">
    </div>
</div>

<div>
    <h1 class="heading-title"><strong>Welcome to Queen Mary Electronics Society!</strong></h1>
    <br><br>
</div>

<div class="container-fluid" style="margin-bottom: 10px;">
    <div class="row">
        <div class="col-md-6 col-sm-12">
            <h2 class="line">Our Bio</h2>
            <p class="body-content">QMES was founded by a group of passionate engineers from Queen Mary, with a common interest and motivation in electronics, programming and robotics. Our society has 3 key goals:<br> 1. To host weekly electronics related activities for other STEM students, or anyone with a fascination with electronics. <br> 2. Participate in at-least 3 electronics related competitions per year. <br> 3. Provide electronics outreach and education.</p>
        </div>
        <div class="col-md-6 col-sm-12" style="margin-bottom: 15px;">
            <h2 class="line">Your QMES key members.</h2>
            <h3>President: Muhie Al Haimus<div class="row no-gutters gallery-spacing"><img class="gallery-photo" src="{{ '/images/Muhie.jpeg' | relative_url }}"></div><br>VP and Welfare Manager: Bohdan Skulimovsky<div class="row no-gutters gallery-spacing"><img class="gallery-photo" src="{{ '/images/Bohdan.jpg' | relative_url }}"></div><br>Treasurer: Rachin Dalal<div class="row no-gutters gallery-spacing"><img class="gallery-photo" src="{{ '/images/Rachin.jpeg' | relative_url }}"></div></h3>
        </div>
        <div class="col-md-6 col-sm-12">
            <h2 class="line">Our Sponsors</h2>
            <img src="{{ '/images/sponsor-board.png' | relative_url }}" alt="sponsors" class="image-fitter">
        </div>
        <div class="col-md-6 col-sm-12">
            <h2 class="line" style="margin: 10px;">Latest Posts From QMES.</h2>
            {% for post in site.posts limit:3 %}
            <div class="post-preview" style="margin: 10px;">
              <a href="{{ post.url | relative_url }}">
                <h2 class="post-title">{{ post.title }}</h2>
              </a>
              <h3 class="post-subtitle">{{ post.subtitle }}</h3>
              <p class="post-meta">Posted by {{ post.author }} on {{ post.date | date: "%B %d, %Y" }}</p>
            </div>
            {% endfor %}
        </div>
    </div>
</div>"""
    
    with open("_site/index.html", "w", encoding="utf-8") as f:
        f.write(index_content)
    
    # About page
    about_content = """---
layout: page
title: Become a Member
permalink: /about-us/
---

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
</div>"""
    
    with open("_site/about-us.html", "w", encoding="utf-8") as f:
        f.write(about_content)
    
    # Our Progress page
    progress_content = """---
layout: page
title: Our Progress
permalink: /our-progress/
---

<div>
    <h1 class="heading-subtitle"><strong>Our Progress - Where are we now?</strong></h1>
</div>

<div class="row" style="margin: 15px;">
    <h2 class="line" style="margin: 15px;">Latest Posts From The QMES Team</h2>
    <div class="col-md-6 col-sm-12">
        {% for post in site.posts %}
        <div class="post-preview" style="margin: 15px;">
            <a href="{{ post.url | relative_url }}">
                <h2 class="post-title">{{ post.title }}</h2>
            </a>
            <h3 class="post-subtitle">{{ post.subtitle }}</h3>
            <p class="post-meta">Posted by {{ post.author }} on {{ post.date | date: "%B %d, %Y" }}</p>
        </div>
        {% endfor %}
    </div>
</div>"""
    
    with open("_site/our-progress.html", "w", encoding="utf-8") as f:
        f.write(progress_content)
    
    # Gallery page
    gallery_content = """---
layout: page
title: Gallery
permalink: /gallery/
---

<div>
    <h1 class="heading-subtitle"><strong>QMES Gallery</strong></h1>
</div>

<div class="container-fluid" style="margin: 15px;">
    <div class="row">
        {% assign gallery_images = "gallery-image-1.jpg,gallery-image-2.jpg,gallery-image-3.jpg,gallery-image-4.jpg,gallery-image-5.jpg,robot.jpg,robot.png,pcb.png" | split: "," %}
        {% for image in gallery_images %}
        <div class="col-md-4 col-sm-6 col-12" style="margin-bottom: 20px;">
            <div class="gallery-item">
                <img src="{{ '/images/' | append: image | relative_url }}" alt="Gallery Image" class="img-fluid gallery-image" style="width: 100%; height: 250px; object-fit: cover; border-radius: 8px;">
            </div>
        </div>
        {% endfor %}
    </div>
</div>"""
    
    with open("_site/gallery.html", "w", encoding="utf-8") as f:
        f.write(gallery_content)
    
    # Contact page
    contact_content = """---
layout: page
title: Contact Us
permalink: /contact/
---

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
</div>"""
    
    with open("_site/contact.html", "w", encoding="utf-8") as f:
        f.write(contact_content)

def main():
    """Main function to generate the Jekyll site"""
    print("🚀 Starting Jekyll site generation...")
    
    # Create output directory
    create_directory("_site")
    
    # Generate Jekyll structure
    create_jekyll_config()
    create_gemfile()
    create_layouts()
    create_includes()
    create_posts()
    create_pages()
    
    # Copy static files
    copy_static_files()
    
    print("✅ Jekyll site generation complete!")
    print("📁 Files generated in the '_site' directory")
    print("\n🚀 Next steps:")
    print("1. cd _site")
    print("2. bundle install")
    print("3. bundle exec jekyll serve")
    print("4. View your site at http://localhost:4000")
    print("5. Push to GitHub for automatic deployment!")

if __name__ == "__main__":
    main()


