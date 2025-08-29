# QMES Static Website Generator

This project converts the Flask-based QMES website to a static site that can be deployed on GitHub Pages. All admin functionality has been removed while maintaining the blog features.

## Features

- ✅ **Static HTML generation** - No server-side processing required
- ✅ **Blog functionality maintained** - All blog posts are preserved
- ✅ **Responsive design** - Bootstrap-based responsive layout
- ✅ **GitHub Pages ready** - Optimized for static hosting
- ❌ **Admin features removed** - No login, user management, or post editing
- ❌ **Database dependency removed** - All data is embedded in static files

## Quick Start

### 1. Install Dependencies

```bash
pip install -r static_requirements.txt
```

### 2. Build the Static Site

```bash
python build_static_site.py
```

This will generate all static HTML files in the `docs/` directory.

### 3. Customize Content

Edit the following files to customize your content:

- **Blog Posts**: Modify `BLOG_POSTS` in `static_site_generator.py`
- **Page Content**: Edit the HTML templates in `generate_pages.py`
- **Images**: Replace images in `app/static/images/` (they'll be copied automatically)

### 4. Deploy to GitHub Pages

1. Push the `docs/` directory to your GitHub repository
2. Go to repository Settings → Pages
3. Set Source to "Deploy from a branch"
4. Select the branch containing your `docs/` folder
5. Set folder to `/docs`
6. Click Save

## File Structure

```
├── static_site_generator.py    # Main generator for index and blog posts
├── generate_pages.py           # Generator for additional pages
├── build_static_site.py        # Main build script
├── static_requirements.txt     # Python dependencies
├── docs/                       # Generated static site (output)
│   ├── index.html             # Homepage
│   ├── about-us.html          # About/Membership page
│   ├── our-progress.html      # Blog listing page
│   ├── gallery.html           # Image gallery
│   ├── contact.html           # Contact information
│   ├── post-1.html            # Individual blog posts
│   ├── post-2.html
│   ├── images/                # Copied from app/static/images
│   └── styles/                # Copied from app/static/styles
└── app/                        # Original Flask app (not deployed)
```

## Customizing Blog Posts

To add or modify blog posts, edit the `BLOG_POSTS` list in `static_site_generator.py`:

```python
BLOG_POSTS = [
    {
        "id": 1,
        "title": "Your Post Title",
        "subtitle": "Your Post Subtitle",
        "author": "Author Name",
        "date_posted": "2024-01-15",
        "content": """
        <p>Your HTML content here.</p>
        <p>You can use HTML tags for formatting.</p>
        """
    },
    # Add more posts...
]
```

## Customizing Pages

To modify page content, edit the HTML templates in `generate_pages.py`. Each page has its own generation function:

- `generate_about_us()` - About/Membership page
- `generate_our_progress()` - Blog listing page
- `generate_gallery()` - Image gallery
- `generate_contact()` - Contact information

## Adding New Pages

To add a new page:

1. Create a new generation function in `generate_pages.py`
2. Add the page to the navigation in all templates
3. Call the function in the `main()` function
4. Rebuild the site

## Styling

The site uses:
- **Bootstrap 4.1.3** for responsive layout
- **Custom CSS** from `app/static/styles/Styles.css`
- **Google Fonts** (Nunito) for typography

## Social Media Links

Update the social media links in all HTML templates to point to your actual accounts:

```html
<a href="https://twitter.com/YOUR_HANDLE" target="_blank">Twitter</a>
<a href="https://www.instagram.com/YOUR_HANDLE" target="_blank">Instagram</a>
<!-- etc. -->
```

## Rebuilding the Site

After making changes to content or templates:

```bash
python build_static_site.py
```

This will regenerate all HTML files with your updates.

## Troubleshooting

### Common Issues

1. **Missing images**: Ensure all referenced images exist in `app/static/images/`
2. **Styling issues**: Check that `app/static/styles/Styles.css` exists
3. **Template errors**: Verify Jinja2 syntax in templates

### Dependencies

- Python 3.6+
- Jinja2 template engine
- Access to original Flask app files

## Migration from Flask

This static generator preserves:
- ✅ All visual design and layout
- ✅ Blog post content and structure
- ✅ Image gallery functionality
- ✅ Responsive navigation
- ✅ Footer and social links

Removed features:
- ❌ User authentication and login
- ❌ Admin panel and post management
- ❌ Database operations
- ❌ Form processing
- ❌ Session management

## Support

For issues or questions about the static site generator, please check:
1. All required files are present
2. Python dependencies are installed
3. Original Flask app files are accessible
4. File permissions allow reading/writing

## License

This static site generator is part of the QMES website project.


