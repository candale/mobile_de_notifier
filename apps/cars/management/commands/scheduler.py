from os import path
import subprocess

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from crontab import CronTab


class Command(BaseCommand):
    help = 'Manage crontab tasks'

    def __init__(self, *args, **kwargs):
        self._crontab = CronTab(user=settings.CRONTAB_USER)

    def add_arguments(self, parser):
        parser.add_argument(
            'start', action='store_true', dest='start', default=False,
            help='Start crontab scheduler for scraping and email sending')

        parser.add_argument(
            'stop', action='store_true', dest='stop', default=False,
            help='Stop crontab scheduler for scraping and email sending')

    def get_python_path(self):
        if settings.RUNNING_IN_VIRTUALENV:
            return path.join(path.dirname(settings.BASE_DIR), 'bin/python')
        else:
            return subprocess.check_output(['which', 'python']).strip()

    def get_scheduler_file_path(self):
        return path.join(settings.SHEDUELR_SCRIPTS_DIRECTORY,
                         settings.SCHDEULER_SCRIPT_NAME)

    def get_command(self):
        return '{} {}'.format(
            self.get_python_path(), self.get_scheduler_file_path()
        )

    def _get_or_create_job(self):
        jobs_list = list(
            self._crontab.find_comment(settings.CRONTAB_ENTRY_COMMENT)
        )

        if len(jobs_list) > 1:
            raise ValueError(
                'There are more than one job with the configured comment')

        if not jobs_list:
            job = self._crontab.new(command=self.get_command())
            job.every(settings.SCHEDULER_BEAT_INTERVAL)
            job.enable(False)
        else:
            job = jobs_list[0]

        return job

    def handle(self, *args, **options):
        if options['start'] and options['stop']:
            raise CommandError('You can only stop or start, man.')

        job = self._get_or_create_job()

        if options['start'] and job.is_enabled() is False:
            job.enable()
            self._crontab.write()

        if options['stop'] and job.is_enabled():
            job.enable(False)
            self._crontab.write()
