import webbrowser
import os

# Convert to HTML first
os.system('jupyter nbconvert --to html banknote_authentication.ipynb')

# Open in default browser for PDF conversion
webbrowser.open('banknote_authentication.html')
