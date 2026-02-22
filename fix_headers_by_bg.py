#!/usr/bin/env python3
"""
Script to fix header styles based on ACTUAL background color, not just even/odd
"""

import os
import re

variations_dir = "variations"

# Manually define which variations have dark backgrounds
dark_bg_variations = [2, 4, 5, 7, 8, 10, 12, 13, 15, 16, 18, 20]  # Based on actual content

for i in range(1, 21):
    filename = f"{i:02d}.html"
    filepath = os.path.join(variations_dir, filename)
    
    if not os.path.exists(filepath):
        print(f"Skipping {filename} - file not found")
        continue
    
    print(f"Processing {filename}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Determine if dark or light background
    is_dark_bg = i in dark_bg_variations
    border_color = '#fff' if is_dark_bg else '#000'
    text_color = '#fff' if is_dark_bg else '#000'
    
    print(f"  Background: {'dark' if is_dark_bg else 'light'}, Colors: {text_color}")
    
    # Standardized audit-header style
    audit_header_style = f'''
        .audit-header {{ 
            border-bottom: 2px solid {border_color}; 
            margin-top: 50px;
            margin-bottom: 40px; 
            padding-bottom: 10px;
            padding-left: 40px;
            padding-right: 40px;
        }}
        
        .audit-header h2 {{ 
            color: {text_color}; 
            margin: 0; 
            letter-spacing: 4px;
            font-size: 20px;
        }}'''
    
    # Standardized metric-id style
    metric_id_style = f'''

        .metric-id {{ 
            float: right; 
            font-weight: bold; 
            border: 1px solid {border_color}; 
            padding: 5px; 
            font-size: 10px;
            color: {text_color};
        }}'''
    
    # Remove old .audit-header style (including multiline)
    content = re.sub(
        r'\.audit-header\s*\{[^}]*\}',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove old .audit-header h2 style
    content = re.sub(
        r'\.audit-header\s+h2\s*\{[^}]*\}',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove old .metric-id style
    content = re.sub(
        r'\.metric-id\s*\{[^}]*\}',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Insert new styles after .nav-separator
    content = re.sub(
        r'(\.nav-separator\s*\{[^}]*\})',
        r'\1' + audit_header_style + metric_id_style,
        content,
        count=1
    )
    
    # Remove inline styles from h2 tags in audit-header
    content = re.sub(
        r'<h2\s+style="[^"]*">',
        '<h2>',
        content
    )
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Updated {filename}")

print("\n✅ All variations updated with correct header colors!")
