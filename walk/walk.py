import re
from .exceptions import (
    WalkDateError,
    WalkDistanceError,
    WalkDurationError
)


class Walk:
    def __init__(self, date: str, distance: float, duration: float) -> None:
        self._set_date_if_valid(date)
        self._set_distance_if_valid(distance)
        self._set_duration_if_valid(duration)

    def _set_date_if_valid(self, date: str) -> None:
        formatted_date = date.strip()
        date_pattern = re.compile('^\d{2}\/\d{2}\/\d{4}$')

        if not date_pattern.match(formatted_date):
            raise WalkDateError()

        self._date = formatted_date

    def _set_distance_if_valid(self, distance: float) -> None:
        MIN_DISTANCE = 1
        MAX_DISTANCE = 70

        if distance not in range(MIN_DISTANCE, MAX_DISTANCE + 1):
            raise WalkDistanceError()

        self._distance = distance

    def _set_duration_if_valid(self, duration: float) -> None:
        MIN_DURATION = 1
        MAX_DURATION = 900

        if duration not in range(MIN_DURATION, MAX_DURATION + 1):
            raise WalkDurationError()

        self._duration = duration

    @property
    def date(self) -> str:
        return self._date

    @property
    def distance(self) -> float:
        return self._distance

    @property
    def duration(self) -> float:
        return self._duration
