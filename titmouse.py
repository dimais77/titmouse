"""Module providing a import app and flask shell."""
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post


 """Function make shell context."""
 @app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}
