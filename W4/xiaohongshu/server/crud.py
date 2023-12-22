from sqlalchemy.orm import Session
from . import models, schemas

def create_article(db: Session, article: schemas.ArticleCreate):
    db_article = models.Article(item=article.item, article=article.article)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article