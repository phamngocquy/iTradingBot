import datetime
import logging
from traceback import format_exc
from schedule import Job, Scheduler

_logger = logging.getLogger(__name__)


class SafeScheduler(Scheduler):
    """
    An implementation of Scheduler that catches jobs that fail, var their
    exception tracebacks as errors, and keeps going.

    Use this to run jobs that may or may not crash without worrying about
    whether other jobs will run or if they'll crash the entire script.
    """

    def __init__(self, rerun_immediately=True):
        self.rerun_immediately = rerun_immediately

        super().__init__()

    def _run_job(self, job: Job):
        # noinspection PyBroadException
        try:
            super()._run_job(job)
        except Exception:
            _logger.error(
                f"Error while {next(iter(job.tags))}...\n{format_exc()}"
            )
            job.last_run = datetime.datetime.now()
            if not self.rerun_immediately:
                # Reschedule the job for the next
                # time it was meant to run, instead of
                # letting it run
                # next tick
                job._schedule_next_run()  # pylint: disable=protected-access
