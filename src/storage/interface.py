import abc


class StorageException(Exception):
  pass


class Collection(abc.ABC):
  @abc.abstractmethod
  def get(self, id):
    pass

  def has(self, id):
    return self.get(id) != None

  @abc.abstractmethod
  def find_one(self, filter=None, sort=None, projection=None):
    pass

  @abc.abstractmethod
  def load(self, filter=None, limit=0, sort=None, projection=None):
    pass

  @abc.abstractmethod
  def save(self, proto):
    pass

  @abc.abstractmethod
  def delete(self, id):
    pass

  @abc.abstractmethod
  def delete_all(self, filter=None):
    pass
