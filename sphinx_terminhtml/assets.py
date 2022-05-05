import os
import tempfile
from pathlib import Path

import requests
from sphinx.application import Sphinx
from sphinx.util.fileutil import copy_asset

asset_file_url = "https://unpkg.com/@terminhtml/bootstrap@1.0.0-alpha.9/dist/@terminhtml-bootstrap.umd.js"
asset_file_name = "@terminhtml-bootstrap.umd.js"


def download_and_copy_asset_files(app: Sphinx, exc):
    if exc is not None:
        # Build failed, don't copy assets
        return

    asset_content = requests.get(asset_file_url).text

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir) / asset_file_name
        tmp_path.write_text(asset_content)

        # Copy asset files
        copy_asset(str(tmp_path), os.path.join(app.outdir, "_static"))


def register_assets(app: Sphinx):
    app.connect("build-finished", download_and_copy_asset_files)
    app.add_js_file(asset_file_name)
