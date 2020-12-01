"""django_admin_search_filter - Allows to create admin list filter as a search box for free-input"""

__version__ = '0.1.0'
__author__ = 'Mikhail Koipish <mkoypish@gmail.com>'
__all__ = []


from django.contrib import admin



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


def get_icontains_input_filter(title_, parameter_name_):

    class FilterCls(InputFilter):

        parameter_name = parameter_name_ + '_icontains'
        title = title_

        def queryset(self, request, queryset):
            if self.value():
                return queryset.filter(**{
                    '%s__icontains' % parameter_name_: self.value()
                })
            return queryset

    return FilterCls


def get_exact_equals_input_filter(title_, parameter_name_):

    class FilterCls(InputFilter):

        parameter_name = parameter_name_ + '_equals'
        title = title_

        def queryset(self, request, queryset):
            if self.value():
                return queryset.filter(**{
                    '%s' % parameter_name_: self.value()
                })
            return queryset

    return FilterCls