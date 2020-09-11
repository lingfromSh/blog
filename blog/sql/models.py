from sql.database import Model
import peewee


class User(Model):
    username = peewee.CharField(max_length=32, unique=True, null=False)
    hashed_password = peewee.CharField(max_length=255, null=False)
    nickname = peewee.CharField(max_length=255, null=True)
    email = peewee.CharField(max_length=255, null=True)
    token = peewee.CharField(max_length=255, null=True)

class Tag(Model):
    title = peewee.CharField(max_length=64, null=False)
    author = peewee.ForeignKeyField(User, backref="created_tags", on_delete="CASCADE")


class Catalog(Model):
    title = peewee.CharField(max_length=64, null=False)
    author = peewee.ForeignKeyField(User, backref="created_catalogs", on_delete="CASCADE")


class Post(Model):
    STATUS_CHOICES = (
        STATUS_PUBLISHED,
        STATUS_DRAFT
    ) = range(2)

    title = peewee.CharField(max_length=32, null=False)
    content = peewee.TextField()
    slug = peewee.CharField(max_length=32)
    summary = peewee.CharField(max_length=255)
    liked = peewee.IntegerField(default=0)
    status = peewee.IntegerField(default=STATUS_DRAFT, choices=STATUS_CHOICES)
    can_comment = peewee.BooleanField(default=True)
    author = peewee.ForeignKeyField(User, backref="created_posts", on_delete="CASCADE")


class PostTag(Model):
    post = peewee.ForeignKeyField(Post, on_delete="CASCADE")
    tag = peewee.ForeignKeyField(Tag, on_delete="CASCADE")
    sort_order = peewee.IntegerField(default=1)


class PostCatalog(Model):
    post = peewee.ForeignKeyField(Post, on_delete="CASCADE")
    catalog = peewee.ForeignKeyField(Catalog, on_delete="CASCADE")


class Comment(Model):
    content = peewee.TextField()
    author = peewee.ForeignKeyField(User, on_delete="CASCADE", backref="comments")
    post = peewee.ForeignKeyField(Post, on_delete="CASCADE", backref="comments")


class CommentTree(Model):
    parent_comment = peewee.ForeignKeyField(Comment, on_delete="SET_NULL")
    child_comment = peewee.ForeignKeyField(Comment, on_delete="CASCADE")
