from app import g
from models import db, Likes

def add_remove_like(msg_id, likes_list):

    likes = [like.id for like in likes_list]

    if msg_id not in likes:
        like = Likes(user_id=g.user.id, message_id=msg_id)

        db.session.add(like)
    
    else:
        Likes.query.filter(Likes.message_id == msg_id).delete()

    db.session.commit()