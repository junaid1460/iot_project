import subprocess
import requests


quote = subprocess.check_output(["./out", "database/bg1.jpg", "database/input4.jpg"])
r = requests.post('https://iotserver-crook-1460.c9users.io/post.php', data = {'val':quote})
