# -*- coding: utf-8 -*-

debug = True
port = 6868

web_server = {
    'login_url': '/login',
    'template_path': 'templates',
    'static_path': 'static',
    'locale_path': 'locale',
    'xsrf_cookies': False,
    'cookie_secret': "57525244df45sdf5sf",
    'autoescape': None,
    'debug': debug,
}
log = {
    'log_max_bytes': 5 * 1024 * 1024,  # 5M
    'backup_count': 10,
    'log_path': {
        # logger of running server; DONOT change the name 'logger'
        'logger': 'logger/files/server.log',
        # logger of user behavior
        'user_logger': 'logger/files/user.log'
    }
}
