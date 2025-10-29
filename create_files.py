import os
from pathlib import Path

# File contents
files = {
    'README.md': open('README.md').read() if os.path.exists('README.md') else '',
    '.gitignore': open('.gitignore').read() if os.path.exists('.gitignore') else '',
    # Add other files
}

for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created: {path}')
