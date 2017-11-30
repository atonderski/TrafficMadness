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
    print(trackbucket.bucket_list)
    assert len(trackbucket.bucket_list[-1]) == 0
    assert len(trackbucket.bucket_list[1]) == 0
    assert len(trackbucket.bucket_list[2]) == 1
    assert len(trackbucket.bucket_list[3]) == 0
