# 🚀 Jekyll Deployment Guide for QMES Website

This guide will walk you through deploying your converted Jekyll QMES website to GitHub Pages with automatic builds and deployments.

## 🎯 What You Get with Jekyll

- **📝 Markdown Blog Posts** - Easy content management
- **🔍 SEO Optimization** - Built-in meta tags and sitemaps
- **📱 Responsive Design** - Mobile-first approach
- **🚀 GitHub Pages Native** - First-class support
- **🔄 Automatic Deployment** - Updates on every push
- **📊 Advanced Features** - RSS feeds, categories, tags

## 📋 Prerequisites

- ✅ GitHub account
- ✅ QMES website repository on GitHub
- ✅ Ruby 2.7+ installed (for local testing)
- ✅ Jekyll site generated (using the provided scripts)

## 🚀 Step 1: Generate Your Jekyll Site

### 1.1 Install Python Dependencies

```bash
pip install -r jekyll_requirements.txt
```

### 1.2 Generate Jekyll Site

```bash
python _jekyll_site_generator.py
```

This creates the `_site/` directory with your complete Jekyll website.

### 1.3 Verify Generated Files

Your `_site/` directory should contain:

```
_site/
├── _config.yml                 # Jekyll configuration
├── Gemfile                     # Ruby dependencies
├── index.html                  # Homepage
├── about-us.html              # About page
├── our-progress.html          # Blog listing
├── gallery.html               # Image gallery
├── contact.html               # Contact page
├── _layouts/                  # Page layouts
├── _includes/                 # Reusable components
├── _posts/                    # Blog posts (markdown)
├── images/                    # All images
└── assets/css/                # CSS files
```

## 🧪 Step 2: Test Locally (Optional but Recommended)

### 2.1 Install Ruby Dependencies

```bash
cd _site
bundle install
```

### 2.2 Start Local Server

```bash
bundle exec jekyll serve
```

### 2.3 View Your Site

Open `http://localhost:4000` in your browser to preview your site locally.

## 📤 Step 3: Deploy to GitHub

### 3.1 Push Your Code

```bash
# Add all files
git add .

# Commit changes
git commit -m "Convert to Jekyll site for GitHub Pages"

# Push to GitHub
git push origin main
```

### 3.2 Enable GitHub Pages

1. Go to your GitHub repository
2. Click **Settings** tab
3. Scroll to **Pages** section (left sidebar)
4. Under **Source**, select **Deploy from a branch**
5. Under **Branch**, select **main** (or your default branch)
6. Under **Folder**, select **/ (root)**
7. Click **Save**

**Note**: For Jekyll sites, we deploy from the root directory, not `/docs`.

## 🔄 Step 4: Automatic Deployment with GitHub Actions

### 4.1 How It Works

The included `.github/workflows/jekyll-deploy.yml` automatically:

1. **Generates Jekyll site** from your Python scripts
2. **Builds with Jekyll** using Ruby and Bundler
3. **Deploys to GitHub Pages** on every push
4. **Uses gh-pages branch** for deployment

### 4.2 Verify Workflow

1. Go to your repository **Actions** tab
2. You should see the "Deploy Jekyll to GitHub Pages" workflow
3. Click on it to see the build process
4. Green checkmark means successful deployment

### 4.3 Deployment Time

- **First deployment**: 5-10 minutes
- **Subsequent updates**: 2-5 minutes
- **Automatic**: Every push triggers a new deployment

## 📝 Step 5: Managing Content

### 5.1 Adding Blog Posts

Create new markdown files in `_site/_posts/`:

```markdown
---
layout: post
title: "Your New Post Title"
subtitle: "Your Post Subtitle"
author: "Your Name"
date: 2024-01-20
categories: [blog]
tags: [qmes, electronics, robotics]
---

Your content here in **Markdown** format.

## Subheadings

- Bullet points
- More content
- Images and links
```

### 5.2 Updating Pages

Edit HTML files in the `_site/` directory:
- `index.html` - Homepage content
- `about-us.html` - About page
- `our-progress.html` - Progress page
- `gallery.html` - Gallery page
- `contact.html` - Contact page

### 5.3 Customizing Layouts

Modify files in `_site/_layouts/`:
- `default.html` - Main page structure
- `post.html` - Blog post layout
- `page.html` - Regular page layout

## 🔧 Step 6: Customization

### 6.1 Site Configuration

Edit `_site/_config.yml`:

