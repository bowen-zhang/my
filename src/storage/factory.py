from proto import core_pb2
from storage import mongo
from third_party.common import pattern


class StorageFactory(pattern.Singleton):
  def __init__(self):
    self._system_storage = SystemStorage()

  @property
  def system_storage(self):
    return self._system_storage

  def get_user_storage(self, user_id):
    return UserStorage(system_storage=self._system_storage, user_id=user_id)


class SystemStorage(object):
  def __init__(self):
    self._users = mongo.SystemCollection(core_pb2.User, 'users')

  @property
  def users(self):
    return self._users


class UserStorage(object):
  def __init__(self, system_storage, user_id):
    self._system_storage = system_storage
    self._user_id = user_id

  @property
  def system_storage(self):
    return self._system_storage

  @property
  def user_id(self):
    return self._user_id

  # User

  def load_user(self):
    return self._system_storage.users.get(self._user_id)

  def save_user(self, proto):
    assert proto.id == self._user_id
    self._system_storage.users.save(proto)
