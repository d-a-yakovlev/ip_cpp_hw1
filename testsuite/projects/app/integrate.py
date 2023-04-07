#!/usr/bin/env python3

import os
import logging
import subprocess
import re


def check(cond):
    if not cond:
        raise RuntimeError("Check not passed")

def system_run_command(args, ignore_stderr = True, additional_env = dict()):
   command = ' '.join([str(arg) for arg in args]) # str - поддержка Path
   # print('Run command %s', command)
   cmd_env = os.environ.copy()
   cmd_env.update(additional_env)
   p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        env=cmd_env)
   output, errors = p.communicate()
   if p.returncode or (not ignore_stderr and errors):
       raise IOError("CMD = [{}]\nErrors: {}".format(command, errors if errors else "[]"))
   p.wait()
   result = output.decode("utf-8").strip()
   return result


path2bin = 'bin/app_for_integrate'


def test_content_string_short():
    res = system_run_command(['echo', "1 baza n", '|', path2bin])
    out_lines = res.split("\n")
    for _ in range(1):
        user_input_line = out_lines[0 + 3*_]
        content_line = out_lines[1 + 3*_]
        sort_content_line = out_lines[2 + 3*_]

        re_res = re.search(r': (.*) {', user_input_line)
        user_input = re_res.groups()[0]

        print(user_input_line, user_input)

        re_res = re.search(r'\[(.*)\]', content_line)
        content = re_res.groups()[0]

        print(content_line, content)

        re_res = re.search(r'\[(.*)\]', sort_content_line)
        sort_content = re_res.groups()[0]

        print(sort_content_line, sort_content)

        check(user_input == content)


def test_sort_string_short():
    res = system_run_command(['echo', "1 baza n", '|', path2bin])
    out_lines = res.split("\n")
    for _ in range(1):
        user_input_line = out_lines[0 + 3*_]
        content_line = out_lines[1 + 3*_]
        sort_content_line = out_lines[2 + 3*_]

        re_res = re.search(r': (.*) {', user_input_line)
        user_input = re_res.groups()[0]

        re_res = re.search(r'\[(.*)\]', content_line)
        content = re_res.groups()[0]
        
        re_res = re.search(r'\[(.*)\]', sort_content_line)
        sort_content = re_res.groups()[0]

        check(sort_content == ''.join(sorted(list(user_input))))


def test_content_string_view_short():
    res = system_run_command(['echo', "2 baza n", '|', path2bin])
    out_lines = res.split("\n")
    for _ in range(1):
        user_input_line = out_lines[0 + 3*_]
        content_line = out_lines[1 + 3*_]
        sort_content_line = out_lines[2 + 3*_]

        re_res = re.search(r': (.*) {', user_input_line)
        user_input = re_res.groups()[0]

        re_res = re.search(r'\[(.*)\]', content_line)
        content = re_res.groups()[0]
        
        re_res = re.search(r'\[(.*)\]', sort_content_line)
        sort_content = re_res.groups()[0]

        check(user_input == content)


def test_sort_string_view_short():
    res = system_run_command(['echo', "2 baza n", '|', path2bin])
    out_lines = res.split("\n")
    for _ in range(1):
        user_input_line = out_lines[0 + 3*_]
        content_line = out_lines[1 + 3*_]
        sort_content_line = out_lines[2 + 3*_]

        re_res = re.search(r': (.*) {', user_input_line)
        user_input = re_res.groups()[0]

        re_res = re.search(r'\[(.*)\]', content_line)
        content = re_res.groups()[0]
        
        re_res = re.search(r'\[(.*)\]', sort_content_line)
        sort_content = re_res.groups()[0]

        check(sort_content == ''.join(sorted(list(user_input))))


def test_pipeline_s_s_short():
    res = system_run_command(['echo', "1 baza y 1 not_baza n", '|', path2bin])
    out_lines = res.split("\n")
    for _ in range(2):
        user_input_line = out_lines[0 + 3*_]
        content_line = out_lines[1 + 3*_]
        sort_content_line = out_lines[2 + 3*_]

        re_res = re.search(r': (.*) {', user_input_line)
        user_input = re_res.groups()[0]

        re_res = re.search(r'\[(.*)\]', content_line)
        content = re_res.groups()[0]
        
        re_res = re.search(r'\[(.*)\]', sort_content_line)
        sort_content = re_res.groups()[0]

        check(user_input == content)
        check(sort_content == ''.join(sorted(list(user_input))))


