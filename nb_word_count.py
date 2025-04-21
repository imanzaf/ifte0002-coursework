import json

# Load the notebook
with open('coursework/GRP_F_CW2.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Extract text from markdown cells
markdown_text = " ".join(
    cell['source'] if isinstance(cell['source'], str) else ''.join(cell['source'])
    for cell in notebook['cells'] if cell['cell_type'] == 'markdown'
)

# Count words
word_count = len(markdown_text.split())
print(f"Total word count (Markdown cells only): {word_count}")
