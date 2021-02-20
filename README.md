# mailer

python django mailer

# routes

| Route                                            | Response           | Description                                |
| ------------------------------------------------ | ------------------ | ------------------------------------------ |
| /mailer/templates                                | html               | links to templates (all types)             |
| /mailer/templates/<name>?type=<type>             | html               | show template                              |
| /mailer/render?template=<html>&context=<context> | html               | render, post?                              |
| /mailer/mails                                    | html               | list mails                                 |
| /mailer/mails/<id>                               | html               | show mail header, body (iframe) and status |
| /mailer/api/mails                                | rest create        |                                            |
| /mailer/api/mails/<id>                           | rest update delete |                                            |
| /mailer/api/mails/<id>/send                      | rest               |                                            |
| /mailer/api/templates                            | rest               |                                            |

docs:
https://docs.djangoproject.com/en/3.2/ref/templates/api/#rendering-a-context
https://email.uplers.com/blog/step-step-guide-create-html-email/
