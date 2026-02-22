#!/usr/bin/env python3
"""
Script to fix header alignment for specific variations
Convert padding to margin for proper edge alignment
"""

import os
import re

variations_dir = "variations"

# Variations that need fixing (excluding 6, 14, 17, 18 which are already fixed)
variations_to_fix = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 19, 20]

# Dark background variations
dark_bg_variations = [2, 4, 5, 7, 8, 10, 12, 13, 15, 16, 18, 20]

for i in variations_to_fix:
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
    
    # New audit-header style with margin instead of padding
    new_audit_header = f'''        .audit-header {{ 
            border-bottom: 2px solid {border_color}; 
            margin-top: 50px;
            margin-left: 40px;
            margin-right: 40px;
            margin-bottom: 40px; 
            padding-bottom: 10px;
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

print("\n✅ All specified variations updated with proper header alignment!")
