#!/usr/bin/env python
# coding: utf-8

import json
import sys

from analyze import *


def main():
    """

    """

    project_path = sys.argv[1]
    target_cache_path = 'cache'

    proj_info = load_from_project(project_path)

    with open(target_cache_path, 'w') as f:
        f.write(json.dumps(proj_info))

if __name__ == '__main__':
    main()

