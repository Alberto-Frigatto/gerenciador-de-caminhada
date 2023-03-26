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

        if distance < MIN_DISTANCE or distance > MAX_DISTANCE:
            raise WalkDistanceError()

        self._distance = distance

    def _set_duration_if_valid(self, duration: float) -> None:
        MIN_DURATION = 1
        MAX_DURATION = 900

        if duration < MIN_DURATION or duration > MAX_DURATION:
            raise WalkDurationError()

        self._duration = self._correct_mins_if_wrong(duration)

    def _correct_mins_if_wrong(self, mins) -> float:
        mins_decimal = round(mins, 2)
        seconds = round(mins_decimal - int(mins_decimal), 2)*100

        if seconds not in range(61):
            correction = .4

            mins_correct = mins_decimal + correction
            return mins_correct

        return mins_decimal

    @property
    def date(self) -> str:
        return self._date

    @property
    def distance(self) -> float:
        return self._distance

    @property
    def duration(self) -> float:
        return self._duration
