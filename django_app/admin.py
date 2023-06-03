from django.contrib import admin
from django_app import models

admin.site.site_header = 'Панель управления'
admin.site.index_title = 'Администрирование сайта'
admin.site.site_title = 'Администрирование'


class IdeaAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'IdeaModel' на панели администратора
    """

    list_display = (
        "author",
        "subdivision",
        "position",
        "phone",
        "email",
        "title",
        "description",
        "place",
        "effect",
        "need",
        "link",
        "is_feedback",
        "created",
    )
    list_display_links = (
        "author",
        "subdivision",
        "position",
        "title",
    )
    list_editable = (
        "is_feedback",
    )
    list_filter = (
        "author",
        "subdivision",
        "position",
        "phone",
        "email",
        "title",
        "description",
        "place",
        "effect",
        "need",
        "link",
        "is_feedback",
        "created",
    )
    # filter_horizontal = (
    #     'users',
    # )
    fieldsets = (
        (
            "Основное",
            {
                "fields": (
                    "author",
                    "subdivision",
                    "position",
                    "phone",
                    "email",
                    "title",
                    "description",
                    "place",
                    "effect",
                    "need",
                )
            },
        ),
        (
            "Техническое",
            {
                "fields": (
                    "link",
                    "is_feedback",
                    "created",
                )
            },
        ),
    )
    search_fields = [
        "author",
        "subdivision",
        "position",
        "email",
        "title",
        "description",
        "place",
        "effect",
        "need",
    ]


admin.site.register(models.IdeaModel, IdeaAdmin)
