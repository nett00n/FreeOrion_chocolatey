from jinja2 import Template
import hashlib
import os
import re
import requests


def main():
    global github_prefix
    github_prefix = "https://github.com/"
    github_user = "freeorion"
    github_repo = "freeorion"

    github_html_data_lines = get_data_from_github(github_user, github_repo)
    latest_version = get_latest_version_from_html(github_html_data_lines)
    win32_url = get_download_url_from_html("Win32", github_html_data_lines, latest_version)
    win32_hashsum = get_sha256_from_url(win32_url)
    render_choco_files(latest_version, win32_url, win32_hashsum)

def get_sha256_from_url(url):
    r = requests.get(url)
    with open('tmp_file', 'wb') as f:
        f.write(r.content)
    with open('tmp_file',"rb") as f:
        bytes = f.read()
        readable_hash = hashlib.sha256(bytes).hexdigest();
    if os.path.exists('tmp_file'):
        os.remove('tmp_file')
    return(readable_hash)

def render_choco_files(latest_version, win32_url, win32_hashsum):
    nuspec_xml = define_nuspec_template()
    nuspec_xml_text = nuspec_xml.render(latest_version = latest_version)
    # print(nuspec_xml_text)
    file = open('freeorion.nuspec', 'w')
    file.write(nuspec_xml_text)
    file.close()
    chocolateyinstall_ps1 = define_chocolateinstall_template()
    chocolateyinstall_ps1_text = chocolateyinstall_ps1.render(win32_url = win32_url, win32_hashsum = win32_hashsum)
    file = open('tools/chocolateyinstall.ps1', 'w')
    file.write(chocolateyinstall_ps1_text)
    file.close()
    # print(chocolateyinstall_ps1_text)

def define_nuspec_template():
    with open("templates/nuspec.j2") as f:
        template_text = f.read()

    jinja_template = Template(template_text)
    return(jinja_template)

def define_chocolateinstall_template():
    with open("templates/chocolateyinstall.ps1.j2") as f:
        template_text = f.read()
    jinja_template = Template(template_text)
    return(jinja_template)

def get_data_from_github(github_user, github_repo):
    github_postfix = "/releases"
    RemoteURL = github_prefix + github_user + "/" + github_repo + github_postfix
    RemoteData = requests.get(RemoteURL)
    lines = RemoteData.text
    return(lines.split("\n"))


def get_download_url_from_html(keyphrase, github_html_data_lines, version):

    for line in github_html_data_lines:
        if "href" not in line:
            continue
        if "/releases/" not in line:
            continue
        if "download" not in line:
            continue
        if version not in line:
            continue
        fields = line.split('"')
        if keyphrase not in line:
            continue
        url = github_prefix + fields[1]
        return(url)

def get_latest_version_from_html(github_html_data_lines):
    version = ''

    for line in github_html_data_lines:
        if "href" not in line:
            continue
        if "/releases/" not in line:
            continue
        if "SDK" in line:
            continue
        if "/tag/" in line:
            test1 = line.split('"')
            test2 = test1[1].split('/')
            version = test2[-1]
            version = re.sub(r"v", "", version)
            print(version)
            return(version)


if __name__ == "__main__":
    main()