def test_pipeline_s_sv_short():
    res = system_run_command(['echo', "1 baza y 2 not_baza n", '|', path2bin])
    out_lines = res.split("\n")
    for _ in range(2):
        user_input_line = out_lines[0 + 3*_]
        content_line = out_lines[1 + 3*_]
        sort_content_line = out_lines[2 + 3*_]

        re_res = re.search(r': (.*) {', user_input_line)
        user_input = re_res.groups()[0]

        re_res = re.search(r'\[(.*)\]', content_line)
        content = re_res.groups()[0]
        
        re_res = re.search(r'\[(.*)\]', sort_content_line)
        sort_content = re_res.groups()[0]

        check(user_input == content)
        check(sort_content == ''.join(sorted(list(user_input))))


def test_pipeline_sv_s_short():
    res = system_run_command(['echo', "2 baza y 1 not_baza n", '|', path2bin])
    out_lines = res.split("\n")
    for _ in range(2):
        user_input_line = out_lines[0 + 3*_]
        content_line = out_lines[1 + 3*_]
        sort_content_line = out_lines[2 + 3*_]

        re_res = re.search(r': (.*) {', user_input_line)
        user_input = re_res.groups()[0]

        re_res = re.search(r'\[(.*)\]', content_line)
        content = re_res.groups()[0]
        
        re_res = re.search(r'\[(.*)\]', sort_content_line)
        sort_content = re_res.groups()[0]

        check(user_input == content)
        check(sort_content == ''.join(sorted(list(user_input))))


def test_pipeline_sv_sv_short():
    res = system_run_command(['echo', "2 baza y 2 not_baza n", '|', path2bin])
    out_lines = res.split("\n")
    for _ in range(2):
        user_input_line = out_lines[0 + 3*_]
        content_line = out_lines[1 + 3*_]
        sort_content_line = out_lines[2 + 3*_]

        re_res = re.search(r': (.*) {', user_input_line)
        user_input = re_res.groups()[0]

        re_res = re.search(r'\[(.*)\]', content_line)
        content = re_res.groups()[0]
        
        re_res = re.search(r'\[(.*)\]', sort_content_line)
        sort_content = re_res.groups()[0]

        check(user_input == content)
        check(sort_content == ''.join(sorted(list(user_input))))


def test_content_string_long():
    res = system_run_command(['echo', "1 hellohello n", '|', path2bin])
    out_lines = res.split("\n")
    for _ in range(1):
        user_input_line = out_lines[0 + 3*_]
        content_line = out_lines[1 + 3*_]
        sort_content_line = out_lines[2 + 3*_]

        re_res = re.search(r': (.*) {', user_input_line)
        user_input = re_res.groups()[0]

        re_res = re.search(r'\[(.*)\]', content_line)
        content = re_res.groups()[0]

        re_res = re.search(r'\[(.*)\]', sort_content_line)
        sort_content = re_res.groups()[0]

        check(user_input == content)


def test_sort_string_long():
    res = system_run_command(['echo', "1 hellohello n", '|', path2bin])
    out_lines = res.split("\n")
    for _ in range(1):
        user_input_line = out_lines[0 + 3*_]
        content_line = out_lines[1 + 3*_]
        sort_content_line = out_lines[2 + 3*_]

        re_res = re.search(r': (.*) {', user_input_line)
        user_input = re_res.groups()[0]

        re_res = re.search(r'\[(.*)\]', content_line)
        content = re_res.groups()[0]
        
        re_res = re.search(r'\[(.*)\]', sort_content_line)
        sort_content = re_res.groups()[0]

        check(sort_content == ''.join(sorted(list(user_input))))


def test_content_string_view_long():
    res = system_run_command(['echo', "2 hellohello n", '|', path2bin])
    out_lines = res.split("\n")
    for _ in range(1):
        user_input_line = out_lines[0 + 3*_]
        content_line = out_lines[1 + 3*_]
        sort_content_line = out_lines[2 + 3*_]

        re_res = re.search(r': (.*) {', user_input_line)
        user_input = re_res.groups()[0]

        re_res = re.search(r'\[(.*)\]', content_line)
        content = re_res.groups()[0]
        
        re_res = re.search(r'\[(.*)\]', sort_content_line)
        sort_content = re_res.groups()[0]

        check(user_input == content)


def test_sort_string_view_long():
    res = system_run_command(['echo', "2 hellohello n", '|', path2bin])
    out_lines = res.split("\n")
    for _ in range(1):
        user_input_line = out_lines[0 + 3*_]
        content_line = out_lines[1 + 3*_]
        sort_content_line = out_lines[2 + 3*_]

        re_res = re.search(r': (.*) {', user_input_line)
        user_input = re_res.groups()[0]

        re_res = re.search(r'\[(.*)\]', content_line)
        content = re_res.groups()[0]
        
        re_res = re.search(r'\[(.*)\]', sort_content_line)
        sort_content = re_res.groups()[0]

        check(sort_content == ''.join(sorted(list(user_input))))


