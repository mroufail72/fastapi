
import os
from fastapi import FastAPI, Request, Response
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)


# # origins = ["https://www.google.com", "https://www.youtube.com"]
# origins = ["*"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app = FastAPI(
#     openapi_url="/openapi.json",
#     docs_url="/docs",
#     redoc_url="/redoc",
# )

# This section is required to fix the Authorize process in production


middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)


@app.middleware("http")
async def cors_handler(request: Request, call_next):
    response: Response = await call_next(request)
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    # Instead of: 'Access-Control-Allow-Origin' = os.environ.get('allowedOrigins'):
    response.headers['Access-Control-Allow-Origin'] = "https://fastapi-production-75e6.up.railway.app, http://127.0.0.1:8000"
    response.headers['Access-Control-Allow-Methods'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response


@app.middleware("http")
async def TestCustomMiddleware(request: Request, call_next):
    print("Middleware works!")
    response = await call_next(request)
    return response


# @app.middleware("http")
# async def add_cors_headers(request, call_next):
#     response = await call_next(request)
#     response.headers["Access-Control-Allow-Origin"] = "https://fastapi-production-75e6.up.railway.app, http://127.0.0.1:8000"
#     response.headers["Access-Control-Allow-Credentials"] = "true"
#     response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
#     response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
#     return response

origins = [
    "https://fastapi-production-75e6.up.railway.app",
    "http://127.0.0.1:8000",
]

# app.add_middleware(CORSMiddleware,
#                    allow_origins=origins,
#                    allow_credentials=True,
#                    allow_methods=["*"],
#                    allow_headers=["*"],

#                    )

# middleware = [
#     Middleware(
#         CORSMiddleware,
#         allow_origins=['*'],
#         allow_credentials=True,
#         allow_methods=['*'],
#         allow_headers=['*']
#     )
# ]


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


# path or route operation - decorator and function
'''get path could be /login or /posts/vote - single slash just indicates root page'''
# Request usually comes in with a GET method and depending on URL returns code


@app.get("/")
def read_root():
    return {"message": "welcome to my api!!!!"}


# Legacy code prior to routing endpoints via separate files


# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {"data": posts}


# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
#             {"title": "favorite foods", "content": "I like pizza", "id": 2}]


# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p


# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i


# @app.get("/posts", response_model=List[schemas.Post])
# def get_posts(db: Session = Depends(get_db)):
#     # cursor.execute("""SELECT * FROM posts""")
#     # posts = cursor.fetchall()
#     posts = db.query(models.Post).all()
#     # print(posts)
#     return posts
#     # return {"data": posts}
#     # return {"data": my_posts}
#     # return {"data": "This is your posts"}


# @ app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# # def create_posts(payLoad: dict = Body(...)):
# def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
#     # cursor.execute("""INSERT INTO posts (title, content, published, rating)
#     #                     VALUES (%s, %s, %s, %s) RETURNING * """,
#     #                (post.title, post.content, post.published, post.rating))
#     # new_post = cursor.fetchone()
#     # conn.commit()
#     # print(post.dict()) ** unpacks the dictionary - cool!
#     new_post = models.Post(**post.dict())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)

#     return new_post
#     # return {"data": new_post}
#     # print(payLoad)
#     # print(post)
#     # print(post.rating)
#     # print(post.dict())
#     # post_dict = post.dict()
#     # post_dict['id'] = randrange(0, 1000000000)
#     # my_posts.append(post_dict)
#     # return {"data": "created post"}
#     # return {"data": post}
#     # return {"post": f"title: {payLoad['title']} content: {payLoad['content']}"}


# # @app.get("/posts/latest")
# # def get_latest_post():
# #     post = my_posts[len(my_posts)-1]
# #     return {"detail": post}


# # add path parameter


# @ app.get("/posts/{id}", response_model=schemas.Post)
# def get_post(id: int, db: Session = Depends(get_db)):
#     post = db.query(models.Post).filter(models.Post.id == id).first()
#     # print(post)
#     # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
#     # post = cursor.fetchone()
#     # print(id)
#     # print(type(id))
#     # post = find_post(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id {id} was not found")

#     return post
#     # return {"post_detail": post}
#     # return {"post_detail": f"Here is post {id}"}


# @ app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db: Session = Depends(get_db)):
#     post = db.query(models.Post).filter(models.Post.id == id)
#     # cursor.execute(
#     #     """DELETE FROM posts WHERE id = %s RETURNING * """, (str(id)))
#     # deleted_post = cursor.fetchone()
#     # conn.commit()
#     if post.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} does not exist")

#     post.delete(synchronize_session=False)
#     db.commit()

#     return Response(status_code=status.HTTP_204_NO_CONTENT)
#     # find the index in the array that has the required id
#     # my_posts.pop(index)
#     # index = find_index_post(id)
#     # if index == None:
#     #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#     #                         detail=f"post with id: {id} does not exist")
#     # my_posts.pop(index)
#     # return Response(status_code=status.HTTP_204_NO_CONTENT)


# @ app.put("/posts/{id}", response_model=schemas.Post)
# def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
#     post_query = db.query(models.Post).filter(models.Post.id == id)
#     # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s, rating = %s WHERE id = %s RETURNING * """,
#     #                (post.title, post.content, post.published, post.rating, str(id)))
#     # updated_post = cursor.fetchone()
#     # conn.commit()
#     # print(post)
#     # index = find_index_post(id)
#     post = post_query.first()

#     if post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} does not exist")

#     post_query.update(updated_post.dict(), synchronize_session=False)
#     db.commit()
#     # post_dict = post.dict()
#     # post_dict['id'] = id
#     # my_posts[index] = post_dict
#     return post_query.first()
#     # return {"data": post_query.first()}


# @ app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

#     # hash password from user.password

#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password

#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user


# @app.get('/users/{id}', response_model=schemas.UserOut)
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()

#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with id: {id} does not exist.")

#     return user
