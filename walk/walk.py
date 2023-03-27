from .exceptions import (
    WalkDateError,
    WalkDistanceError,
    WalkDurationError
)
from datetime import datetime


class Walk:
    def __init__(self, date: str, distance: float, duration: float) -> None:
        self._set_date_if_valid(date)
        self._set_distance_if_valid(distance)
        self._set_duration_if_valid(duration)

    def _set_date_if_valid(self, date: str) -> None:
        strip_date = date.strip()

        if not self._validate_date(strip_date):
            raise WalkDateError()

        formatted_date = datetime.strptime(strip_date, '%d/%m/%Y') \
            .strftime('%d/%m/%Y')

        self._date = formatted_date

    def _validate_date(self, date: str) -> bool:
        try:
            datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
            return False

        return True

    def _set_distance_if_valid(self, distance: float) -> None:
        if not self._validate_distance(distance):
            raise WalkDistanceError()

        self._distance = float(distance)

    def _validate_distance(self, distance: float) -> bool:
        MIN_DISTANCE = 1
        MAX_DISTANCE = 70

        try:
            distance_float = float(distance)
        except ValueError:
            return False

        if distance_float < MIN_DISTANCE or distance_float > MAX_DISTANCE:
            return False

        return True

    def _set_duration_if_valid(self, duration: float) -> None:
        if not self._validate_duration(duration):
            raise WalkDurationError()

        self._duration = self._correct_mins_if_wrong(duration)

    def _validate_duration(self, duration: float) -> bool:
        MIN_DURATION = 1
        MAX_DURATION = 900

        try:
            duration_float = float(duration)
        except ValueError:
            return False

        if duration_float < MIN_DURATION or duration_float > MAX_DURATION:
            return False

        return True

    def _correct_mins_if_wrong(self, mins) -> float:
        mins_decimal = round(float(mins), 2)
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
