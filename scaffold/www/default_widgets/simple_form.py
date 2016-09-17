from scaffold.core.widget import base_widget_extended


class control(base_widget_extended):
    method = 'post'
    action = '/'
    inputs = []
    template = '''
        <div class="row">
            <div class="input-field col s12">
              %s
            </div>
          </div>'''

    def create(self, action, method='post'):
        self.action = action
        self.method = method
        return self

    @staticmethod
    def set_template(template):
        if template:
            control.template = template

    def append(self, input_type, input_name, label, values="", classes='validate', disabled=''):
        if input_type == 'select' and values:
            if isinstance(values, (str or unicode)):
                self.inputs.append("""<select name="%s" id="%s">%s</select>""" % (
                    input_name,
                    input_name,
                    """<option value="%s">%s</option>""" % (values, values)))
                return self
            if isinstance(values[0], (str or unicode)):
                self.inputs.append("""<select name="%s" id="%s">%s</select>""" % (
                    input_name,
                    input_name,
                    '\n'.join(["""<option value="%s">%s</option>""" % (value, value) for value in values])))
                return self
            if type(values[0]) in (list, tuple):
                self.inputs.append("""
                    <select name="%s" id="%s">%s</select>""" % (
                        input_name,
                        input_name,
                        "\n".join(["""<option value="%s">%s</option>""" % (value, item) for value, item in values])))
            return self 

        if input_type == 'textarea':
            self.inputs.append("""<textarea name="%s" id="%s">%s</textarea>""" % (input_name, input_name, values))
            return self 


        self.inputs.append("""
            <input type="%s" name="%s" id="%s" placeholder="%s" %s classes="%s" value="%s" />
            <label for="%s">%s</label>""" % (
                input_type,
                input_name,
                input_name,
                label,
                'disabled="disabled" ' if disabled else '',
                classes,
                values,
                input_name,
                label
            )
        )
        return self

    def render(self):
        super(control, self).render()
        return """<div class="row">
                <form class="col s12" method="%s" action="%s">
                    %s
                </form>
            </div>""" % (
                self.method,
                self.action,
                "\n".join([control.template % input_item for input_item in self.inputs])
            )
