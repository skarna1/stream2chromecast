import codecs
import re

# Copyright (C) 2016-2017 Sami Karna
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# The software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with software.  If not, see <http://www.gnu.org/licenses/>.


class ConvertSrt2Vtt(object):
    """Simple srt to vtt converter. Converts only following:
       time stamps with comma to full stop
       prepends the file with WEBVTT header
    """
    WEBVTT_SUFFIX = ".vtt"
    WEBVTT_HEADER="WEBVTT\n\n"

    def convert_file(self, filename):
        content = self._read_file(filename)
        content = self._convert(content)
        filename = re.sub("\.[sS][rR][tT]", self.WEBVTT_SUFFIX, filename)
        return self._write_file(filename, content)

    def _read_file(self, filename):
        with open (filename, "r") as srt_file:
            content = srt_file.readlines()
        return content

    def _convert(self, lines):
        content = []
        content.append(self.WEBVTT_HEADER)
        for line in lines:
            if "-->" in line:
                line = line.replace(',', '.')
            content.append(line)
        return content

    def _write_file(self, filename, content):
        with open(filename, "w") as vtt_file:
            vtt_file.write(codecs.BOM_UTF8)
            vtt_file.writelines(content)
        return filename


