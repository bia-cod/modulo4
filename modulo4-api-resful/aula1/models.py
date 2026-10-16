from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime
from sqlalchemy.sql import func
from database import Base

class Produto(Base):
    _tablename_ = 'produtos' # nome da tabela no banco

    #Colunas da tabela
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    ativo = Column(Boolean, default=True)
criado_em = Column(DateTime(timezone=True), server_default=func.now())

#_repr_ - como o objeto aparece no terminal (ú´til para debug)
def_repr_(self):
   return f'<Produto id={self.id} nome={self.nome}'

