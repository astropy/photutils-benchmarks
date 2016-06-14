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

name = "sing_sm_ap"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (500., 500.)
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['error'] = False

name = "sing_sm_ap_err"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (500., 500.)
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['error'] = True

name = "sing_bg_ap"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (500., 500.)
c['circ']     = (50.,)
c['circ_ann'] = (50., 60.)
c['elli']     = (50., 20., 0.5)
c['elli_ann'] = (20., 50., 40., 0.5)
c['error'] = False

name = "sing_bg_ap_err"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (500., 500.)
c['circ']     = (50.,)
c['circ_ann'] = (50., 60.)
c['elli']     = (50., 20., 0.5)
c['elli_ann'] = (20., 50., 40., 0.5)
c['error'] = True

name = "mult_sm_ap"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (list(zip(np.random.uniform(250., 750., 100), np.random.uniform(250., 750., 100))))
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['error'] = False

name = "mult_sm_ap_err"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (list(zip(np.random.uniform(250., 750., 100), np.random.uniform(250., 750., 100))))
c['circ']     = (5.,)
c['circ_ann'] = (5., 6.)
c['elli']     = (5., 2., 0.5)
c['elli_ann'] = (2., 5., 4., 0.5)
c['error'] = True

name = "mult_bg_ap"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (list(zip(np.random.uniform(250., 750., 10), np.random.uniform(250., 750., 10))))
c['circ']     = (50.,)
c['circ_ann'] = (50., 60.)
c['elli']     = (50., 20., 0.5)
c['elli_ann'] = (20., 50., 40., 0.5)
c['error'] = False

name = "mult_bg_ap_err"
c = COMBINATIONS[name] = {}
c['dims']     = (1000, 1000)
c['pos']      = (list(zip(np.random.uniform(250., 750., 10), np.random.uniform(250., 750., 10))))
c['circ']     = (50.,)
c['circ_ann'] = (50., 60.)
c['elli']     = (50., 20., 0.5)
c['elli_ann'] = (20., 50., 40., 0.5)
c['error'] = True


class parametrize:

    def __init__(self, combinations, aperture_type):
        self.combinations = combinations
        self.aperture_type = aperture_type

    def __call__(self, cls):

        for key in sorted(self.combinations.keys()):

            comb = self.combinations[key]
            name = key.lower().replace(',','').replace(' ', '_')

            for method in [('subpixel',1), ('subpixel',5), 'exact']:

                if isinstance(method, tuple):
                    method, subpixels = method
                else:
                    subpixels = 1

                parameters = {}
                parameters['data_shape'] = comb['dims']
                parameters['apertures'] = CLASSES[self.aperture_type](comb['pos'], *comb[self.aperture_type])
                parameters['method'] = method
                parameters['subpixels'] = subpixels
                parameters['error'] = comb['error']

                method_name = "time_" + name + "_" + method

                if method == 'subpixel':
                    method_name = method_name + "_{0:02d}".format(subpixels)

                # The par=parameters is to force closure
                setattr(cls, method_name, lambda self, par=parameters: cls.do_test(**par))

        return cls


class BaseAperturePhotometry:

    timeout = 120.0

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


@parametrize(COMBINATIONS, 'circ')
class CircularAperturePhotometry(BaseAperturePhotometry):
    pass

@parametrize(COMBINATIONS, 'circ_ann')
class CircularAnnulusPhotometry(BaseAperturePhotometry):
    pass

@parametrize(COMBINATIONS, 'elli')
class EllipticalAperturePhotometry(BaseAperturePhotometry):
    pass

@parametrize(COMBINATIONS, 'elli_ann')
class EllipticalAnnulusPhotometry(BaseAperturePhotometry):
    pass
