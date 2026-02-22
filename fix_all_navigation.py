#!/usr/bin/env python3
"""
Script to fix navigation on all variation pages:
- Return Home in upper left
- Prev | Next in upper right with proper arrows
- Consistent positioning across all pages
"""

import os
import re

variations_dir = "variations"

for i in range(1, 21):
    filename = f"{i:02d}.html"
    filepath = os.path.join(variations_dir, filename)
    
    if not os.path.exists(filepath):
        print(f"Skipping {filename} - file not found")
        continue
    
    print(f"Processing {filename}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Determine background color for nav link colors
    is_dark_bg = (i % 2 == 0)  # Even numbered variations have dark backgrounds
    nav_color = '#fff' if is_dark_bg else '#888'
    nav_hover = '#888' if is_dark_bg else '#000'
    
    # Update .back-link style to ensure it's positioned correctly
    back_link_style = f'''        .back-link {{ 
            font-size: 10px; 
            text-decoration: none; 
            color: {nav_color}; 
            text-transform: uppercase; 
            letter-spacing: 2px;
            position: absolute;
            top: 40px;
            left: 40px;
            z-index: 100;
        }}'''
    
    # Replace existing .back-link style
    content = re.sub(
        r'\.back-link\s*\{[^}]+\}',
        back_link_style,
        content,
        count=1
    )
    
    # Update or add .nav-container style
    nav_container_style = f'''
        
        .nav-container {{ 
            position: absolute;
            top: 40px;
            right: 40px;
            display: flex; 
            gap: 10px;
            align-items: center; 
            z-index: 100;
        }}
        
        .nav-link {{ 
            font-size: 10px; 
            text-decoration: none; 
            color: {nav_color}; 
            text-transform: uppercase; 
            letter-spacing: 2px;
        }}
        
        .nav-link:hover {{ 
            color: {nav_hover}; 
        }}
        
        .nav-separator {{
            color: {nav_color};
            font-size: 10px;
        }}'''
    
    # Remove old nav styles if they exist
    content = re.sub(r'\.nav-container\s*\{[^}]+\}', '', content)
    content = re.sub(r'\.nav-link\s*\{[^}]+\}', '', content)
    content = re.sub(r'\.nav-link:hover\s*\{[^}]+\}', '', content)
    content = re.sub(r'\.nav-separator\s*\{[^}]+\}', '', content)
    
    # Insert new nav styles after .back-link
    content = re.sub(
        r'(\.back-link\s*\{[^}]+\})',
        r'\1' + nav_container_style,
        content,
        count=1
    )
    
    # Build navigation HTML
    prev_num = i - 1
    next_num = i + 1 if i < 20 else None
    
    back_link = '<a href="../index.html" class="back-link">← Return Home</a>'
    
    if i == 1:
        # First variation: no prev
        nav_html = f'''    <a href="../index.html" class="back-link">← Return Home</a>
    
    <div class="nav-container">
        <a href="02.html" class="nav-link">Next →</a>
    </div>'''
    elif i == 20:
        # Last variation: no next
        nav_html = f'''    <a href="../index.html" class="back-link">← Return Home</a>
    
    <div class="nav-container">
        <a href="19.html" class="nav-link">← Prev</a>
    </div>'''
    else:
        # Middle variations: both prev and next
        nav_html = f'''    <a href="../index.html" class="back-link">← Return Home</a>
    
    <div class="nav-container">
        <a href="{prev_num:02d}.html" class="nav-link">← Prev</a>
        <span class="nav-separator">|</span>
        <a href="{next_num:02d}.html" class="nav-link">Next →</a>
    </div>'''
    
    # Remove old navigation
    # Pattern 1: Old nav-container with all three links
    content = re.sub(
        r'<div class="nav-container">.*?</div>\s*\n\s*',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Pattern 2: Old back-link standalone
    content = re.sub(
        r'<a href="\.\./index\.html" class="back-link">.*?</a>\s*\n\s*',
        '',
        content
    )
    
    # Insert new navigation right after <body>
    content = re.sub(
        r'(<body>)\s*',
        r'\1\n' + nav_html + '\n    \n',
        content,
        count=1
    )
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Updated {filename}")

print("\n✅ All variations updated with consistent navigation!")
