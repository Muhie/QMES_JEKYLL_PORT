# 🚀 QMES Jekyll Website

Your Flask QMES website has been converted to a modern **Jekyll static site generator**! This provides better blog management, SEO optimization, and easier content updates.

## ✨ Why Jekyll?

- **🎯 Better Blog Management** - Markdown-based posts with automatic categorization
- **🔍 SEO Optimized** - Built-in meta tags, sitemaps, and structured data
- **📱 Responsive Design** - Mobile-first approach with Bootstrap
- **🚀 GitHub Pages Native** - First-class support for GitHub Pages
- **🔄 Easy Updates** - Just edit markdown files and push
- **📊 Built-in Features** - RSS feeds, search, and more

## 🏗️ Jekyll Structure

```
_site/                          # Generated Jekyll site
├── _config.yml                 # Jekyll configuration
├── Gemfile                     # Ruby dependencies
├── index.html                  # Homepage
├── about-us.html              # About/Membership page
├── our-progress.html          # Blog listing page
├── gallery.html               # Image gallery
├── contact.html               # Contact page
├── _layouts/                  # Page layouts
│   ├── default.html           # Main layout template
│   ├── post.html              # Blog post layout
│   └── page.html              # Page layout
├── _includes/                 # Reusable components
│   ├── navigation.html        # Navigation menu
│   └── footer.html            # Footer component
├── _posts/                    # Blog posts (markdown)
│   ├── 2024-01-15-welcome-to-qmes.md
│   ├── 2024-02-20-first-robotics-competition.md
│   └── 2024-03-10-weekly-electronics-workshops.md
├── images/                    # All website images
└── assets/css/                # CSS stylesheets
```

## 🚀 Quick Start

### 1. Generate Jekyll Site

```bash
# Install Python dependencies
pip install -r jekyll_requirements.txt

# Generate Jekyll site
python _jekyll_site_generator.py
```

### 2. Test Locally

```bash
# Navigate to Jekyll directory
cd _site

# Install Ruby dependencies
bundle install

# Start local server
bundle exec jekyll serve

# View at http://localhost:4000
```

### 3. Deploy to GitHub Pages

```bash
# Push to GitHub
git add .
git commit -m "Convert to Jekyll site"
git push origin main

# GitHub Actions will automatically build and deploy!
```

## 📝 Managing Content

### Adding Blog Posts

Create new markdown files in `_site/_posts/` with this format:

```markdown
---
layout: post
title: "Your Post Title"
subtitle: "Your Post Subtitle"
author: "Your Name"
date: 2024-01-15
categories: [blog]
tags: [qmes, electronics, robotics]
---

Your content here in **Markdown** format.

- Bullet points
- Code snippets
- Images
- Links
```

### Updating Pages

Edit the HTML files in the `_site/` directory:
- `index.html` - Homepage content
- `about-us.html` - About page
- `our-progress.html` - Progress page
- `gallery.html` - Gallery page
- `contact.html` - Contact page

### Customizing Layouts

Modify files in `_site/_layouts/`:
- `default.html` - Main page structure
- `post.html` - Blog post layout
- `page.html` - Regular page layout

## 🎨 Customization

### Changing Site Settings

Edit `_site/_config.yml`:

```yaml
title: Queen Mary Electronics Society
description: QMES - Electronics, Programming, and Robotics Society
url: "https://your-username.github.io"
baseurl: "/your-repo-name"

# Add your social media links
social:
  twitter: "@qmes_official"
  instagram: "@qmes_official"
  facebook: "QMES Official"
```

### Updating Navigation

Edit `_site/_includes/navigation.html` to:
- Add new menu items
- Change navigation structure
- Update social links

### Modifying Styles

Edit `_site/assets/css/Styles.css` for:
- Color schemes
- Typography
- Layout adjustments
- Responsive design

## 🔧 Advanced Features

### Categories and Tags

Blog posts automatically support:
- **Categories**: Group posts by type (blog, news, events)
- **Tags**: Add multiple tags for better organization
- **Automatic listing**: Generate category and tag pages

### SEO Optimization

Built-in features include:
- Meta descriptions
- Open Graph tags
- Twitter Card support
- Automatic sitemap generation
- Structured data markup

### RSS Feed

Automatic RSS feed generation at `/feed.xml` for:
- Blog readers
- Email newsletters
- Social media automation

## 🚀 Deployment Options

### Option 1: GitHub Actions (Recommended)

The included workflow automatically:
1. Generates Jekyll site from Python
2. Builds with Jekyll
3. Deploys to GitHub Pages
4. Updates on every push

### Option 2: Manual Deployment

```bash
# Build site
cd _site
bundle exec jekyll build

# Deploy _site/_site folder to GitHub Pages
```

## 🛠️ Troubleshooting

### Common Issues

#### 1. Bundle Install Fails
```bash
# Update Ruby and Bundler
gem update --system
gem install bundler
bundle install
```

#### 2. Jekyll Build Errors
```bash
# Check Jekyll version
jekyll --version

# Clean and rebuild
bundle exec jekyll clean
bundle exec jekyll build
```

#### 3. Missing Dependencies
```bash
# Install system dependencies (Ubuntu/Debian)
sudo apt-get install ruby-full build-essential

# Install system dependencies (macOS)
brew install ruby
```

### Debugging

1. **Check Jekyll logs**: `bundle exec jekyll serve --verbose`
2. **Validate front matter**: Use online YAML validators
3. **Check file permissions**: Ensure all files are readable
4. **Verify Ruby version**: Use Ruby 2.7+ for Jekyll 4.x

## 📚 Jekyll Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Jekyll Themes](https://jekyllthemes.io/)
- [Liquid Template Language](https://shopify.github.io/liquid/)
- [Markdown Guide](https://www.markdownguide.org/)

## 🔄 Migration from Static HTML

### What Changed

- ✅ **HTML → Markdown**: Blog posts now use Markdown
- ✅ **Manual → Automatic**: Navigation and layouts are automatic
- ✅ **Static → Dynamic**: Content is generated from data
- ✅ **Basic → Advanced**: SEO, feeds, and more features

### What Stayed the Same

- ✅ **Design**: All visual styling preserved
- ✅ **Content**: All your content maintained
- ✅ **Images**: All images and assets preserved
- ✅ **Functionality**: All features working

## 🎯 Next Steps

1. **Customize Content**: Update blog posts and pages
2. **Add Features**: Implement search, comments, or analytics
3. **Optimize SEO**: Add meta descriptions and keywords
4. **Deploy**: Push to GitHub for automatic deployment
5. **Monitor**: Check analytics and performance

## 🆘 Support

For Jekyll-specific issues:
1. Check the troubleshooting section above
2. Review Jekyll documentation
3. Check GitHub Actions logs
4. Verify Ruby and Jekyll versions

Your QMES website is now a modern, powerful Jekyll site ready for the world! 🚀


