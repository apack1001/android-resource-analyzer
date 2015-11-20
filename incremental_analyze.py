#!/usr/bin/env python
# coding: utf-8

import json
import sys
from analyze import *


def main():
    project_path = sys.argv[1]
    cache_path = sys.argv[2]
    target_cache_path = 'cache'

    cur_proj_info = load_from_project(project_path)
    prev_proj_info = load_from_cache(cache_path)
    with open(target_cache_path, 'w') as f:
        f.write(json.dumps(cur_proj_info))


    large = large_size_resources(project_path, 300)
    changes = diff_resource_change(prev_proj_info['assets_and_resources'],
            cur_proj_info['assets_and_resources'])
    similar_jars = similar_jar_packages(project_path)
    large_so_libs = large_size_dynamic_libraries(project_path, 300)

    report(measure = 1024,
            path = '.',
            report_filename = 'report',
            resources_diff = changes,
            large_resources = large,
            similar_jars = similar_jars,
            large_so_libs = large_so_libs
            )

if __name__ == '__main__':
    main()

