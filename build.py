#!/usr/bin/env python3
import argparse
import os
import shutil
import subprocess
import sys

PY = os.getenv("PY", "python")
PELICAN = os.getenv("PELICAN", "pelican")

BASEDIR = os.getcwd()
INPUTDIR = os.path.join(BASEDIR, "content")
OUTPUTDIR = os.path.join(BASEDIR, "output")
CONFFILE = os.path.join(BASEDIR, "pelicanconf.py")
PUBLISHCONF = os.path.join(BASEDIR, "publishconf.py")

GITHUB_PAGES_BRANCH = "main"

def run(cmd, cwd=None):
    print(f"> {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd)
    if result.returncode != 0:
        sys.exit(result.returncode)

def html(args):
    opts = build_opts(args)
    run(f"{PELICAN} \"{INPUTDIR}\" -o \"{OUTPUTDIR}\" -s \"{CONFFILE}\" {opts}")

def clean(args):
    if os.path.isdir(OUTPUTDIR):
        print(f"Removing {OUTPUTDIR}")
        shutil.rmtree(OUTPUTDIR)

def regenerate(args):
    opts = build_opts(args)
    run(f"{PELICAN} -r \"{INPUTDIR}\" -o \"{OUTPUTDIR}\" -s \"{CONFFILE}\" {opts}")

def serve(args):
    opts = build_opts(args)
    run(f"{PELICAN} -l \"{INPUTDIR}\" -o \"{OUTPUTDIR}\" -s \"{CONFFILE}\" {opts}")

def serve_global(args):
    opts = build_opts(args)
    run(f"{PELICAN} -l \"{INPUTDIR}\" -o \"{OUTPUTDIR}\" -s \"{CONFFILE}\" {opts} -b {args.server}")

def devserver(args):
    opts = build_opts(args)
    run(f"{PELICAN} -lr \"{INPUTDIR}\" -o \"{OUTPUTDIR}\" -s \"{CONFFILE}\" {opts}")

def devserver_global(args):
    opts = build_opts(args)
    run(f"{PELICAN} -lr \"{INPUTDIR}\" -o \"{OUTPUTDIR}\" -s \"{CONFFILE}\" {opts} -b 0.0.0.0")

def publish(args):
    opts = build_opts(args)
    run(f"{PELICAN} \"{INPUTDIR}\" -o \"{OUTPUTDIR}\" -s \"{PUBLISHCONF}\" {opts}")

def github(args):
    publish(args)
    run(f"ghp-import -m \"Generate Pelican site\" -b {GITHUB_PAGES_BRANCH} \"{OUTPUTDIR}\"")
    run(f"git push origin {GITHUB_PAGES_BRANCH}")

def build_opts(args):
    opts = []
    if args.debug:
        opts.append("-D")
    if args.relative:
        opts.append("--relative-urls")
    if args.port:
        opts.append(f"-p {args.port}")
    return " ".join(opts)

def main():
    parser = argparse.ArgumentParser(description="Pelican build tool")
    parser.add_argument("--debug", action="store_true", help="Enable debug (-D)")
    parser.add_argument("--relative", action="store_true", help="Use relative URLs")
    parser.add_argument("--port", type=int, help="Port for server commands")
    parser.add_argument("--server", default="0.0.0.0", help="Server address (for serve-global)")

    subparsers = parser.add_subparsers(dest="command", required=True)

    for cmd in [
        "html", "clean", "regenerate", "serve", "serve-global",
        "devserver", "devserver-global", "publish", "github"
    ]:
        subparsers.add_parser(cmd)

    args = parser.parse_args()

    commands = {
        "html": html,
        "clean": clean,
        "regenerate": regenerate,
        "serve": serve,
        "serve-global": serve_global,
        "devserver": devserver,
        "devserver-global": devserver_global,
        "publish": publish,
        "github": github,
    }

    commands[args.command](args)

if __name__ == "__main__":
    main()
