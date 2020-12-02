"""django_admin_search_filter - Allows to create admin list filter as a search box for free-input"""

__version__ = '0.1.0'
__author__ = 'Mikhail Koipish <mkoypish@gmail.com>'
__all__ = []


from django.contrib import admin
from django.db.models import Q


class InputFilter(admin.SimpleListFilter):
    template = 'input_admin_filter.html'

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return [
            ('x','x')
        ]
    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice

import typing
def get_icontains_input_filter(title_, attrs: typing.Union[list, tuple, str]):


    if isinstance(attrs, str):
        attrs = (attrs, )

    class FilterCls(InputFilter):

        parameter_name = '-'.join(attrs) + '-icontains'
        title = title_

        def queryset(self, request, queryset):

            if self.value():
                query = Q()
                for a in attrs:
                    query |= Q(**{
                        '%s__icontains' % a: self.value()
                    })

                return queryset.filter(query)
            return queryset

    return FilterCls


def get_exact_equals_input_filter(title_, attrs: typing.Union[list, tuple, str]):

    class FilterCls(InputFilter):
        parameter_name = '-'.join(attrs) + '-equals'
        title = title_

        def queryset(self, request, queryset):
            if self.value():
                query = Q()
                for a in attrs:
                    query |= Q(**{
                        '%s__iexact' % a: self.value()
                    })
                return queryset.filter(query)
            return queryset

    return FilterCls