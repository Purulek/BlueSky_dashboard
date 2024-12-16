from atproto import Client, client_utils
import pandas as pd
import numpy as np



login = 'XXX'
password = ''


def main(log, passw):
    client = Client()
    profile = client.login(log, passw)
    print('Welcome,', profile.display_name)

    text = client_utils.TextBuilder().text('Hello World from ').link('Python SDK', 'https://atproto.blue')
    post = client.send_post(text)
    client.like(post.uri, post.cid)




main(login, password)