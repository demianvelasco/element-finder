PORT = 8000
URL = "http://localhost:{}".format(PORT)
SITE_LOCATION = 'test_site/index.html'

csv_log_single_site_init = [(False, False, True), (False, False, False)]
# TODO: Add logs and csv tests
#    (True, False, True), (False, False, True), (True, True, True)]

variations = [{
    'element': 'id',
    'element_id': 'header',
    'expected_amount': 1,
}, {
    'element': 'id',
    'element_id': 'headerLeft',
    'expected_amount': 1,
}, {
    'element': 'id',
    'element_id': 'headerRight',
    'expected_amount': 1,
}, {
    'element': 'id',
    'element_id': 'wrapall',
    'expected_amount': 1,
}, {
    'element': 'id',
    'element_id': 'sidebar',
    'expected_amount': 1,
}, {
    'element': 'id',
    'element_id': 'logo',
    'expected_amount': 1,
}, {
    'element': 'id',
    'element_id': 'sidebarContent',
    'expected_amount': 1,
}, {
    'element': 'id',
    'element_id': 'main',
    'expected_amount': 1,
}
]

TESTS = list()

for variation in variations:
    for options in csv_log_single_site_init:
        init_params = dict()
        init_params['url'] = URL
        init_params['element_id'] = variation['element_id']
        init_params['csv'] = options[0]
        init_params['debug'] = options[1]
        init_params['single_site'] = options[2]
        TESTS.append(
            (init_params, variation['element'], variation['element_id'], URL, options[0], options[1], options[2], variation['expected_amount']))
