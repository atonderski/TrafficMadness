from traffic_madness.track.trackbucket import TrackBucket
from traffic_madness.car import Car
import pytest

def test_default():
    trackbucket = TrackBucket(100,25, 3)
    assert len(trackbucket.bucket_list) == 4

def test_raise_not_divisible():
    with pytest.raises(ValueError):
        trackbucket = TrackBucket(99, 30, 3)

def test_add_car():
    trackbucket = TrackBucket(100,25, 1)
    trackbucket.add_car(Car(60, 20 , 20))
    assert len(trackbucket.bucket_list[0]) == 0
    assert len(trackbucket.bucket_list[1]) == 0
    assert len(trackbucket.bucket_list[2]) == 1
    assert len(trackbucket.bucket_list[3]) == 0

def test_car_has_moved():
    trackbucket = TrackBucket(100,25, 1)
    car = Car(60, 20 , 20)
    trackbucket.add_car(car)
    old_pos = car.position
    car.position = 20
    trackbucket.car_has_moved(car, old_pos)
    assert len(trackbucket.bucket_list[0]) == 1
    assert len(trackbucket.bucket_list[1]) == 0
    assert len(trackbucket.bucket_list[2]) == 0
    assert len(trackbucket.bucket_list[3]) == 0
