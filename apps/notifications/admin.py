from django.contrib import admin

from notifications.models import SearchUrl


@admin.register(SearchUrl)
class SearchUrlAdmin(admin.ModelAdmin):
    readonly_fields = ('next_run_date', 'number_of_times_scraped')
