from eralchemy import render_er
## Draw from SQLAlchemy base
render_er(Base, 'erd_from_sqlalchemy.png')

## Draw from database
render_er("sqlite:///mydb.db", 'erd_from_sqlite.png')