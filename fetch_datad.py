from atproto import Client, client_utils
import pandas as pd
import numpy as np



login = 'XXX'
password = 'XXX'
post_topic =[]
textx = []


def main(log, passw,textx):
    client = Client()
    profile = client.login(log, passw)
    print('Welcome,', profile.display_name)
    text = client_utils.TextBuilder().text(textx).link('Python SDK', 'https://atproto.blue')
    post = client.send_post(text)
    client.like(post.uri, post.cid)


def get_posts(log,passw,theme,text):
    client = Client()
    search = theme
    profile = client.login(log, passw)
    post = client.send_post(text)
    client.like(post.uri, post.cid)
    pass

def create_fiel(log,password):
    pass






main(login, password,textx)
get_posts(login,password,post_topic)