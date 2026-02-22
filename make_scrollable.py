import os
import re

# Directory containing the variation files
variations_dir = "variations"

# Process all HTML files
for i in range(1, 21):
    filename = f"{i:02d}.html"
    filepath = os.path.join(variations_dir, filename)
    
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Replace overflow: hidden with overflow: auto (or overflow-y: auto for vertical only)
        # Also remove height: 100vh constraint to allow content to expand
        content = re.sub(
            r'(body\s*{[^}]*?)overflow:\s*hidden;',
            r'\1overflow-y: auto;',
            content
        )
        
        # Optionally remove height: 100vh to allow natural content height
        content = re.sub(
            r'(body\s*{[^}]*?)height:\s*100vh;',
            r'\1min-height: 100vh;',
            content
        )
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        print(f"✓ Updated {filename}")
    else:
        print(f"✗ File not found: {filename}")

print("\nAll variation pages are now vertically scrollable!")
