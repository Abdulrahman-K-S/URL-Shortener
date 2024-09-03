from models.url import URL
from app import db

def save_url(original_url):
    new_url = URL(original_url)
    db.session.add(new_url)
    db.session.commit()
    return new_url

def get_original_url(original_url=None, shortened_url=None):
    if original_url:
        return URL.query.filter_by(original_url=original_url).first()
    if shortened_url:
        return URL.query.filter_by(shortened_path=shortened_url).first()
    return None