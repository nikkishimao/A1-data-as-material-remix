#!/usr/bin/env python3
"""
Apply the header style from units 6, 14, 17, 18 to all other units
"""

import os
import re

variations_dir = "variations"

# Dark background variations
dark_bg_variations = [2, 4, 5, 7, 8, 10, 12, 13, 15, 16, 18, 20]

# Variation 17 needs absolute positioning due to centered flexbox
absolute_position_variations = [17]

for i in range(1, 21):
    filename = f"{i:02d}.html"
    filepath = os.path.join(variations_dir, filename)
    
    if not os.path.exists(filepath):
        print(f"Skipping {filename} - file not found")
        continue
    
    print(f"Processing {filename}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Determine colors
    is_dark_bg = i in dark_bg_variations
    border_color = '#fff' if is_dark_bg else '#000'
    text_color = '#fff' if is_dark_bg else '#000'
    
    # Choose header style based on variation
    if i in absolute_position_variations:
        # Absolute positioning for centered layouts
        new_audit_header = f'''        .audit-header {{ 
            border-bottom: 2px solid {border_color}; 
            position: absolute;
            top: 100px;
            left: 40px;
            right: 40px;
            margin: 0;
            padding-bottom: 10px;
        }}'''
    else:
        # Standard margin-based positioning
        new_audit_header = f'''        .audit-header {{ 
            border-bottom: 2px solid {border_color}; 
            margin-top: 100px;
            margin-left: 40px;
            margin-right: 40px;
            margin-bottom: 40px; 
            padding-bottom: 10px;
            padding-left: 0;
            padding-right: 0;
        }}'''
    
    # Replace the audit-header style
    content = re.sub(
        r'\.audit-header\s*\{[^}]*\}',
        new_audit_header,
        content,
        flags=re.DOTALL,
        count=1
    )
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Updated {filename}")

print("\n✅ All variations now match the header style of units 6, 14, 17, 18!")
