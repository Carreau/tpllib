"""
A library with jupyter nbconvert templates
"""

import os
import os.path

from traitlets.config import Config
from nbconvert.exporters.html import HTMLExporter
from nbconvert.exporters.latex import LatexExporter

__version__='0.1.2'

#-----------------------------------------------------------------------------
# Classes
#-----------------------------------------------------------------------------

class MyExporter(HTMLExporter):
    """
    My custom exporter  
    """
    
    @property
    def template_path(self):
        """
        We want to inherit from HTML template, and have template under
        `./templates/` so append it to the search path. (see next section)
        """
        return super().template_path+[os.path.join(os.path.dirname(__file__), "templates")]

    def _template_file_default(self):
        """
        We want to use the new template we ship with our library.
        """
        return 'noprompt' # full



class TexCJK(LatexExporter):
    """
    My custom exporter  
    """
    
    @property
    def template_path(self):
        """
        We want to inherit from HTML template, and have template under
        `./templates/` so append it to the search path. (see next section)
        """
        return super().template_path+[os.path.join(os.path.dirname(__file__), "templates")]

    def _template_file_default(self):
        return 'noprompt' # full


class ChineeseCJK(TexCJK):

    def _template_file_default(self):
        return 'latex_chineese'

