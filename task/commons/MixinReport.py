# coding=utf-8
import os

from django.http import HttpResponse
from secretary import Renderer

from restAuth import settings


class MixinReport():
    """
        Использует для рендера шаблонов
            С использование библиотеки secretary
    """
    engine = Renderer()
    template_name = ''  # Имя шаблона для рендера
    context = {}  # Данные

    # renderers
    def renders(self):
        template = os.path.join(settings.BASE_DIR, 'static', self.template_name)
        result = self.engine.render(template, **self.context)
        return result



    def get_report(self):
        """
            Возваращет готовый шаблон
        """
        response = HttpResponse(content_type='application/odt', content=self.renders())
        response['Content-Disposition'] = 'attachment; filename="renders.odt"'
        return response