def test_pipeline_s_s_long():
    res = system_run_command(['echo', "1 hellohello y 1 goodbyegoodbye n", '|', path2bin])
    out_lines = res.split("\n")
    for _ in range(2):
        user_input_line = out_lines[0 + 3*_]
        content_line = out_lines[1 + 3*_]
        sort_content_line = out_lines[2 + 3*_]

        re_res = re.search(r': (.*) {', user_input_line)
        user_input = re_res.groups()[0]

        re_res = re.search(r'\[(.*)\]', content_line)
        content = re_res.groups()[0]
        
        re_res = re.search(r'\[(.*)\]', sort_content_line)
        sort_content = re_res.groups()[0]

        check(user_input == content)
        check(sort_content == ''.join(sorted(list(user_input))))


def test_pipeline_s_sv_long():
    res = system_run_command(['echo', "1 hellohello y 2 goodbyegoodbye n", '|', path2bin])
    out_lines = res.split("\n")
    for _ in range(2):
        user_input_line = out_lines[0 + 3*_]
        content_line = out_lines[1 + 3*_]
        sort_content_line = out_lines[2 + 3*_]

        re_res = re.search(r': (.*) {', user_input_line)
        user_input = re_res.groups()[0]

        re_res = re.search(r'\[(.*)\]', content_line)
        content = re_res.groups()[0]
        
        re_res = re.search(r'\[(.*)\]', sort_content_line)
        sort_content = re_res.groups()[0]

        check(user_input == content)
        check(sort_content == ''.join(sorted(list(user_input))))


def test_pipeline_sv_s_long():
    res = system_run_command(['echo', "2 hellohello y 1 goodbyegoodbye n", '|', path2bin])
    out_lines = res.split("\n")
    for _ in range(2):
        user_input_line = out_lines[0 + 3*_]
        content_line = out_lines[1 + 3*_]
        sort_content_line = out_lines[2 + 3*_]

        re_res = re.search(r': (.*) {', user_input_line)
        user_input = re_res.groups()[0]

        re_res = re.search(r'\[(.*)\]', content_line)
        content = re_res.groups()[0]
        
        re_res = re.search(r'\[(.*)\]', sort_content_line)
        sort_content = re_res.groups()[0]

        check(user_input == content)
        check(sort_content == ''.join(sorted(list(user_input))))


def test_pipeline_sv_sv_long():
    res = system_run_command(['echo', "2 hellohello y 2 goodbyegoodbye n", '|', path2bin])
    out_lines = res.split("\n")
    for _ in range(2):
        user_input_line = out_lines[0 + 3*_]
        content_line = out_lines[1 + 3*_]
        sort_content_line = out_lines[2 + 3*_]

        re_res = re.search(r': (.*) {', user_input_line)
        user_input = re_res.groups()[0]

        re_res = re.search(r'\[(.*)\]', content_line)
        content = re_res.groups()[0]
        
        re_res = re.search(r'\[(.*)\]', sort_content_line)
        sort_content = re_res.groups()[0]

        check(user_input == content)
        check(sort_content == ''.join(sorted(list(user_input))))


def test_size_string():
    res = system_run_command(['echo', "1 hellohello n", '|', path2bin])
    out_lines = res.split("\n")
    for _ in range(1):
        user_input_line = out_lines[0 + 3*_]
        content_line = out_lines[1 + 3*_]

        re_res = re.search(r'{(.*)}', user_input_line)
        user_input_size = re_res.groups()[0]

        re_res = re.search(r'{(.*)}', content_line)
        content_size = re_res.groups()[0]

        check(user_input_size == content_size)



tests = [
    test_content_string_short,
    test_sort_string_short,
    test_content_string_view_short,
    test_sort_string_view_short,
    test_pipeline_s_s_short,
    test_pipeline_s_sv_short,
    test_pipeline_sv_s_short,
    test_pipeline_sv_sv_short,
    test_content_string_long,
    test_sort_string_long,
    test_content_string_view_long,
    test_sort_string_view_long,
    test_pipeline_s_s_long,
    test_pipeline_s_sv_long,
    test_pipeline_sv_s_long,
    test_pipeline_sv_sv_long,
    test_size_string,
]

def run_tests():
    idx, test_name = 0, ""
    failed_count = 0

    print("="*5 + f"Integration tests of {path2bin}" + "="*5 + "\n")
    
    for i, test in enumerate(tests):
        idx, test_name = i + 1, test.__qualname__
        print(f"{idx}) {test_name} running", end=' ')
        try:
            test()
            print("OK!")
        except Exception as e:
            print(f"\n#{idx} test : {str(e)}")
            failed_count += 1
        print("-"*42)
    if failed_count == 0:
        print("\nTests passed")
    else:
        print(f"\n{failed_count} tests has failed")
    

if __name__ == "__main__":
    run_tests()
