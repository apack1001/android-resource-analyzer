#!/usr/bin/env python
# coding: utf-8

import os
import json

from bjm_jsondiff import benjamin_jsondiff

from grip import export

def _all_resources_and_assets(path):
    pattern = "'\(main/res\)\|\(assets\)'"
    return _find_sth_by_pattern(path, "*.*", pattern)


def _all_dynamic_libraries(path):
    pattern = '\.so$'
    return _find_sth_by_pattern(path, "*.so", pattern)


def _all_jar_files(path):
    pattern = '\.jar$'
    return _find_sth_by_pattern(path, "*.jar", pattern)


def _find_sth_by_pattern(path, suffix, pattern):
    cmd = "find %s -name '*.*' | grep -e %s" % (path, pattern)
    filename_list = os.popen(cmd).read().split('\n')
    ret = {}
    ret['data'] = {}
    total_size = 0
    for filename in filename_list:
        if filename == '':
            continue
        key = filename.split(path)[1].lstrip('/')
        ret['data'][key] = {}
        size = os.path.getsize(filename)
        ret['data'][key]['size'] = size
        total_size += size

    ret['total_size'] = total_size

    return ret


def _large_size_dectect(resources, empathy):
    ret = []
    for filename, entry in resources['data'].iteritems():
        size = entry['size']
        if size > empathy * 1024:
            ret.append({"size": size, "file": filename})

    return ret


def similar_jar_packages(path):
    """
    Detect whether this project use similar jar files.
    For now, only similar json libraries detecting rule supported.
    """
    # TODO refactor. extract to a configuration file.
    json_pattern_list = ['gson', 'json-simple', 'fastjson']
    ret = {}
    ret['json']= {}
    ret['json']['list'] = []
    total_json_files_size = 0
    jarfiles = _all_jar_files(path)
    for filename, entry in jarfiles['data'].iteritems():
        size = entry['size']
        for pattern in json_pattern_list:
            if filename.find(pattern) != -1:
                ret['json']['list'].append({"size": size, "file": filename})
                total_json_files_size += size
                break

    ret['json']['total_size'] = total_json_files_size


    return ret



def diff_resource_change(base, now):
    """
    Calcuate resource changes of two different version project.

    @param base: base resource list
    @type base: an instance of C{dict}, each key-value pair looks like this:
        '<filepath>': {'size'}: <filesize>


    @param now: base resource list
    @type now: an instance of C{dict}, each key-value pair looks like this:
        '<filepath>': {'size'}: <filesize>

    @return an instance of changes
    """

    raw_res_differences = benjamin_jsondiff(base['data'], now['data'])

    ret = {}
    ret['increase'] = {}
    ret['increase']['count'] = 0
    ret['increase']['size'] = 0
    ret['increase']['list'] = []
    ret['decrease'] = {}
    ret['decrease']['count'] = 0
    ret['decrease']['size'] = 0
    ret['decrease']['list'] = []
    ret['add'] = {}
    ret['add']['count'] = 0
    ret['add']['size'] = 0
    ret['add']['list'] = []
    ret['remove'] = {}
    ret['remove']['count'] = 0
    ret['remove']['size'] = 0
    ret['remove']['list'] = []
    ret['add']['list'] = []
    ret['total'] = {}
    ret['total']['size_diff'] = 0
    ret['total']['size_diff_adjust'] = 0
    ret['total']['size_diff_rate'] = 0.0
    ret['trendcy'] = 'plain'

    for diff in raw_res_differences:
        if 'add' in diff:
            ret['add']['count'] += 1
            ret['add']['size'] += diff['value']['size']
            ret['add']['list'].append({'file': diff['add'], "size": diff['value']['size']})
            ret['total']['size_diff'] += diff['value']['size']
        elif 'remove' in diff:
            ret['remove']['count'] += 1
            ret['remove']['size'] += diff['prev']['size']
            ret['remove']['list'].append({'file': diff['remove'], "size": diff['prev']['size']})
            ret['total']['size_diff'] -= diff['prev']['size']
        elif 'replace' in diff:
            if diff['prev'] < diff['value']:
                size = diff['value'] - diff['prev']
                ret['increase']['size'] += size
                ret['increase']['count'] += 1
                ret['increase']['list'].append({'file': diff['replace'][0:-5], "size": size})
            elif diff['prev'] > diff['value']:
                size = diff['prev'] - diff['value']
                ret['decrease']['size'] += size
                ret['decrease']['count'] += 1
                ret['decrease']['list'].append({'file': diff['replace'][0:-5], "size": size})
            ret['total']['size_diff'] += (diff['value'] - diff['prev'])

    total_size_diff_rate = float(now['total_size'] - base['total_size']) * \
            100.0 / float(base['total_size'])

    ret['total']['size_diff_rate'] = total_size_diff_rate

    ret['total']['size_diff_adjust'] = now['total_size'] - base['total_size']

    if ret['total']['size_diff'] > 0:
        ret['trendcy'] = 'increase'
    elif ret['total']['size_diff'] < 0:
        ret['trendcy'] = 'decrease'
    return ret


