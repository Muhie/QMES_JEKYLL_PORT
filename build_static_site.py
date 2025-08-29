#!/usr/bin/env python3
"""
Main script to build the complete static QMES website
"""

import os
import sys

def main():
    """Build the complete static website"""
    print("🚀 Building QMES Static Website for GitHub Pages")
    print("=" * 50)
    
    # Check if required files exist
    if not os.path.exists("static_site_generator.py"):
        print("❌ Error: static_site_generator.py not found!")
        sys.exit(1)
    
    if not os.path.exists("generate_pages.py"):
        print("❌ Error: generate_pages.py not found!")
        sys.exit(1)
    
    # Import and run the generators
    try:
        print("📝 Step 1: Running main static site generator...")
        import static_site_generator
        static_site_generator.main()
        
        print("\n📄 Step 2: Generating additional pages...")
        import generate_pages
        generate_pages.main()
        
        print("\n✅ Static website build complete!")
        print("\n📁 Files generated in the 'docs' directory:")
        
        # List generated files
        if os.path.exists("docs"):
            for root, dirs, files in os.walk("docs"):
                level = root.replace("docs", "").count(os.sep)
                indent = " " * 2 * level
                print(f"{indent}{os.path.basename(root)}/")
                subindent = " " * 2 * (level + 1)
                for file in files:
                    print(f"{subindent}{file}")
        
        print("\n🚀 Next steps:")
        print("1. Review the generated files in the 'docs' directory")
        print("2. Customize the blog posts in static_site_generator.py")
        print("3. Update social media links in the templates")
        print("4. Push the 'docs' directory to GitHub")
        print("5. Enable GitHub Pages in your repository settings")
        print("6. Set the source to 'docs' folder")
        
    except Exception as e:
        print(f"❌ Error during build: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
