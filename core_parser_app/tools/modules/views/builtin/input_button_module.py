""" Input Button Module
"""
from core_parser_app.tools.modules.views.module import AbstractModule


class InputButtonModule(AbstractModule):
    """ Input Button module
    """
    def __init__(self, scripts=list(), styles=list(), button_label='Send', label=None, default_value=None):
        """ Initialize the module

        Args:
            scripts:
            styles:
            button_label:
            label:
            default_value:
        """
        AbstractModule.__init__(self, scripts=scripts, styles=styles)
        self.button_label = button_label
        self.label = label
        self.default_value = default_value

    def _render_module(self, request):
        """ Return the module rendering

        Args:
            request:

        Returns:

        """
        params = {"button_label": self.button_label}
        if self.label is not None:
            params.update({"label": self.label})
        if self.default_value is not None:
            params.update({"default_value": self.default_value})
        return AbstractModule.render_template('core_parser_app/builtin/input_button.html', params)

    def _retrieve_data(self, request):
        """ Retrieve module's data

        Args:
            request:

        Returns:

        """
        raise NotImplementedError("_retrieve_data method is not implemented.")

    def _render_data(self, request):
        """ Retrieve module's data rendering

        Args:
            request:

        Returns:

        """
        raise NotImplementedError("_render_data method is not implemented.")