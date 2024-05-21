#!/usr/bin/python3
"""Hello module"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_hbnb(strict_slashes=False):
        """Hello HBNB

            Returns:
                    greetings(str): Hello HBNB!

                        """
                            return 'Hello HBNB!'


                        @app.route('/hbnb')
                        def display_hbnb(strict_slashes=False):
                                """Displays HBNB"""
                                    return 'HBNB'


                                @app.route('/c/<path:subpath>')
                                def display_subpath(subpath, strict_slashes=False):
                                        """Displays c/text"""
                                            return 'C {}'.format(subpath.replace('_', ' '))


                                        @app.route('/python/<path:subpath>')
                                        def python_path(subpath, strict_slashes=False):
                                                """Display the subpath Python"""
                                                    return 'Python {}'.format(subpath.replace('_', ' '))


                                                @app.route('/python/')
                                                def python_pathless(strict_slashes=False):
                                                        """Display the default option"""
                                                            return 'Python is cool'


                                                        @app.route('/number/<int:num>')
                                                        def show_integer(num, strict_slashes=False):
                                                                """Display n only if integer"""
                                                                    return '{} is a number'.format(num)


                                                                @app.route('/number_template/<int:num>')
                                                                def html_page(num, strict_slashes=False):
                                                                        """Returns
                                                                                html page(html): only if n is an integer
                                                                                    """
                                                                                        return render_template('5-number.html', num=num)


                                                                                    @app.route('/number_odd_or_even/<int:num>')
                                                                                    def even_odd(num, strict_slashes=False):
                                                                                            """Returns
                                                                                                    html page(html): if integer
                                                                                                        """
                                                                                                            return render_template('6-number_odd_or_even.html', num=num)


                                                                                                        if __name__ == "__main__":
                                                                                                                app.run(host='0.0.0.0', port=5000)#!/usr/bin/python3
                                                                                                                """Hello module"""

                                                                                                                from flask import Flask
                                                                                                                from flask import render_template
                                                                                                                app = Flask(__name__)


                                                                                                                @app.route('/')
                                                                                                                def hello_hbnb(strict_slashes=False):
                                                                                                                        """Hello HBNB

                                                                                                                            Returns:
                                                                                                                                    greetings(str): Hello HBNB!

                                                                                                                                        """
                                                                                                                                            return 'Hello HBNB!'


                                                                                                                                        @app.route('/hbnb')
                                                                                                                                        def display_hbnb(strict_slashes=False):
                                                                                                                                                """Displays HBNB"""
                                                                                                                                                    return 'HBNB'


                                                                                                                                                @app.route('/c/<path:subpath>')
                                                                                                                                                def display_subpath(subpath, strict_slashes=False):
                                                                                                                                                        """Displays c/text"""
                                                                                                                                                            return 'C {}'.format(subpath.replace('_', ' '))


                                                                                                                                                        @app.route('/python/<path:subpath>')
                                                                                                                                                        def python_path(subpath, strict_slashes=False):
                                                                                                                                                                """Display the subpath Python"""
                                                                                                                                                                    return 'Python {}'.format(subpath.replace('_', ' '))


                                                                                                                                                                @app.route('/python/')
                                                                                                                                                                def python_pathless(strict_slashes=False):
                                                                                                                                                                        """Display the default option"""
                                                                                                                                                                            return 'Python is cool'


                                                                                                                                                                        @app.route('/number/<int:num>')
                                                                                                                                                                        def show_integer(num, strict_slashes=False):
                                                                                                                                                                                """Display n only if integer"""
                                                                                                                                                                                    return '{} is a number'.format(num)


                                                                                                                                                                                @app.route('/number_template/<int:num>')
                                                                                                                                                                                def html_page(num, strict_slashes=False):
                                                                                                                                                                                        """Returns
                                                                                                                                                                                                html page(html): only if n is an integer
                                                                                                                                                                                                    """
                                                                                                                                                                                                        return render_template('5-number.html', num=num)


                                                                                                                                                                                                    @app.route('/number_odd_or_even/<int:num>')
                                                                                                                                                                                                    def even_odd(num, strict_slashes=False):
                                                                                                                                                                                                            """Returns
                                                                                                                                                                                                                    html page(html): if integer
                                                                                                                                                                                                                        """
                                                                                                                                                                                                                            return render_template('6-number_odd_or_even.html', num=num)


                                                                                                                                                                                                                        if __name__ == "__main__":
                                                                                                                                                                                                                                app.run(host='0.0.0.0', port=5000)
