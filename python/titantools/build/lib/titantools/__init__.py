from __future__ import unicode_literals

__copyright__ = "2014, Mike Mackintosh"
__version__ = '0.0.3'

try:
      __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
      __path__ = __import__('pkgutil').extend_path(__path__, __name__)
