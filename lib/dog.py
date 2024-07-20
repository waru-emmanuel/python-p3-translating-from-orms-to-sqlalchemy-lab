from models import Dog

def create_table(base,engine):
    base.metadata.create_all(engine)

    
def save(session, dog):
    """Saves a dog instance to the database and commits the transaction."""
    session.add(dog)
    session.commit()
    return dog.id
    

def get_all(session):
    """Returns a list of all Dog instances in the database."""
    return session.query(Dog).all()

def update_breed(session, dog, breed):
    """Updates the dog's breed in the database and commits the transaction."""
    dog.breed = breed
    session.commit()
    return dog
    

def find_by_name(session, name):
    """Returns the first Dog instance in the database with the given name."""
    return session.query(Dog).filter(Dog.name == name).first()


def find_by_id(session, id):
    """Returns the first Dog instance in the database with the given id."""
    return session.query(Dog).filter(Dog.id == id).first()
    
def find_by_name_and_breed(session, name, breed):
    """Returns the first Dog instance in the database with the given name and breed."""
    return session.query(Dog).filter(Dog.name == name).filter(Dog.breed == breed).first()
    

def update_breed(session, dog, breed):
    """Updates the dog's breed in the database and commits the transaction."""
    dog.breed = breed
    session.commit()
    return dog

    