import os
from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager
from functools import wraps

engine = create_engine(os.getenv('DATABASE_URL'))
Session = sessionmaker(bind=engine)

Base = declarative_base()

def uses_db(func):
    @wraps(func)
    def context(*args, **kwargs):
        with db() as new_session:
            print(new_session)
            session = kwargs.get('session', None)

            if session is None:
                session = new_session
            
            kwargs['session'] = session
            return func(*args, **kwargs)
    return context

@contextmanager
def db():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
