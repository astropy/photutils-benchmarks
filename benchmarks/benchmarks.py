import numpy as np

from photutils import aperture_photometry, CircularAperture


class AperturePhotometry:

    def setup(self):
        self.d = {}
        for x in range(500):
            self.d[x] = None

    def do_test(self, data_shape, apertures, method, error):
        
        data = np.ones(data_shape)
        
        if error:
            error = np.ones(data_shape)
        else:
            error = None
            
        aperture_photometry(data, apertures, method=method, error=error)

    def time_basic_center(self):
        """
        Small data, single small aperture
        """
        aperture_photometry(data_shape=(20, 20),
                            apertures=CircularAperture((10, 10), 5),
                            method='center',
                            error=False)

    def time_basic_subpixels_1(self):
        """
        Small data, single small aperture
        """
        aperture_photometry(data_shape=(20, 20),
                            apertures=CircularAperture((10, 10), 5),
                            method='subpixel', subpixels=1,
                            error=False)

    def time_basic_subpixels_5(self):
        """
        Small data, single small aperture
        """
        aperture_photometry(data_shape=(20, 20),
                            apertures=CircularAperture((10, 10), 5),
                            method='subpixel', subpixels=5,
                            error=False)

    def time_basic_subpixels_10(self):
        """
        Small data, single small aperture
        """
        aperture_photometry(data_shape=(20, 20),
                            apertures=CircularAperture((10, 10), 5),
                            method='subpixel', subpixels=10,
                            error=False)

    def time_basic_exact(self):
        """
        Small data, single small aperture
        """
        aperture_photometry(data_shape=(20, 20),
                            apertures=CircularAperture((10, 10), 5),
                            method='exact',
                            error=False)

class MemSuite:
    def mem_list(self):
        return [0] * 256
