from django.shortcuts import render
from vk import VkApi
from .forms import SearchUserForm


def index(request):
    formset = SearchUserForm()
    return render(request, 'vk/index.html', {'formset': formset})


def result(request):
    vk_resp = VkApi()
    vk_resp.get_friends_lst()
    return render(request, 'vk/result.html', {'vk_resp': vk_resp})
