#!/usr/bin/env python3
"""
Extract blog data from existing Flask database
This script helps migrate existing blog posts to the static site
"""

import os
import sys
import json
from datetime import datetime

def extract_from_database():
    """Extract blog posts from existing database"""
    print("🔍 Attempting to extract blog data from existing database...")
    
    try:
        # Try to import Flask and database models
        sys.path.append('app')
        from models import db, Blogpost
        from config import Config
        
        # Create Flask app context
        from flask import Flask
        app = Flask(__name__)
        app.config.from_object(Config)
        db.init_app(app)
        
        with app.app_context():
            # Query all blog posts
            posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
            
            if posts:
                print(f"✅ Found {len(posts)} blog posts!")
                
                # Convert to static format
                static_posts = []
                for post in posts:
                    static_post = {
                        "id": post.id,
                        "title": post.title,
                        "subtitle": post.subtitle,
                        "author": post.author,
                        "date_posted": post.date_posted.strftime('%Y-%m-%d'),
                        "content": post.content
                    }
                    static_posts.append(static_post)
                
                # Save to JSON file
                with open('extracted_blog_posts.json', 'w', encoding='utf-8') as f:
                    json.dump(static_posts, f, indent=2, ensure_ascii=False)
                
                print("💾 Blog posts saved to 'extracted_blog_posts.json'")
                print("\n📝 To use these posts in your static site:")
                print("1. Copy the content from extracted_blog_posts.json")
                print("2. Paste it into the BLOG_POSTS list in static_site_generator.py")
                print("3. Rebuild your static site")
                
                return static_posts
            else:
                print("ℹ️  No blog posts found in database")
                return []
                
    except ImportError as e:
        print(f"⚠️  Could not import database models: {e}")
        print("ℹ️  This is normal if you don't have the database set up")
        return []
    except Exception as e:
        print(f"❌ Error extracting data: {e}")
        return []

def create_sample_data():
    """Create sample blog data if no database exists"""
    print("📝 Creating sample blog data...")
    
    sample_posts = [
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
            <p>The team worked hard to build and program our robot, and we learned so much in the process.</p>
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
    
    # Save sample data
    with open('sample_blog_posts.json', 'w', encoding='utf-8') as f:
        json.dump(sample_posts, f, indent=2, ensure_ascii=False)
    
    print("💾 Sample blog posts saved to 'sample_blog_posts.json'")
    print("\n📝 To use these posts in your static site:")
    print("1. Copy the content from sample_blog_posts.json")
    print("2. Paste it into the BLOG_POSTS list in static_site_generator.py")
    print("3. Rebuild your static site")
    
    return sample_posts

def main():
    """Main function"""
    print("🔍 QMES Blog Data Extractor")
    print("=" * 40)
    
    # Try to extract from database first
    posts = extract_from_database()
    
    if not posts:
        print("\n📝 No database data found, creating sample data instead...")
        posts = create_sample_data()
    
    print(f"\n✅ Ready to build static site with {len(posts)} blog posts!")
    print("\n🚀 Next steps:")
    print("1. Review the generated JSON file")
    print("2. Update the BLOG_POSTS in static_site_generator.py")
    print("3. Run: python build_static_site.py")

if __name__ == "__main__":
    main()


