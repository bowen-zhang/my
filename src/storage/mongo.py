from bson import objectid


import settings
from storage import interface
from third_party.mongo_utils import storage as mongo_storage


class SystemCollection(interface.Collection):
  def __init__(self, proto_cls, collection, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self._storage = mongo_storage.ProtobufMongoStorage(proto_cls=proto_cls,
                                                       database=settings.current['database'], collection=collection)

  def get(self, id):
    return self._storage.find_one({'id': id})

  def find_one(self, filter=None, sort=None, projection=None):
    filter = filter or {}
    return self._storage.find_one(filter=filter, sort=sort, projection=projection)

  def load(self, filter=None, limit=0, sort=None, projection=None):
    filter = filter or {}
    return list(self._storage.find(filter=filter, limit=limit, sort=sort, projection=projection))

  def save(self, proto):
    if proto.id:
      self._storage.save(proto, {'id': proto.id})
    else:
      proto.id = self._storage.save(proto)
      self._storage.save(proto, {'_id': objectid.ObjectId(proto.id)})

    return self.get(proto.id)

  def delete(self, id):
    self._storage.collection.delete_many({'id': id})

  def delete_all(self, filter=None):
    """Deletes all documents satisfying the filter.

    Args:
      filter (dict): MongoDB filter.
    Returns:
      # of documents deleted.
    """
    filter = filter or {}
    return self._storage.collection.delete_many(filter).deleted_count


class UserCollection(interface.Collection):
  def __init__(self, proto_cls, collection, user_id, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self._storage = mongo_storage.ProtobufMongoStorage(proto_cls=proto_cls,
                                                       database=settings.current['database'], collection=collection)
    self._user_id = user_id

  def get(self, id):
    return self._storage.find_one({
        'id': id,
        'user_id': self._user_id,
    })

  def find_one(self, filter=None, sort=None, projection=None):
    filter = filter or {}
    filter['user_id'] = self._user_id
    return self._storage.find_one(filter=filter, sort=sort, projection=projection)

  def load(self, filter=None, limit=0, sort=None, projection=None):
    filter = filter or {}
    filter['user_id'] = self._user_id
    return list(self._storage.find(filter=filter, limit=limit, sort=sort, projection=projection))

  def save(self, proto):
    proto.user_id = self._user_id
    if proto.id:
      self._storage.save(proto, {'id': proto.id, 'user_id': self._user_id})
    else:
      proto.id = self._storage.save(proto)
      self._storage.save(proto, {'_id': objectid.ObjectId(
          proto.id), 'user_id': self._user_id})

    return self.get(proto.id)

  def delete(self, id):
    self._storage.collection.delete_many({
        'id': id,
        'user_id': self._user_id,
    })

  def delete_all(self, filter=None):
    filter = filter or {}
    filter['user_id'] = self._user_id
    self._storage.collection.delete_many(filter)


class MultiUserCollection(interface.Collection):
  def __init__(self, proto_cls, collection, user_ids, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self._storage = mongo_storage.ProtobufMongoStorage(proto_cls=proto_cls,
                                                       database=settings.current['database'], collection=collection)
    self._user_ids = user_ids

  def get(self, id):
    return self._storage.find_one({
        'id': id,
        'user_id': {'$in': self._user_ids},
    })

  def find_one(self, filter=None, sort=None, projection=None):
    filter = filter or {}
    filter['user_id'] = {'$in': self._user_ids}
    return self._storage.find_one(filter=filter, sort=sort, projection=projection)

  def load(self, filter=None, limit=0, sort=None, projection=None):
    filter = filter or {}
    filter['user_id'] = {'$in': self._user_ids}
    return list(self._storage.find(filter=filter, limit=limit, sort=sort, projection=projection))

  def save(self, proto):
    raise interface.StorageException(
        'Mutation not allowed with multi-user access.')

  def delete(self, id):
    raise interface.StorageException(
        'Mutation not allowed with multi-user access.')

  def delete_all(self, filter=None):
    raise interface.StorageException(
        'Mutation not allowed with multi-user access.')
