from app import db
import datetime
import hashlib

class URL(db.Model):
    """URL

    This class contains the attributes for the URL to be able
    to map the shortened url to it's original one
    """
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), nullable=False)
    shortened_url = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, original_url):
        """__init__
        """
        self.original_url = original_url
        self.shortened_url = self.generate_shortened_url()
    
    def generate_shortened_url(self):
        return hashlib.md5(self.original_url.encode()).hexdigest()[:128]
