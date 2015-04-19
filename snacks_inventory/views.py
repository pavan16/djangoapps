from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse

from snacks_inventory.models import Snack, User, SnackConsumer
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder

def index(request):
    all_snacks_list = Snack.objects.all()
    context = {'all_snacks_list': all_snacks_list }
    return render(request, 'snacks_inventory/index.html', context)


def user_registration(request):
    data = json.loads(request.body)
    new_user_name = data['user_name']
    new_user_email = data['user_email']
    new_user_password = data['user_password']
    try:
        user = User.objects.get(user_name=new_user_name)
    except User.DoesNotExist:
        user_obj = User.objects.create(user_name=new_user_name,
                                       user_email=new_user_email,
                                       password=new_user_password)

    if user.user_name == new_user_name:

        result = 'Successfully updated snacks inventory'
    else:
        result = 'Update not successful as snack quantity is not available'
    return HttpResponse(json.dumps({"status": result}),
                        content_type="application/json")






def get_all_snacks(request):
    snacks = list()
    all_snacks_list = Snack.objects.all()
    for snack in all_snacks_list:
        snacks_dict = dict()
        snacks_dict['snackName'] = snack.name
        snacks_dict['remainingQuantity'] = snack.original_quantity
        snacks.append(snacks_dict)
    data = {"snacks": snacks}
    return HttpResponse(json.dumps(data),
                        content_type="application/json")


@csrf_exempt
def consumed_an_item(request):
    data = json.loads(request.body)
    user_name = data['user_name']
    snack_id = data['snack_id']
    quantity = int(data['quantity'])
    snack = get_object_or_404(Snack, pk=snack_id)
    # snack_consumer = SnackConsumer.objects.create(consumed_user=user_name,
    #                                               sn)
    if snack.original_quantity > 0:
        snack.original_quantity -= quantity
        snack.user.user_name = user_name
        snack.save()
        result = 'Successfully updated snacks inventory'
    else:
        result = 'Update not successful as snack quantity is not available'
    return HttpResponse(json.dumps({"status": result}),
                        content_type="application/json")


def get_all_consumed_snacks(request):
    consumed_snacks_list = list()

    all_snacks_consumed_list = SnackConsumer.objects.all()

    for snack_consumer in all_snacks_consumed_list:
        snacks_consumed = dict()
        snacks_consumed['ConsumerName'] = snack_consumer.consumed_user.user_name
        snacks_consumed['ConsumedSnack'] = snack_consumer.consumed_snack_name.name
        snacks_consumed['ConsumedQuantity'] = snack_consumer.consumed_quantity
        snacks_consumed['ConsumedDate'] = snack_consumer.date_consumed
        consumed_snacks_list.append(snacks_consumed)
    data = {"snacks_consumed": consumed_snacks_list}
    return HttpResponse(json.dumps(data,
                                   cls=DjangoJSONEncoder),
                        content_type="application/json")