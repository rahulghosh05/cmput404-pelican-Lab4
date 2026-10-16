import os
from pelicanconf import *
# Set this to the Classroom Pages URL before deploying, or export SITEURL.
SITEURL = os.environ.get('SITEURL', '')
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True
if not SITEURL:
    raise ValueError('Set SITEURL to https://OWNER.github.io/REPOSITORY before publishing')
