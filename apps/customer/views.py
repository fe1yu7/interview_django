from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import serializers

from common.paginator import pages
from common.utils import json_response
from .models import CustomerModel


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CustomerModel


class CustomerResource(APIView):
    def get(self, request):
        request_data = self.request.query_params
        client_name = request_data.get('client_name')
        page_size = int(request_data.get('page_size', 10))
        page = int(request_data.get('page', 1))
        if not client_name:
            return JsonResponse(data=json_response('', 'missing parameters client_name', 422))
        customer_obj = CustomerModel.objects.all().order_by("-score")  # 成绩倒序排列
        paginator = pages(customer_obj, page, page_size)
        customer_data = CustomerSerializers(customer_obj, many=True)
        data_list = list()
        for index, customer in enumerate(customer_data.data):
            data_list.append({'index': index + 1, 'customer': customer})
        data = {
            "page": page,
            "count": page_size,
            "total": paginator.count,
            "data": data_list
        }
        return JsonResponse(data=json_response(data, 'successful', 200))

    def post(self, request):
        """
        更新、新建客户端数据
        :param request:
        :return: 200  or 422（missing parameters）
        """
        request_data = self.request.data
        client_name = request_data.get('client_name')
        score = request_data.get('score')
        if not score or not client_name:
            return JsonResponse(data=json_response('', 'missing parameters client_name or score', 422))

        customer_obj = CustomerModel.objects.filter(client_name=client_name).first()
        if not customer_obj:
            CustomerModel.objects.create(client_name=client_name, score=score)
        else:
            customer_obj.score = score
            customer_obj.save()
        return JsonResponse(data=json_response('', 'save successful', 200))
