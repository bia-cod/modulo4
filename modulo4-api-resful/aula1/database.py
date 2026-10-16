












# SessionLocal: fábrica de sessões - cada requisição tem sua própria
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base: classe base



# yield entrega a sessão - endpoint execulta