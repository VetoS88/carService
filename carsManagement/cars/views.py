from typing import Union

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


class JSONResponseMixin:
    """
    Примесь для рендеринга json контента.
    """

    @staticmethod
    def render_to_json_response(context: Union[dict, list, iter], **response_kwargs):
        """
            Возвращает json http ответ.
        """
        return JsonResponse(
            context,
            **response_kwargs
        )

@method_decorator(csrf_exempt, name='dispatch')
class CarsAddView(JSONResponseMixin, View):
    """
        Представление добавления атомобиля
    """

    def get(self, request):
        """
        :return:
        """
        return self.render_to_json_response({
            'message': 'ok',
            'error': None
        })

    def post(self, request):
        """
            Добавление автомобиля
        """
        return self.render_to_json_response({
            'message': 'ok',
            'error': None
        })


class CarRetrieveView(JSONResponseMixin, View):
    """
        представление получения атомомбиля
    """

    def get(self, request, serial_number):
        """
        :return:
        """
        return self.render_to_json_response({
            'message': 'ok',
            'error': None
        })
