"""Serves the single page app web ui."""

import json

from ndscheduler import settings
from ndscheduler import utils
from ndscheduler.version import __version__
from ndscheduler.server.handlers import base
from getpass import getuser
import platform
import pkg_resources
import logging


def get_system_info():
    return platform.uname()


logger = logging.getLogger(__name__)


class Handler(base.BaseHandler):
    """Index page request handler."""

    def get(self):
        """Serve up the single page app for scheduler dashboard."""

        # redirect to root if coming from unknown URL via
        if self.request.uri != "/":
            self.redirect("/")
            return

        # Get job pack versions
        job_versions = []
        for job in settings.JOB_CLASS_PACKAGES:
            try:
                job_versions.append(f"{job} v{pkg_resources.require(job.split('.')[0])[0].version}")
            except pkg_resources.DistributionNotFound:
                job_versions.append(f"{job} <undefined>")

        if self.current_user and isinstance(self.current_user, bytes):
            admin_user = self.current_user.decode() in settings.ADMIN_USER
        else:
            admin_user = self.current_user and self.current_user in settings.ADMIN_USER
        logger.debug("Is admin user: %s", admin_user)
        website_info = {
            "title": settings.WEBSITE_TITLE,
            "version": __version__,
            "job_versions": ", ".join(job_versions),
            "user": getuser(),
            "host": get_system_info().node,
            "admin_user": admin_user,  # self.current_user and self.current_user in settings.ADMIN_USER,
            "help_url": settings.HELP_URL,
            "issues_url": settings.ISSUES_URL,
        }

        meta_info = utils.get_all_available_jobs()
        self.render(
            settings.APP_INDEX_PAGE,
            jobs_meta_info=json.dumps(meta_info),
            website_info=website_info,
            # current_user=self.get_current_user(),
        )
