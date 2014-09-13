import numpy as np

from photutils import (aperture_photometry,
                       CircularAperture, CircularAnnulus,
                       EllipticalAperture, EllipticalAnnulus)


CLASSES = {}
CLASSES['circ'] = CircularAperture
CLASSES['circ_ann'] = CircularAnnulus
CLASSES['elli'] = EllipticalAperture
CLASSES['elli_ann'] = EllipticalAnnulus

COMBINATIONS = {}

name = "Small data, single small aperture"
c = COMBINATIONS[name] = {}
c['dims']     = (20, 20)
c['pos']      = (10., 10.)
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['error'] = False

name = "Small data, error, single small aperture"
c = COMBINATIONS[name] = {}
c['dims']     = (20, 20)
c['pos']      = (10., 10.)
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['error'] = True

name = "Big data, single small aperture"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (500., 500.)
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['error'] = False

name = "Big data, error, single small aperture"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (500., 500.)
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['error'] = True

name = "Big data, single big aperture"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (500., 500.)
c['circ']     = (50.,)
c['circ_ann'] = (50., 60.)
c['elli']     = (50., 20., 0.5)
c['elli_ann'] = (20., 50., 40., 0.5)
c['error'] = False

name = "Big data, error, single big aperture"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (500., 500.)
c['circ']     = (50.,)
c['circ_ann'] = (50., 60.)
c['elli']     = (50., 20., 0.5)
c['elli_ann'] = (20., 50., 40., 0.5)
c['error'] = True

name = "Small data, multiple small apertures"
c = COMBINATIONS[name] = {}
c['dims']     = (20, 20)
c['pos']      = (zip(np.random.uniform(5., 15., 1000), np.random.uniform(5., 15., 1000)))
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['error'] = False

name = "Small data, error, multiple small apertures"
c = COMBINATIONS[name] = {}
c['dims']     = (20, 20)
c['pos']      = (zip(np.random.uniform(5., 15., 1000), np.random.uniform(5., 15., 1000)))
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['error'] = True

name = "Big data, multiple small apertures"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (zip(np.random.uniform(250., 750., 1000), np.random.uniform(250., 750., 1000)))
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['error'] = False

name = "Big data, error, multiple small apertures"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (zip(np.random.uniform(250., 750., 1000), np.random.uniform(250., 750., 1000)))
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['error'] = True

name = "Big data, multiple big apertures"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (zip(np.random.uniform(250., 750., 100), np.random.uniform(250., 750., 100)))
c['circ']     = (50.,)
c['circ_ann'] = (50., 60.)
c['elli']     = (50., 20., 0.5)
c['elli_ann'] = (20., 50., 40., 0.5)
c['error'] = False

name = "Big data, error, multiple big apertures"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (zip(np.random.uniform(250., 750., 100), np.random.uniform(250., 750., 100)))
c['circ']     = (50.,)
c['circ_ann'] = (50., 60.)
c['elli']     = (50., 20., 0.5)
c['elli_ann'] = (20., 50., 40., 0.5)
c['error'] = True


class parametrize:

    def __init__(self, combinations):
        self.combinations = combinations

    def __call__(self, cls):

        for key in sorted(self.combinations.keys()):

            comb = self.combinations[key]
            name = key.lower().replace(',','').replace(' ', '_')

            for aper in ['circ', 'circ_ann', 'elli', 'elli_ann']:

                for method in ['center', ('subpixel',1), ('subpixel',5), ('subpixel',10), 'exact']:

                    if isinstance(method, tuple):
                        method, subpixels = method
                    else:
                        subpixels = 1

                    parameters = {}
                    parameters['data_shape'] = comb['dims']
                    parameters['apertures'] = CLASSES[aper](comb['pos'], *comb[aper])
                    parameters['method'] = method
                    parameters['subpixels'] = subpixels
                    parameters['error'] = comb['error']

                    method_name = "time_" + name + "_" + aper + "_" + method

                    if method == 'subpixel':
                        method_name = method_name + "_{0:02d}".format(subpixels)

                    # The par=parameters is to force closure
                    setattr(cls, method_name, lambda self, par=parameters: cls.do_test(**par))

        return cls


@parametrize(COMBINATIONS)
class AperturePhotometry:

    @staticmethod
    def do_test(data_shape=None, apertures=None, method=None,
                subpixels=None, error=None):

        data = np.ones(data_shape)

        if error:
            error = np.ones(data_shape)
        else:
            error = None

        aperture_photometry(data, apertures, method=method, error=error,
                            subpixels=subpixels)
