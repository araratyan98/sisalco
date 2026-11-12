#!/bin/sh
# Builds the static site into docs/ (works on GitHub Pages, Netlify, Cloudflare Pages, any static host)
set -e
cd "$(dirname "$0")/.."
rm -rf docs && mkdir docs
cp -r web/logo.png web/gate.jpg web/gate-bg.webp web/ph web/tex docs/
touch docs/.nojekyll
{
  printf '<!doctype html>\n<html lang="hy"><head><meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<style>:root{color-scheme:dark}body{margin:0;font:14px system-ui}img{max-width:100%%}[hidden]{display:none!important}</style>\n'
  # the page starts with its own <title>/<meta>/<style>; those are valid inside <head> too
  cat web/sis-alco.html
  printf '\n</body></html>\n'
} > docs/index.html
echo "built docs/ ($(du -sh docs | cut -f1))"
