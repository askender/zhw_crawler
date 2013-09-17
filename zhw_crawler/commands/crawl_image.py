#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_image():
    import requests
    for i in xrange(1, 50):
        image_url = 'http://www.flazx.us/themes/Meditation/images/body-bg-%s.png' % i
        print(image_url)
        image_name = 'body-bg-%s.png' % i
        r = requests.get(image_url)
        if r.status_code == 200:
            with open(image_name, 'w') as f:
                for chunk in r.iter_content():
                    f.write(chunk)


if __name__ == '__main__':
    get_image()
