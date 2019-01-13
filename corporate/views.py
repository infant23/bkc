from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import View
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q


from .models import Upload, Company, Content
# from .utils import ObjectPaginationlMixin, ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
# from .forms import PostForm, TagForm, CommentForm, ImageForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# class PostIndex(ObjectPaginationlMixin, View):
#     model = Article
#     template = 'dracoin/index.html'
#     page_value = 5
