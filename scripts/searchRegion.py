#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 03:33:05 2017

@author: yisubai
"""

import pickle

def search_region(location,interval):
    """
    Find the region from correct pickle
    Return: return binray formate interval
    location: whcih chr 
    interval: tuple with (start,end)
    """

    with open('DNase-seq-human.pkl', 'rb') as f:
        mynewlist = pickle.load(f)
    
    index_of_chr = location[2:]
    target_chr = mynewlist[index_of_chr]
    
    return find_closest_region(interval,target_chr)
    
    



def find_closest_region(interval, sorted_region_list):
	"""
	Find one of the regions from the sorted_region_list that overlaps the input inteval. 
	Return: index and the found interval
	This function does not return the interval with the maximum overlap. It return one of the regions that have a overlap
	"""
	start = 0
	end = len(sorted_region_list) - 1
	while end >= start:
		mid = (end + start) // 2
		if have_intersection(interval, sorted_region_list[mid]):
			return mid, sorted_region_list[mid]
		elif interval[0] > sorted_region_list[mid][1]:
			start = mid + 1
		elif interval[1] < sorted_region_list[mid][0]:
			end = mid - 1
	return -1, None



def have_intersection(interval1, interval2):
	"""
	Returns boolean if the intervals have some intersection or not
	"""
	two_inside_one = interval1[0] <= interval2[0] and interval1[1] >= interval2[1]
	one_inside_two = interval1[0] >= interval2[0] and interval1[1] <= interval2[1]
	two_overlapps_left = interval1[0] <= interval2[1] and interval1[0] >= interval2[0]
	two_overlapps_right = interval1[1] <= interval2[1] and interval1[1] >= interval2[0]

	return two_inside_one or one_inside_two or two_overlapps_left or two_overlapps_right