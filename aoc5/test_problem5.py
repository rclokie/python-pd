from problem5 import *

def test_partition():
    assert partition(0,0,"")==0

def test_partition1():
    assert partition(0,127,"BBBBBBB")==127
    assert partition(0,127,"FFFFFFF")==0
    assert partition(0,127,"FBFBBFF")==44
    assert partition(0,127,"BFFFBBF")==70
    assert partition(0,127,"FFFBBBF")==14
    assert partition(0,127,"BBFFBBF")==102
    assert partition(0,7,"RRR")==7
    assert partition(0,7,"LLL")==0
    assert partition(0,7,"RLL")==4


def test_sums():
    assert parseRow("FBFBBFFRLR") == 357
    assert parseRow("BFFFBBFRRR") == 567
    assert parseRow("FFFBBBFRRR") == 119
    assert parseRow("BBFFBBFRLL") == 820

