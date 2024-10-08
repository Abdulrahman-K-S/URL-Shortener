from app import db
from ..service import save_url, get_original_url
from flask import url_for, redirect

def create_short_url(original_url):
    if not original_url:
        raise ValueError("original_url is required")

    existing_url = get_original_url(original_url)
    if existing_url:
        return url_for('create', shortened_url=existing_url.shortened_url, _external=True)
    
    new_url = save_url(original_url)
    return url_for('create', shortened_url=new_url.shortened_url, _external=True)

def redirect_to_original(shortened_url):
    url = get_original_url(shortened_url=shortened_url)
    if url:
        return redirect(url.original_url)
    return 'URL not found', 404
