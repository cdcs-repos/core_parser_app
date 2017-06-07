"""Core parser app admin views
"""

from django.http.response import HttpResponseBadRequest

from core_main_app.utils.rendering import admin_render
from core_parser_app.views.common.views import get_context


def manage_template_modules(request, template_id):
    """View that allows module management

    Args:
        request:
        template_id:

    Returns:

    """

    assets = {
        "js": [
            {
                "path": 'core_main_app/common/js/XMLTree.js',
                "is_raw": True
            },
            {
                "path": 'core_parser_app/common/js/module_manager.js',
                "is_raw": False
            },
            {
                "path": 'core_main_app/common/js/backtoprevious.js',
                "is_raw": True
            }
        ],
        "css": ['core_main_app/common/css/XMLTree.css']
    }

    try:
        return admin_render(request,
                            'core_parser_app/common/module_manager.html',
                            assets=assets,
                            context=get_context(template_id))
    except Exception, e:
        return HttpResponseBadRequest(e.message)
