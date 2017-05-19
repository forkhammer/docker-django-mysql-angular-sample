# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, View, FormView
from django.contrib.auth.views import login, logout
from django.utils.decorators import method_decorator
from annoying.decorators import ajax_request
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response, HttpResponseRedirect
import json
from django.core.urlresolvers import reverse


class BreadcrumbMixin(object):
    def get_context_data(self, **kwargs):
        self.request.breadcrumbs(self.get_breadcrumbs())
        return super(BreadcrumbMixin, self).get_context_data(**kwargs)

    def get_breadcrumbs(self):
        return []


class LoginRequiredMixin(object):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated():
            return HttpResponseForbidden()
        else:
            return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class AjaxResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            error_message = ''
            for field in form.errors:
                error_message += '<p class="error">%s</p>' % form.errors[field][0]
            return self.render_to_json_response({'message': error_message}, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = self.get_ajax_response()
            return self.render_to_json_response(data)
        else:
            return response

    def dispatch(self, request, *args, **kwargs):
        try:
            return super(AjaxResponseMixin, self).dispatch(request, *args, **kwargs)
        except Exception as ex:
            if self.request.is_ajax():
                data = {
                    'message': str(ex)
                }
                return self.render_to_json_response(data, status=400)
            else:
                raise ex

    def delete(self, request, *args, **kwargs):
        del_id = self.get_object().pk
        response = super(AjaxResponseMixin, self).delete(request, *args, **kwargs)
        if self.request.is_ajax():
            data = self.get_ajax_response()
            return self.render_to_json_response(data)
        else:
            return response

    def get_ajax_response(self):
        return {}

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax() and self.request.method == 'POST':
            return self.render_to_json_response({'result': True})
        else:
            return super(AjaxResponseMixin, self).render_to_response(context, **response_kwargs)