def dulplicated_resource_remover(res, assets):
    # TODO
    """

    """
    ret = {}

    return ret


def large_size_resources(path, empathy):
    """
    Find all the resources which size are larger than L{empathy}(KB).

    @param path: path of resources
    @type path: C{str}

    @param empathy: empathy, measured in KB
    @type empathy: C{int}

    @return all hit resources
    """

    """
    # Deprecated
    cmd = "du -sk `find %s -name '*.*' | grep -e '\(/res\)\|\(assets\)' | grep -v xml`  | sort -r -n | awk '{if ($1 >= %d) {print;}}'" % (path, empathy)
    output = os.popen(cmd)
    raw =  output.read()
    lines = raw.split('\n')
    ret = []
    for line in lines:
        if line == '':
            continue
        entries = line.split('\t')
        size = entries[0]
        filename = entries[1].split(path)[1].lstrip('/')
        ret.append({"size": size, "file": filename})
    """

    resources = _all_resources_and_assets(path)

    return _large_size_dectect(resources, empathy)



def large_size_dynamic_libraries(path, empathy):
    """
    Find all the resources which size are larger than L{empathy}(KB).

    @param path: path of resources
    @type path: C{str}

    @param empathy: empathy, measured in KB
    @type empathy: C{int}

    @return all hit resources
    """
    resources = _all_dynamic_libraries(path)

    return _large_size_dectect(resources, empathy)



def load_from_project(path):
    ret = {}
    ret['assets_and_resources'] = _all_resources_and_assets(path)
    print 'assets'
    ret['jar'] = _all_jar_files(path)
    print 'jar packages'
    ret['dynamic_so_libs'] = _all_dynamic_libraries(path)
    print 'dynamic libraries'

    return ret


def load_from_cache(path):
    ret = None
    with open(path) as f:
        ret = json.load(f)
    return ret


def save(**kwargs):
    """
    save assets, resources, java packages, dynamic libraries properties.
    """
    out_filename = kwargs['out_filename']
    out_path = kwargs['out_path']
    assets_and_resources = kwargs['assets_and_resources']
    jars = kwargs['jar']
    dynamic_so_libs = kwargs['so']

    filename = out_path + '/' + out_filename
    json_result = {}
    json_reuslt['assets_and_resources'] = assets_and_resources
    json_result['jar'] = jars
    json_result['dynamic_so_libs'] = dynamic_so_libs
    content = json.dumps(json_result)

    with open(filename, 'w') as f:
        f.write(content)


def report(**kwargs):
    """
    """
    resources_diff = kwargs['resources_diff']
    measure = 1024 if 'measure' not in kwargs else kwargs['measure']
    report_filename = 'report' if 'report_filename' not in kwargs else kwargs['report_filename']
    # FIXME
    title = u'android资源分析结果' if 'title' not in kwargs else kwargs['title']
    path = '.' if 'path' not in kwargs else kwargs['path']

    report_md_tpl = ""
    # FIXME
    with open("report_tpl.md") as f:
        report_md_tpl = f.read()

    var = []

    tmp = resources_diff['add']['count']
    var.append(tmp)
    tmp = resources_diff['add']['size']
    var.append(tmp)

    tmp = resources_diff['remove']['count']
    var.append(tmp)
    tmp = resources_diff['remove']['size']
    var.append(tmp)

    tmp = resources_diff['increase']['count']
    var.append(tmp)
    tmp = resources_diff['increase']['size']

    var.append(tmp)
    tmp = resources_diff['decrease']['count']
    var.append(tmp)
    tmp = resources_diff['decrease']['size']
    var.append(tmp)

    # FIXME
    tmp = '增加' if resources_diff['total']['size_diff'] > 0 else '减少'
    var.append(tmp)

    tmp = resources_diff['total']['size_diff']
    var.append(tmp)

    tmp = resources_diff['total']['size_diff_rate']
    var.append(tmp)

    # large resources
    large_resources = kwargs['large_resources']
    tpl = '''
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td></td>
    </tr>
    '''
    tmp = ''
    for res in large_resources:
        tmp += tpl % (res['file'], res['size'] / measure)
    var.append(tmp)

    # large dynamic libraries
    large_so_libs = kwargs['large_so_libs']
    tpl = '''
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td></td>
    </tr>
    '''
    tmp = ''
    for so in large_so_libs:
        tmp += tpl % (so['file'], so['size'] / measure)
    var.append(tmp)

    # similar jar packages
    similar_jars = kwargs['similar_jars']
    tpl = '''
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td></td>
    </tr>
    '''
    tmp = ''
    for jar in similar_jars['json']['list']:
        tmp += tpl % (jar['file'], jar['size'] / measure)
    var.append(tmp)


    report_md = report_md_tpl % tuple(var)

    report_md_path = path + '/' + report_filename + ".md"
    with open(report_md_path, 'w') as f:
        f.write(report_md)

    report_html_path = path + '/' + report_filename + '.html'

    export(path=report_md_path, out_filename = report_html_path, title = title)