```yaml
title: Queen Mary Electronics Society
description: QMES - Electronics, Programming, and Robotics Society
url: "https://your-username.github.io"
baseurl: "/your-repo-name"

# Add your social media
social:
  twitter: "@qmes_official"
  instagram: "@qmes_official"
  facebook: "QMES Official"
```

### 6.2 Navigation Updates

Edit `_site/_includes/navigation.html` to:
- Add new menu items
- Update social links
- Change navigation structure

### 6.3 Styling Changes

Edit `_site/assets/css/Styles.css` for:
- Color schemes
- Typography
- Layout adjustments
- Responsive design

## 🚀 Step 7: Update and Deploy

### 7.1 After Making Changes

```bash
# Regenerate Jekyll site (if you modified the generator)
python _jekyll_site_generator.py

# Commit and push changes
git add .
git commit -m "Update website content"
git push origin main
```

### 7.2 Automatic Deployment

GitHub Actions will automatically:
1. Generate the Jekyll site
2. Build with Jekyll
3. Deploy to GitHub Pages
4. Update your live site

## ✅ Step 8: Verify Deployment

### 8.1 Check GitHub Pages Status

1. Go to repository **Settings** → **Pages**
2. Look for green checkmark indicating successful deployment
3. Note the deployment time and URL

### 8.2 Test Your Live Site

1. Visit your deployed URL
2. Test all navigation links
3. Verify blog posts load correctly
4. Check responsive design on mobile
5. Test image loading and gallery

### 8.3 Check GitHub Actions

1. Go to **Actions** tab
2. Verify workflow completed successfully
3. Check for any error messages
4. Monitor deployment times

## 🛠️ Troubleshooting

### Common Issues

#### 1. Site Not Loading

- Check GitHub Pages is enabled
- Verify source is set to root directory (not `/docs`)
- Wait 5-10 minutes for deployment
- Check repository settings

#### 2. Jekyll Build Failures

- Check GitHub Actions logs for errors
- Verify Ruby version compatibility
- Check for syntax errors in markdown files
- Validate YAML front matter

#### 3. Missing Images or Styles

- Ensure all files exist in `_site/` directory
- Check file paths in templates
- Verify file permissions
- Check for typos in filenames

#### 4. GitHub Actions Failures

- Check Actions tab for error details
- Verify workflow file syntax
- Check repository permissions
- Ensure Ruby and Jekyll versions are compatible

### Debugging Steps

1. **Check GitHub Actions logs** for detailed error messages
2. **Verify file structure** in `_site/` folder
3. **Test locally** with `bundle exec jekyll serve`
4. **Validate markdown** using online validators
5. **Check YAML syntax** in `_config.yml`

## 🔄 Maintenance

### Regular Updates

1. **Content Updates**: Edit markdown files and push
2. **Image Updates**: Replace files in `_site/images/`
3. **Style Updates**: Modify `_site/assets/css/Styles.css`
4. **Layout Updates**: Edit files in `_site/_layouts/`

### Backup Strategy

- Keep your original Flask app files
- Version control all changes
- Regular backups of `_site/` directory
- Document any custom modifications

## 🎯 Advanced Features

### SEO Optimization

- Add meta descriptions to pages
- Include Open Graph tags
- Optimize image alt text
- Add structured data markup

### Analytics Integration

- Add Google Analytics tracking code
- Include in `_site/_layouts/default.html`
- Monitor site performance
- Track user engagement

### Custom Domain

1. Add custom domain in repository Settings → Pages
2. Configure DNS records
3. Add `CNAME` file to `_site/` directory
4. Wait for DNS propagation

## 📚 Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages with Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll)
- [Liquid Template Language](https://shopify.github.io/liquid/)
- [Markdown Guide](https://www.markdownguide.org/)

## 🎉 Success!

After following this guide, you'll have:

✅ **Modern Jekyll website** with advanced features  
✅ **Automatic deployment** on every push  
✅ **SEO optimization** built-in  
✅ **Easy content management** with Markdown  
✅ **Professional appearance** with responsive design  
✅ **GitHub Pages hosting** with automatic updates  

Your QMES website is now a powerful, modern Jekyll site that automatically deploys to GitHub Pages! 🚀

## 🆘 Need Help?

1. **Check troubleshooting section** above
2. **Review Jekyll documentation**
3. **Check GitHub Actions logs**
4. **Verify Ruby and Jekyll versions**
5. **Test locally** before pushing

Happy coding! 🎯


