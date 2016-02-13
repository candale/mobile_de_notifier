from django.contrib import admin

from notifications.models import SearchUrl
from cars.admin import CarInline


@admin.register(SearchUrl)
class SearchUrlAdmin(admin.ModelAdmin):
    readonly_fields = (
        'next_run_date', 'number_of_times_scraped', 'next_mailing_run_date',
        'number_of_emails_sent'
    )
    inlines = (CarInline,)
