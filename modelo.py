from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///habilidades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Programador(Base):
    __tablename__ = 'programador'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)
    email = Column(String(60))

    def __repr__(self):
        return '<Programador {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit(self)

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Habilidade(Base):
    __tablename__ = 'habilidade'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)

    def __repr__(self):
        return '<Habilidade: {}>'.format(self.nome)


class ProgramadorHabilidade(Base):
    __tablename__ = 'programador_habilidade'
    id = Column(Integer, primary_key=True)
    programador_nome = Column(String, ForeignKey('programador.nome'))
    habilidade_nome = Column(String, ForeignKey('programador.nome'))
    programador = relationship('Programador')
    habilidade = relationship('Habilidade')
