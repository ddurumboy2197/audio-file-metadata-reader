class EmailTemplateRenderer:
    def __init__(self, template):
        self.template = template

    def render(self, data):
        rendered_template = self.template
        for key, value in data.items():
            rendered_template = rendered_template.replace(f"{{ {key} }}", value)
        return rendered_template


def render_email(template, data):
    renderer = EmailTemplateRenderer(template)
    return renderer.render(data)


# Misol:
template = """
Salom, {name}!

Sizning emailingiz: {email}
Sizning manzilingiz: {address}

Dasturchi,
{dasturchi}
"""

data = {
    "name": "Ali",
    "email": "ali@example.com",
    "address": "Toshkent, Uzbekiston",
    "dasturchi": "Dasturchi"
}

print(render_email(template, data))
```

Kodni ishlatish uchun quyidagilar kerak:

1. `template` degan stringda email shablonini yozing.
2. `data` degan dictionaryda emailga kirishuvchi ma'lumotlarni yozing.
3. `render_email` funksiyasiga `template` va `data`ni bering.
4. Funksiya email shablonini `data`ga moslashtirib qaytadi.
