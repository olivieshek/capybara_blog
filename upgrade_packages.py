import re
from subprocess import call

with open("requirements.txt", mode='r') as file:
    content = file.readlines()

packages = list()
for i, dist in enumerate(content):
    packages.append(re.match(r'\w+', dist).group())

call('pip3 install --upgrade' + ' ' + ' '.join(packages), shell=True)


