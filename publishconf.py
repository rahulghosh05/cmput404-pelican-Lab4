import os
from pelicanconf import *
# GitHub Pages project URL; override with SITEURL for another deployment.
SITEURL = os.environ.get('SITEURL', 'https://rahulghosh05.github.io/cmput404-pelican-Lab4')
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True
if not SITEURL:
    raise ValueError('Set SITEURL to https://OWNER.github.io/REPOSITORY before publishing')
