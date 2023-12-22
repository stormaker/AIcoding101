from pydantic import BaseModel


class ArticleCreate(BaseModel):
	item: str
	article: str


class Article(BaseModel):
	id: int
	item: str
	article: str


class Config:
	orm_mode = True
