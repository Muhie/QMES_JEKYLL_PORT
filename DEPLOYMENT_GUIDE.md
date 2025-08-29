# GitHub Pages Deployment Guide for QMES Website

This guide will walk you through deploying your converted QMES static website to GitHub Pages.

## Prerequisites

- ✅ GitHub account
- ✅ QMES website repository on GitHub
- ✅ Static site files generated (using the provided scripts)

## Step 1: Prepare Your Repository

### 1.1 Push Your Code to GitHub

```bash
# Initialize git if not already done
git init

# Add all files
git add .

# Commit your changes
git commit -m "Convert Flask app to static site for GitHub Pages"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

### 1.2 Repository Structure

Your repository should look like this:

```
your-repo/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── app/                    # Original Flask app (not deployed)
├── docs/                   # Generated static site (will be deployed)
├── static_site_generator.py
├── generate_pages.py
├── build_static_site.py
├── extract_blog_data.py
├── static_requirements.txt
├── STATIC_SITE_README.md
├── DEPLOYMENT_GUIDE.md
└── README.md
```

## Step 2: Build Your Static Site

### 2.1 Install Dependencies

```bash
pip install -r static_requirements.txt
```

### 2.2 Generate the Static Site

```bash
python build_static_site.py
```

This will create the `docs/` directory with all your static HTML files.

### 2.3 Verify Generated Files

Check that the `docs/` directory contains:

- `index.html` - Homepage
- `about-us.html` - About page
- `our-progress.html` - Blog listing
- `gallery.html` - Image gallery
- `contact.html` - Contact page
- `post-*.html` - Individual blog posts
- `images/` - All images
- `styles/` - CSS files

## Step 3: Configure GitHub Pages

### 3.1 Enable GitHub Pages

1. Go to your GitHub repository
2. Click **Settings** tab
3. Scroll down to **Pages** section (left sidebar)
4. Under **Source**, select **Deploy from a branch**
5. Under **Branch**, select **main** (or your default branch)
6. Under **Folder**, select **/docs**
7. Click **Save**

### 3.2 Wait for Deployment

GitHub will automatically build and deploy your site. This usually takes 1-5 minutes.

### 3.3 Access Your Site

Your site will be available at:
```
https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/
```

## Step 4: Automatic Deployment (Optional)

### 4.1 GitHub Actions Setup

The provided `.github/workflows/deploy.yml` will automatically:

- Build your static site on every push
- Deploy to GitHub Pages automatically
- Use the `gh-pages` branch for deployment

### 4.2 Manual vs Automatic

- **Manual**: Push `docs/` folder to main branch
- **Automatic**: Push any changes, GitHub Actions builds and deploys

## Step 5: Customize Your Content

### 5.1 Update Blog Posts

Edit `static_site_generator.py`:

```python
BLOG_POSTS = [
    {
        "id": 1,
        "title": "Your Actual Title",
        "subtitle": "Your Actual Subtitle",
        "author": "Real Author Name",
        "date_posted": "2024-01-15",
        "content": """
        <p>Your actual blog content here.</p>
        <p>Use HTML for formatting.</p>
        """
    }
]
```

### 5.2 Update Social Media Links

Edit all HTML templates to include your actual social media accounts:

```html
<a href="https://twitter.com/QMES_Official" target="_blank">Twitter</a>
<a href="https://www.instagram.com/qmes_official" target="_blank">Instagram</a>
```

### 5.3 Update Contact Information

Edit `generate_pages.py` to include your actual contact details:

```python
# In generate_contact() function
"<li><strong>Email:</strong> your-actual-email@qmul.ac.uk</li>"
```

## Step 6: Rebuild and Deploy

### 6.1 After Making Changes

```bash
# Rebuild the static site
python build_static_site.py

# Commit and push changes
git add .
git commit -m "Update website content"
git push origin main
```

### 6.2 With GitHub Actions

If using automatic deployment, just push your changes:

```bash
git add .
git commit -m "Update website content"
git push origin main
```

GitHub Actions will automatically rebuild and deploy.

## Step 7: Verify Deployment

### 7.1 Check GitHub Pages Status

1. Go to repository **Settings** → **Pages**
2. Look for green checkmark indicating successful deployment
3. Note the deployment time

### 7.2 Test Your Site

1. Visit your deployed URL
2. Test all navigation links
3. Verify images load correctly
4. Check responsive design on mobile
5. Test blog post links

## Troubleshooting

### Common Issues

#### 1. Site Not Loading

- Check GitHub Pages is enabled
- Verify `/docs` folder is selected
- Wait 5-10 minutes for deployment
- Check repository settings

#### 2. Missing Images

- Ensure all images exist in `app/static/images/`
- Check file paths in HTML templates
- Verify image file permissions

#### 3. Styling Issues

- Check `app/static/styles/Styles.css` exists
- Verify CSS file paths in HTML
- Check for CSS syntax errors

#### 4. Build Errors

- Install required dependencies: `pip install -r static_requirements.txt`
- Check Python version (3.6+ required)
- Verify all required files exist

#### 5. GitHub Actions Failures

- Check Actions tab for error details
- Verify workflow file syntax
- Check repository permissions

### Debugging Steps

1. **Check GitHub Pages logs** in repository Settings
2. **Verify file structure** in `docs/` folder
3. **Test locally** by opening HTML files in browser
4. **Check browser console** for JavaScript errors
5. **Validate HTML** using online validators

## Maintenance

### Regular Updates

1. **Content Updates**: Edit source files and rebuild
2. **Image Updates**: Replace files in `app/static/images/`
3. **Style Updates**: Modify `app/static/styles/Styles.css`
4. **Blog Posts**: Add to `BLOG_POSTS` list

### Backup

- Keep your original Flask app files
- Version control all changes
- Regular backups of generated `docs/` folder

## Advanced Configuration

### Custom Domain

1. Add custom domain in repository Settings → Pages
2. Configure DNS records
3. Add `CNAME` file to `docs/` folder

### SEO Optimization

- Add meta descriptions to HTML templates
- Include Open Graph tags
- Optimize image alt text
- Add structured data markup

### Analytics

- Add Google Analytics tracking code
- Include in HTML templates
- Monitor site performance

## Support Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Static Site Generators](https://www.staticgen.com/)
- [HTML/CSS Validation](https://validator.w3.org/)

## Next Steps

After successful deployment:

1. ✅ **Test all functionality**
2. ✅ **Update content with real information**
3. ✅ **Configure custom domain (optional)**
4. ✅ **Set up analytics (optional)**
5. ✅ **Share your new static website!**

Your QMES website is now successfully converted to a static site and deployed on GitHub Pages! 🎉


