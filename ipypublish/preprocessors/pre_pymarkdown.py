# -*- coding: utf-8 -*-
"""Nbconvert preprocessor for the python-markdown nbextension."""

import re

from nbconvert.preprocessors import Preprocessor


class PyMarkdownPreprocessor(Preprocessor):
    """
    :mod:`nbconvert` Preprocessor for the python-markdown nbextension.

    This :class:`~nbconvert.preprocessors.Preprocessor` replaces kernel code in
    markdown cells with the results stored in the cell metadata.
    """

    def replace_variables(self, source, variables):
        """
        Replace {{variablename}} with stored value
        """
        try:
            replaced = re.sub(
                "{{(.*?)}}", lambda m: variables.get(m.group(1), ""), source
            )
        except TypeError:
            replaced = source
        return replaced

    def preprocess_cell(self, cell, resources, index):
        """
        Preprocess cell

        Parameters
        ----------
        cell : NotebookNode cell
            Notebook cell being processed
        resources : dictionary
            Additional resources used in the conversion process.  Allows
            preprocessors to pass variables into the Jinja engine.
        cell_index : int
            Index of the cell being processed (see base.py)
        """
        if cell.cell_type == "markdown":
            if hasattr(cell["metadata"], "variables"):
                variables = cell["metadata"]["variables"]
                if len(variables) > 0:
                    cell.source = self.replace_variables(cell.source, variables)
        return cell, resources

    # def preprocess(self, nb, resources):
    #     """
    #     Preprocess cell

    #     Parameters
    #     ----------
    #     cell : NotebookNode cell
    #         Notebook cell being processed
    #     resources : dictionary
    #         Additional resources used in the conversion process.  Allows
    #         preprocessors to pass variables into the Jinja engine.
    #     cell_index : int
    #         Index of the cell being processed (see base.py)
    #     """
    #     final_cells = []
    #     for cell in nb.cells:
    #         final_cells.append(self.preprocess_cell(cell))

    #     nb.cells = final_cells

    #     return nb, resources
    #     # if cell.cell_type == "markdown":
    #     #     if hasattr(cell['metadata'], 'variables'):
    #     #         variables = cell['metadata']['variables']
    #     #         if len(variables) > 0:
    #     #             cell.source = self.replace_variables(
    #     #                 cell.source, variables)
    #     # return cell, resources
