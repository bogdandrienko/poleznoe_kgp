from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, FileExtensionValidator
from django.utils import timezone
from django_cleanup import cleanup


@cleanup.select
class IdeaModel(models.Model):
    """
    Сущность полезного предложения
    """
    author = models.CharField(
        validators=[MinLengthValidator(1), MaxLengthValidator(200)],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='ФИО(полностью)',
        help_text='<small class="text-muted">CharField [1, 200]</small><hr><br>',

        max_length=200,
    )
    subdivision = models.CharField(
        validators=[MinLengthValidator(1), MaxLengthValidator(50), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Подразделение',
        help_text='<small class="text-muted">CharField [1, 50]</small><hr><br>',

        max_length=50,
    )
    position = models.CharField(
        validators=[MinLengthValidator(1), MaxLengthValidator(200), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Профессия, должность',
        help_text='<small class="text-muted">CharField [1, 200]</small><hr><br>',

        max_length=200,
    )
    phone = models.CharField(
        validators=[MinLengthValidator(1), MaxLengthValidator(100), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Номер телефона',
        help_text='<small class="text-muted">CharField [1, 100]</small><hr><br>',

        max_length=100,
    )
    email = models.EmailField(
        validators=[MinLengthValidator(1), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Электронная почта(e-mail)',
        help_text='<small class="text-muted">CharField [1, 300]</small><hr><br>',

        max_length=300,
    )
    title = models.CharField(
        validators=[MinLengthValidator(1), MaxLengthValidator(300), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Предложение(наименование)',
        help_text='<small class="text-muted">CharField [1, 300]</small><hr><br>',

        max_length=300,
    )
    description = models.TextField(
        validators=[MinLengthValidator(1), MaxLengthValidator(3000), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Описание',
        help_text='<small class="text-muted">CharField [1, 3000]</small><hr><br>',

        max_length=3000,
    )
    place = models.TextField(
        validators=[MinLengthValidator(1), MaxLengthValidator(2000), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Краткое описание объекта, место применения',
        help_text='<small class="text-muted">CharField [1, 2000]</small><hr><br>',

        max_length=2000,
    )
    effect = models.TextField(
        validators=[MinLengthValidator(1), MaxLengthValidator(1000), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Ожидаемый эффект',
        help_text='<small class="text-muted">CharField [1, 1000]</small><hr><br>',

        max_length=1000,
    )
    need = models.TextField(
        validators=[MinLengthValidator(1), MaxLengthValidator(1000), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Необходимые ТМЦ',
        help_text='<small class="text-muted">CharField [1, 1000]</small><hr><br>',

        max_length=1000,
    )
    is_feedback = models.BooleanField(
        editable=True,
        blank=True,
        null=False,
        default=False,
        verbose_name='Нужно ли связаться с человеком',
        help_text='<small class="text-muted">BooleanField</small><hr><br>',
    )
    link = models.TextField(
        validators=[MinLengthValidator(1), MaxLengthValidator(900), ],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default='',
        verbose_name='Ссылка(на приложения)',
        help_text='<small class="text-muted">CharField [1, 900]</small><hr><br>',

        max_length=900,
    )
    created = models.DateTimeField(
        editable=True,
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name='Дата и время создания',
        help_text='<small class="text-muted">DateTimeField</small><hr><br>',

        auto_now=False,
        auto_now_add=False,
    )

    class Meta:
        app_label = 'django_app'
        ordering = ('-created', 'title')
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'
        db_table = 'django_app_post_model_table'

    def __str__(self):
        if self.is_feedback:
            completed = "Нужно связаться"
        else:
            completed = "Не нужно связываться"
        return f"[{self.created}] {self.title} ({self.id}) | {self.description[0:30]}... | {completed}"
