import numpy as np

from functools import partial
from photutils import (aperture_photometry,
                       CircularAperture, CircularAnnulus,
                       EllipticalAperture, EllipticalAnnulus)


CLASSES = {}
CLASSES['circ'] = CircularAperture
CLASSES['circ_ann'] = CircularAnnulus
CLASSES['elli'] = EllipticalAperture
CLASSES['elli_ann'] = EllipticalAnnulus


class parametrize(object):

    def __init__(self, combinations):
        self.combinations = combinations

    def __call__(self, cls):

        for key in self.combinations:

            comb = self.combinations[key]
            name = key.lower().replace(',','').replace(' ', '_')

            if comb['error'] is True:
                error = np.ones(comb['dims'])
            else:
                error = None

            for aper in ['circ', 'circ_ann', 'elli', 'elli_ann']:

                for method in ['center', ('subpixel',1), ('subpixel',5), ('subpixel',10), 'exact']:

                    if isinstance(method, tuple):
                        method, subpixels = method
                    else:
                        subpixels = 1

                    parameters = {}
                    parameters['data_shape'] = comb['dims']
                    print(key, comb[aper])
                    parameters['apertures'] = CLASSES[aper](comb['pos'], *comb[aper])
                    parameters['method'] = method
                    parameters['subpixels'] = subpixels
                    parameters['error'] = error

                    method_name = "time_" + name + "_" + aper + "_" + method

                    if method == 'subpixel':
                        method_name = method_name + "_{0:02d}".format(subpixels)

                    setattr(cls, method_name, partial(cls.do_test, **parameters))
        return cls


COMBINATIONS = {}

name = "Small data, single small aperture"
c = COMBINATIONS[name] = {}
c['dims']     = (20, 20)
c['pos']      = (10., 10.)
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['iter']     = 1000
c['multiap']  = False
c['multipos'] = False
c['error'] = False

name = "Small data, error, single small aperture"
c = COMBINATIONS[name] = {}
c['dims']     = (20, 20)
c['pos']      = (10., 10.)
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['iter']     = 1000
c['multiap']  = False
c['multipos'] = False
c['error'] = True

name = "Big data, single small aperture"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (500., 500.)
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['iter']     = 1000
c['multiap']  = False
c['multipos'] = False
c['error'] = False

name = "Big data, error, single small aperture"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (500., 500.)
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['iter']     = 1000
c['multiap']  = False
c['multipos'] = False
c['error'] = True

name = "Big data, single big aperture"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (500., 500.)
c['circ']     = (50.,)
c['circ_ann'] = (50., 60.)
c['elli']     = (50., 20., 0.5)
c['elli_ann'] = (20., 50., 40., 0.5)
c['iter']     = 10
c['multiap']  = False
c['multipos'] = False
c['error'] = False

name = "Big data, error, single big aperture"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (500., 500.)
c['circ']     = (50.,)
c['circ_ann'] = (50., 60.)
c['elli']     = (50., 20., 0.5)
c['elli_ann'] = (20., 50., 40., 0.5)
c['iter']     = 10
c['multiap']  = False
c['multipos'] = False
c['error'] = True

name = "Small data, multiple small apertures"
c = COMBINATIONS[name] = {}
c['dims']     = (20, 20)
c['pos']      = (zip(np.random.uniform(5., 15., 1000), np.random.uniform(5., 15., 1000)))
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['iter']     = 1
c['multiap']  = False
c['multipos'] = True
c['error'] = False

name = "Small data, error, multiple small apertures"
c = COMBINATIONS[name] = {}
c['dims']     = (20, 20)
c['pos']      = (zip(np.random.uniform(5., 15., 1000), np.random.uniform(5., 15., 1000)))
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['iter']     = 1
c['multiap']  = False
c['multipos'] = True
c['error'] = True

name = "Big data, multiple small apertures"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (zip(np.random.uniform(250., 750., 1000), np.random.uniform(250., 750., 1000)))
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['iter']     = 1
c['multiap']  = False
c['multipos'] = True
c['error'] = False

name = "Big data, error, multiple small apertures"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (zip(np.random.uniform(250., 750., 1000), np.random.uniform(250., 750., 1000)))
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['iter']     = 1
c['multiap']  = False
c['multipos'] = True
c['error'] = True

name = "Big data, multiple big apertures"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (zip(np.random.uniform(250., 750., 100), np.random.uniform(250., 750., 100)))
c['circ']     = (50.,)
c['circ_ann'] = (50., 60.)
c['elli']     = (50., 20., 0.5)
c['elli_ann'] = (20., 50., 40., 0.5)
c['iter']     = 1
c['multiap']  = False
c['multipos'] = True
c['error'] = False

name = "Big data, error, multiple big apertures"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (zip(np.random.uniform(250., 750., 100), np.random.uniform(250., 750., 100)))
c['circ']     = (50.,)
c['circ_ann'] = (50., 60.)
c['elli']     = (50., 20., 0.5)
c['elli_ann'] = (20., 50., 40., 0.5)
c['iter']     = 1
c['multiap']  = False
c['multipos'] = True
c['error'] = True


@parametrize(COMBINATIONS)
class AperturePhotometry:

    def setup(self):
        self.positions = np.random.uniform(0., 20., 2000).reshape((1000, 2))

    def do_test(self, data_shape=None, apertures=None, method=None,
                subpixels=None, error=None):

        data = np.ones(data_shape)

        if error:
            error = np.ones(data_shape)
        else:
            error = None

        aperture_photometry(data, apertures, method=method, error=error,
                            subpixels=subpixels)
