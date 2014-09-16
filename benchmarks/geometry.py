import numpy as np

from photutils.geometry import circular_overlap_grid, elliptical_overlap_grid


def time_circular_small_exact():
    circular_overlap_grid(-4., 4., -4., 4., 10, 10, 3.,
                          use_exact=1, subpixels=1)


def time_circular_small_subpixel_1():
    circular_overlap_grid(-4., 4., -4., 4., 10, 10, 3.,
                          use_exact=0, subpixels=1)


def time_circular_small_subpixel_5():
    circular_overlap_grid(-4., 4., -4., 4., 10, 10, 3.,
                          use_exact=1, subpixels=5)


def time_circular_big_exact():
    circular_overlap_grid(-4., 4., -4., 4., 100, 100, 3.,
                          use_exact=1, subpixels=1)


def time_circular_big_subpixel_1():
    circular_overlap_grid(-4., 4., -4., 4., 100, 100, 3.,
                          use_exact=0, subpixels=1)


def time_circular_big_subpixel_5():
    circular_overlap_grid(-4., 4., -4., 4., 100, 100, 3.,
                          use_exact=1, subpixels=5)


def time_elliptical_small_exact():
    elliptical_overlap_grid(-4., 4., -4., 4., 10, 10, 3., 2., 1.,
                            use_exact=1, subpixels=1)


def time_elliptical_small_subpixel_1():
    elliptical_overlap_grid(-4., 4., -4., 4., 10, 10, 3., 2., 1.,
                            use_exact=0, subpixels=1)


def time_elliptical_small_subpixel_5():
    elliptical_overlap_grid(-4., 4., -4., 4., 10, 10, 3., 2., 1.,
                            use_exact=1, subpixels=5)


def time_elliptical_big_exact():
    elliptical_overlap_grid(-4., 4., -4., 4., 100, 100, 3., 2., 1.,
                            use_exact=1, subpixels=1)


def time_elliptical_big_subpixel_1():
    elliptical_overlap_grid(-4., 4., -4., 4., 100, 100, 3., 2., 1.,
                            use_exact=0, subpixels=1)


def time_elliptical_big_subpixel_5():
    elliptical_overlap_grid(-4., 4., -4., 4., 100, 100, 3., 2., 1.,
                            use_exact=1, subpixels=5)
