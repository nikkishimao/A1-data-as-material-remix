#!/usr/bin/env python3
"""
Script to add prev/next navigation to all variation HTML files
"""

import os
import re

# Path to variations folder
variations_dir = "variations"

# Process files 03 through 20 (01 and 02 already done)
for i in range(3, 21):
    filename = f"{i:02d}.html"
    filepath = os.path.join(variations_dir, filename)
    
    if not os.path.exists(filepath):
        print(f"Skipping {filename} - file not found")
        continue
    
    print(f"Processing {filename}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Determine prev and next files
    prev_num = i - 1
    next_num = i + 1 if i < 20 else None
    
    prev_link = f'<a href="{prev_num:02d}.html" class="nav-link"><-- Prev</a>'
    home_link = '<a href="../index.html" class="nav-link">← Return Home</a>'
    next_link = f'<a href="{next_num:02d}.html" class="nav-link">Next --></a>' if next_num else ''
    
    # Add nav styling if not present
    if '.nav-container' not in content:
        # Find the .back-link style and add nav styles after it
        nav_styles = '''
        
        .nav-container { 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            margin-bottom: 20px; 
        }
        
        .nav-link { 
            font-size: 10px; 
            text-decoration: none; 
            color: #888; 
            text-transform: uppercase; 
            letter-spacing: 2px;
        }
        
        .nav-link:hover { 
            color: #000; 
        }'''
        
        # Adjust color for dark backgrounds (variations 2, 4, 6, etc.)
        if i % 2 == 0:
            nav_styles = nav_styles.replace('color: #888;', 'color: #fff;')
            nav_styles = nav_styles.replace('color: #000;', 'color: #888;')
        
        # Insert after .back-link style
        content = re.sub(
            r'(\.back-link\s*{[^}]+})',
            r'\1' + nav_styles,
            content,
            count=1
        )
    
    # Replace the old back link with new nav container
    old_back_link_pattern = r'<a href="\.\./index\.html" class="back-link">← Return Home</a>'
    
    if next_num:
        new_nav = f'''<div class="nav-container">
        {prev_link}
        {home_link}
        {next_link}
    </div>
    '''
    else:
        # For variation 20, no next link
        new_nav = f'''<div class="nav-container">
        {prev_link}
        {home_link}
    </div>
    '''
    
    # Replace the back link
    content = re.sub(old_back_link_pattern, new_nav.strip(), content)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Updated {filename}")

print("\nDone! All variation files have been updated with prev/next navigation.")
