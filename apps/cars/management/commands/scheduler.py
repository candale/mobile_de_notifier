from os import path
import subprocess

from django.core.management.base import BaseCommand
from django.conf import settings

from crontab import CronTab


class Command(BaseCommand):
    help = 'Start or stop the scheduler (cron job) for the mailing or crawler'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self._crontab = CronTab(user=settings.CRONTAB_USER)

    def add_arguments(self, parser):
        start_group = parser.add_mutually_exclusive_group()
        stop_group = parser.add_mutually_exclusive_group()

        start_group.add_argument(
            '-c', '--crawler', choices=['start', 'stop'],
            help='Start crontab scheduler for scraping and email sending')

        stop_group.add_argument(
            '-m', '--mailing', choices=['start', 'stop'],
            help='Stop crontab scheduler for scraping and email sending')

    def get_python_path(self):
        if settings.RUNNING_IN_VIRTUALENV:
            return path.join(path.dirname(settings.BASE_DIR), 'bin/python')
        else:
            return subprocess.check_output(['which', 'python']).strip()

    def get_scrapy_path(self):
        if settings.RUNNING_IN_VIRTUALENV:
            return path.join(path.dirname(settings.BASE_DIR), 'bin/scrapy')
        else:
            return subprocess.check_output(['which', 'scrapy']).strip()

    def get_scheduler_file_path(self):
        return path.join(settings.SHEDUELR_SCRIPTS_DIRECTORY,
                         settings.SCHDEULER_SCRIPT_NAME)

    def get_crawler_command(self):
        return 'cd {} && {} crawl {}'.format(
            settings.SCRAPY_PROJECT_ROOT,
            self.get_scrapy_path(),
            settings.SPIDER_NAME
        )

    def get_mailing_command(self):
        return 'cd {} && {} manage.py send_emails'.format(
            settings.BASE_DIR,
            self.get_python_path()
        )

    def _get_or_create_job(self, command, comment, interval):
        jobs_list = list(
            self._crontab.find_comment(comment)
        )

        if len(jobs_list) > 1:
            raise ValueError(
                'There are more than one job with the configured comment')

        if not jobs_list:
            job = self._crontab.new(command=command, comment=comment)
            job.minute.every(interval)
            job.enable(False)
        else:
            job = jobs_list[0]

        return job

    def handle_job(self, job, action):
        if action == 'start' and job.is_enabled() is False:
            job.enable()
            self._crontab.write()

        if action == 'stop' and job.is_enabled():
            job.enable(False)
            self._crontab.write()

    def handle_crawler(self, action):
        job = self._get_or_create_job(
            self.get_crawler_command(), settings.CRONTAB_CRAWLER_ENTRY_COMMENT,
            settings.CRAWLER_SCHEDULER_BEAT_INTERVAL
        )

        self.handle_job(job, action)

    def handle_mailing(self, action):
        job = self._get_or_create_job(
            self.get_mailing_command(), settings.CRONTAB_MAILING_ENTRY_COMMENT,
            settings.MAILING_SCHEDULER_BEAT_INTERVAL
        )

        self.handle_job(job, action)

    def handle(self, *args, **options):
        import pudb; pu.db
        if 'crawler' in options and options['crawler']:
            self.handle_crawler(options['crawler'])
        elif 'mailing' in options and options['mailing']:
            self.handle_mailing(options['mailing'])
