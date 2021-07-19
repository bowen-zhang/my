from absl import app as absl_app
import flask

from third_party.common import app


class MyApp(app.App):
  def __init__(self):
    super().__init__(name='My')
    self.init_logging('../../log', console_handler=None)

    self._web = flask.Flask(__name__,
                            template_folder='../web',
                            static_url_path='',
                            static_folder='../web')
    self._web.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    self._web.add_url_rule('/', view_func=self._on_index)

  def run(self):
    self._web.run(host='0.0.0.0', port=8081, debug=True)

  def _on_index(self):
    return self._web.send_static_file('index.html')


def main(argv):
  MyApp().run()


if __name__ == '__main__':
  absl_app.run(main)
