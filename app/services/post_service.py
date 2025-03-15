from ..repositories import create_post, get_posts_by_user, delete_post
from ..models import Post

class PostService:
    def __init__(self, db):
        self.db = db

    def create_post(self, post_data, user_id: int):
        post = Post(text=post_data.text, owner_id=user_id)
        return create_post(self.db, post)

    def get_posts(self, user_id: int):
        return get_posts_by_user(self.db, user_id)

    def delete_post(self, post_id: int):
        return delete_post(self.db, post_id)