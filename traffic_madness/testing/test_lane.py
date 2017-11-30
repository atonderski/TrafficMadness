import pytest

from traffic_madness.car import Car
from traffic_madness.track.trackbucket import TrackBucket


def test_default():
    trackbucket = TrackBucket(100, 25, 3)
    assert len(trackbucket.bucket_list) == 4


def test_raise_not_divisible():
    with pytest.raises(ValueError):
        trackbucket = TrackBucket(99, 30, 3)


def test_add_car():
    trackbucket = TrackBucket(100, 25, 1)
    trackbucket.add_car(Car(60, 20, 20))
    print(trackbucket.bucket_list)
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

def test_get_nearby_cars():
    trackbucket = TrackBucket(100, 25, 2)

    c1 = Car(0, 20, 20, 0)
    c2 = Car(60, 20, 20, 0)
    c3 = Car(60, 20, 20, 1)
    c4 = Car(50, 20, 20, 0)
    trackbucket.add_car(c1)
    trackbucket.add_car(c2)
    trackbucket.add_car(c3)
    trackbucket.add_car(c4)

    nearby_cars = trackbucket.get_nearby_cars(55)
    print(nearby_cars)
    assert c1 not in nearby_cars[0] and c1 not in nearby_cars[1]
    assert c2 in nearby_cars[0] and c2 not in nearby_cars[1]
    assert c3 in nearby_cars[1] and c3 not in nearby_cars[0]
    assert c4 in nearby_cars[0] and c4 not in nearby_cars[1]

def test_get_all_cars():
    trackbucket = TrackBucket(100, 25, 2)

    c1 = Car(0, 20, 20, 0)
    c2 = Car(60, 20, 20, 0)
    c3 = Car(60, 20, 20, 1)
    c4 = Car(50, 20, 20, 0)
    trackbucket.add_car(c1)
    trackbucket.add_car(c2)
    trackbucket.add_car(c3)
    trackbucket.add_car(c4)

    all_cars = trackbucket.get_all_cars()
    assert c1 in all_cars and c2 in all_cars and c3 in all_cars and c4 in all_cars
    assert len(all_cars) == 4
    assert trackbucket.get_num_cars() == 4
