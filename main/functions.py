def genarate_form_errors(form):
    message = ''
    for field in form:
        if field.errors:
            message += field.errors
    for err in form.non_field_errors():
        message += str(err)
    
    return message
