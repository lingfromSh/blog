from . import models, schemas


def get_user(user_id: int):
    return models.User.filter(models.User.id == user_id).first()


def get_user_by_email(email: str):
    return models.User.filter(models.User.email == email).first()


def get_user_by_username(username: str):
    return models.User.filter(models.User.username == username).first()


def get_users(skip: int = 0, limit: int = 100):
    return list(models.User.select().offset(skip).limit(limit))


def create_user(user: schemas.UserCreate):
    fake_hashed_password = user.password + "not_really_hashed_password"
    fake_random_token = "fake_random_token"
    db_user = models.User(username=user.username, hashed_password=fake_hashed_password, token=fake_random_token)
    db_user.save()
    return db_user


def update_user(user: schemas.UserUpdate):
    db_user = get_user(user.id)
    if db_user:
        if user.password is not None:
            fake_hashed_password = user.password + "not_really_hashed_password"
            db_user.hashed_password = fake_hashed_password
        if user.email is not None:
            db_user.email = user.email
        db_user.save()
        return db_user
    return None


def get_tag(tag_id: int):
    return models.Tag.filter(models.Tag.id == tag_id).first()


def get_tags_of_user(user_id: int, skip: int = 0, limit: int = 100):
    return list(models.Tag.filter(models.Tag.author_id == user_id).offset(skip).limit(limit))


def create_tag(tag: schemas.TagCreate):
    db_tag = models.Tag(title=tag.title, author_id=tag.author_id)
    db_tag.save()
    return db_tag


def get_catalog(catalog_id: int):
    return models.Catalog.filter(models.Catalog.id == catalog_id).first()


def get_catalogs_of_user(user_id: int, skip: int = 0, limit: int = 100):
    return list(models.Catalog.filter(models.Catalog.author_id == user_id).offset(skip).limit(limit))


def create_catalog(catalog: schemas.CatalogCreate):
    db_catalog = models.Catalog(title=catalog.title, author_id=catalog.author_id)
    db_catalog.save()
    return db_catalog


def get_post(post_id: int):
    return models.Post.filter(models.Post.id == post_id).first()


def get_posts_of_user(user_id: int, skip: int = 0, limit: int = 100):
    return list(models.Post.filter(models.Post.author_id == user_id).offset(skip).limit(limit))


def create_post(post: schemas.PostCreate):
    db_post = models.Post(**post.dict())
    db_post.save()
    return db_post


def update_post(post: schemas.PostUpdate):
    db_post = get_post(post.id)
    if db_post:
        db_post.title = post.title
        db_post.slug = post.slug
        db_post.summary = post.summary
        db_post.content = post.content
        db_post.status = post.status
        db_post.can_comment = post.can_comment
        db_post.save()
        return db_post
    return db_post
