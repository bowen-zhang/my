import yaml


_DEFAULT_SETTINGS_FILEPATH = './settings.yaml'


def _load(path=None):
  path = path or _DEFAULT_SETTINGS_FILEPATH
  with open(path, 'r') as f:
    settings = yaml.safe_load(f)
    env = settings['environment']
    return settings[env]


current = _load()
