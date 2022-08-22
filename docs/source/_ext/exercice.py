from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from docutils import nodes

class exercise(nodes.Admonition, nodes.Element):
    pass

class ExerciseDirective(BaseAdmonition):
    node_class = exercise

def visit_exercise(self, node, name=''):
    self.visit_admonition(node, 'exercise')

def depart_exercise(self, node=None):
    self.depart_admonition(node)

def setup(app):
    app.add_directive('exercise', ExerciseDirective)

    app.add_node(exercise,
        html=(visit_exercise, depart_exercise)
    )