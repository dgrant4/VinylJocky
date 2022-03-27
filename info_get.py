import discogs_client


def get_label(release_id):
    user_token = ('OLvgzIrrgDuxlZmsUrfNZIEFOjngxXcXMmgZSZuz')
    d= discogs_client.Client('my_user_agent/1.0',user_token = user_token)
    release = d.release(release_id)
    return release
