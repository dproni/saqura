from django import forms
from django.utils.safestring import mark_safe
from django.conf import settings

class Redactor(forms.Textarea):
    class Media:
           css = {
               'all': ('pretty.css',)
           }
           js = ('animations.js', 'actions.js')
       

    def __init__(self, attrs=None):
        self.attrs = attrs
        if attrs:
            self.attrs.update(attrs)
        super(Redactor, self).__init__(attrs)

        #
        #
        # Jwysiwig
        #
        #

#    def render(self, name, value, attrs=None):
#        rendered = super(Redactor, self).render(name, value, attrs)
#        return rendered + mark_safe(u'''
#        <script type="text/javascript">
#        $(document).ready(function()	{
#             $('#id_%s').wysiwyg();
#        });
#        </script>''' % name)

        #
        #
        # Redactor
        #
        #

    def render(self, name, value, attrs=None):
        rendered = super(Redactor, self).render(name, value, attrs)
        return rendered + mark_safe(u'''
        <script type="text/javascript">
        $(document).ready(
            function()
            {
                $('#id_%s').redactor({ focus: true });
            }
        );
        </script>''' % name)
