import os

name  = os.environ.get('NEW_NAME', '').encode('utf-8')
email = os.environ.get('NEW_EMAIL', '').encode('utf-8')

commit.author_name = name
commit.author_email = email
commit.committer_name = name
commit.committer_email = email
