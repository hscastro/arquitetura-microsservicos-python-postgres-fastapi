

class User:

    def __init__(self, id, email, password_hash, role, created_at):
        self.id = id                          # Atributo de instância
        self.email = email                    # Atributo de instância
        self.password_hash = password_hash    # Atributo de instância
        self.role = role                      # Atributo de instância
        self.created_at = created_at          # Atributo de instância