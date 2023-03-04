import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

import sys
sys.path.append("/brevets")

import arrow

from mypymongo import brevet_insert, brevet_fetch

def test_1():

    brevet_dis = 200

    begin_date = '2021-01-01T12:00'

    control_list = [{"km": 75, "open_t": '2021-01-01T2:12', "close_t": '2021-01-01T5:00'}, 
                {"km": 100, "open_t": '2021-01-01T2:56', "close_t": '2021-01-01T6:40'}, 
                {"km": 125, "open_t": '2021-01-01T3:41', "close_t": '2021-01-01T8:20'}]

    assert brevet_insert(begin_date, brevet_dis, control_list)

def test_2():

    brevet_dis2 = 200

    begin_date2 = '2021-01-01T12:00'

    control_list2 = [{"km": 100, "open_t": '2021-01-01T2:56', "close_t": '2021-01-01T6:40'}, 
                {"km": 150, "open_t": '2021-01-01T4:25', "close_t": '2021-01-01T10:00'}, 
                {"km": 175, "open_t": '2021-01-01T5:09', "close_t": '2021-01-01T11:40'}]

    assert brevet_insert(begin_date2, brevet_dis2, control_list2)    