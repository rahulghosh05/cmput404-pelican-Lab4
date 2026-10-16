from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit, unquote
root=Path('output')
errors=[]
for page in root.glob('*.html'):
 soup=BeautifulSoup(page.read_text(),'html.parser')
 assert len(soup.find_all('html'))==1, page
 for tag,attr in [('a','href'),('link','href')]:
  for node in soup.find_all(tag):
   target=urlsplit(node.get(attr,''))
   if target.scheme or target.netloc: continue
   dest=page.parent/unquote(target.path) if target.path else page
   if not dest.exists(): errors.append(f'{page}: missing {dest}')
   elif target.fragment:
    other=BeautifulSoup(dest.read_text(),'html.parser')
    if not other.find(id=unquote(target.fragment)): errors.append(f'{page}: missing fragment {target.fragment}')
assert not errors, '\n'.join(errors[:30])
assert (root/'.nojekyll').exists()
assert len(list(Path('content').glob('*.*')))==4
print('PASS: four articles, one HTML document per page, all local links and fragments, stylesheets, .nojekyll')
